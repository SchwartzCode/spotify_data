import json
import os
from tabulate import tabulate

class Printer():
    def __init__(self, max_print_amount:int=50):
        # maximum number of items printed when calling print_sorted_dict_data
        self.max_print_amount = max_print_amount
        self.ms_TO_hrs = 3600000
        self.HRS_to_MINS = 60
        
    def print_sorted_dict_data(self, dict_in: dict, column_headers: list):
        # pretty print data in <dict_in> and label columns with <column_headers>
        
        song_info_to_print = []        
        
        for i, item in enumerate(dict_in):
            print_row = [i+1, item[0]]
            
            for key in item[1].keys():
                print_row.append(item[1][key])

            song_info_to_print.append(print_row)
            
            if i >= self.max_print_amount-1:
                break
            
        print("\n\n", tabulate(song_info_to_print, headers=column_headers))
    
    def print_streaming_history(self, streaming_history_dict):
        '''
        print top <self.max_print_amount> songs in streaming history, sorted by number of plays
        '''
        
        sorted_songs = sorted(streaming_history_dict.items(), key=lambda x: x[1]['time_played'], reverse=True)
        print(f"{len(streaming_history_dict.keys())} unique songs listen to. Top {self.max_print_amount}:")
        
        print_col_headers = ['Rank', 'Song Name', 'Hours Listened', 'Plays', 'Average Play [mins]']
        
        self.print_sorted_dict_data(sorted_songs, print_col_headers)

class Library(Printer):
    
    def __init__(self, path: str, max_print_amount:int=50):
        print(f'Loading data from: {path}')
        super().__init__(max_print_amount=max_print_amount)

        f = open(path)
        self.lib = json.load(f)
        
    def tally_artist_and_song_appearances(self):
        # count up appearances of songs and artists in playlists
        
        playlists = self.lib['playlists']
        
        self.playlist_data = {'artists':{}, 'songs':{}}
        
        for plst in playlists:
            print(f"Loading in playlist: {plst['name']}")
            
            for song in plst['items']:
                
                # catches glitchy imported songs
                if song['track'] is None:
                    continue
                
                song_name = song['track']['trackName']
                if song_name in self.playlist_data['songs'].keys():
                    self.playlist_data['songs'][song_name]['appearances'] += 1
                else:
                    self.playlist_data['songs'][song_name] = {'appearances': 1}
                
                artist_name = song['track']['artistName']
                if artist_name in self.playlist_data['artists'].keys():
                    self.playlist_data['artists'][artist_name]['appearances'] += 1
                else:
                    self.playlist_data['artists'][artist_name] = {'appearances': 1}
                
    def print_playlist_data(self):
        '''
        prints top <self.max_print_amount> songs and artists, sorted by
        number of appearances in playlists
        '''
        
        sorted_songs = sorted(self.playlist_data['songs'].items(), key=lambda x: x[1]['appearances'], reverse=True)
        print(f"{len(self.playlist_data['songs'].keys())} unique songs in library")
        song_print_col_headers = ["Rank", "Song", "# of Playlist Appearances"]
        self.print_sorted_dict_data(sorted_songs, song_print_col_headers)

        sorted_artists = sorted(self.playlist_data['artists'].items(), key=lambda x: x[1]['appearances'], reverse=True)
        print(f"\n\n{len(self.playlist_data['artists'].keys())} unique artists in library")
        artist_print_col_headers = ["Rank", "Artist", "# of Songs in Playlists"]
        self.print_sorted_dict_data(sorted_artists, artist_print_col_headers)

  
class StreamingHistory(Printer):
    
    def __init__(self, path: str, max_print_amount:int=50):
        super().__init__(max_print_amount=max_print_amount)
        print(f'Loading data from: {path}')

        f = open(path)
        self.hist = json.load(f)
        
    def load_streaming_history(self):
        '''
        Count number of plays and time played for each song in loaded streaming history
        '''
        
        self.streaming_data = {}
        
        for elem in self.hist:
            song_name = elem["trackName"]
            time_played = elem["msPlayed"] / self.ms_TO_hrs
            
            if song_name in self.streaming_data.keys():
                self.streaming_data[song_name]['time_played'] += time_played
                self.streaming_data[song_name]['plays'] += 1
                self.streaming_data[song_name]['average_play'] = self.HRS_to_MINS * \
                                                                 self.streaming_data[song_name]['time_played'] / \
                                                                 self.streaming_data[song_name]['plays']

            else:
                self.streaming_data[song_name] = {'time_played': time_played, 'plays': 1, 
                                                  'average_play':self.HRS_to_MINS*time_played}

    def print_info(self):
        self.print_streaming_history(self.streaming_data)

class BigDataStreamingHistory(Printer):
    def __init__(self, folder_path: str, max_print_amount:int=150):
        super().__init__(max_print_amount=max_print_amount)
        print(f'Loading data from folder: {folder_path}')

        self.data_dict = {}

        self.load_data(folder_path)
        
    def load_data(self, folder_path):

        for file in os.listdir(folder_path):
            if file.startswith("endsong"):

                file_path = os.path.join(folder_path, file)
                self.add_file_data_to_dict(file_path)
    
    def add_file_data_to_dict(self, file_path):
        print(f"Saving data from: {file_path}")
        f = open(file_path)
        input_file = json.load(f)
                
        for elem in input_file:
            song_name = elem["master_metadata_track_name"]
            time_played = elem["ms_played"] / self.ms_TO_hrs
            
            if song_name is None:
                # either a podcast or a song imported into spotify
                continue

            if song_name in self.data_dict.keys():
                self.data_dict[song_name]['time_played'] += time_played
                self.data_dict[song_name]['plays'] += 1
                self.data_dict[song_name]['average_play'] = self.HRS_to_MINS * \
                                                            self.data_dict[song_name]['time_played'] / \
                                                            self.data_dict[song_name]['plays']
            else:
                self.data_dict[song_name] = {'time_played': time_played, 'plays': 1, 
                                             'average_play': self.HRS_to_MINS*time_played}

    def print_info(self):
        self.print_streaming_history(self.data_dict)