import json
from tabulate import tabulate

class Library():
    
    def __init__(self, path: str, max_print_amount=50):
        print(f'Loading data from: {path}')

        f = open(path)
        self.lib = json.load(f)
        self.max_print_amount = max_print_amount
        
    def load_song_data_all_playlists(self):
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
                    self.playlist_data['songs'][song_name] += 1
                else:
                    self.playlist_data['songs'][song_name] = 1
                
                artist_name = song['track']['artistName']
                if artist_name in self.playlist_data['artists'].keys():
                    self.playlist_data['artists'][artist_name] += 1
                else:
                    self.playlist_data['artists'][artist_name] = 1
                
    def print_playlist_data(self):
        
        sorted_songs = sorted(self.playlist_data['songs'].items(), key=lambda x: x[1], reverse=True)
        print(f"{len(self.playlist_data['songs'].keys())} unique songs in library")
        song_print_col_headers = ["Rank", "Song", "# of Playlist Appearances"]
        self.print_dict_data(sorted_songs, song_print_col_headers)

        sorted_artists = sorted(self.playlist_data['artists'].items(), key=lambda x: x[1], reverse=True)
        print(f"\n\n{len(self.playlist_data['artists'].keys())} unique artists in library")
        artist_print_col_headers = ["Rank", "Artist", "# of Songs in Playlists"]
        self.print_dict_data(sorted_artists, artist_print_col_headers)


    def print_dict_data(self, dict_in, column_headers):
        
        song_info_to_print = []        
        
        for i, item in enumerate(dict_in):
            song_info_to_print.append([i+1, item[0], item[1]])
            
            if i >= self.max_print_amount-1:
                break
            
        print(tabulate(song_info_to_print, headers=column_headers))

  
class StreamingHistory():
    
    def __init__(self, path: str, max_print_amount=50):
        print(f'Loading data from: {path}')

        f = open(path)
        self.hist = json.load(f)
        self.max_print_amount = max_print_amount
        
    def load_streaming_history(self):
        
        self.streaming_data = {}
        
        for elem in self.hist:
            song_name = elem["trackName"]
            time_played = elem["msPlayed"] / 3600000 # convert ms to hours
            
            if song_name in self.streaming_data.keys():
                self.streaming_data[song_name]['time_played'] += time_played
                self.streaming_data[song_name]['plays'] += 1
            else:
                self.streaming_data[song_name] = {'time_played': time_played, 'plays': 1}
        
    def print_streaming_history(self):
        sorted_songs = sorted(self.streaming_data.items(), key=lambda x: x[1]['plays'], reverse=True)
        print(f"{len(self.streaming_data.keys())} unique songs listen to. Top {self.max_print_amount}:")
        
        print_col_headers = ['Rank', 'Song Name', 'Plays', 'Hours Listened']
        
        self.print_dict_data(sorted_songs, print_col_headers)
        
    def print_dict_data(self, dict_in, column_headers):
        
        song_info_to_print = []        
        
        for i, item in enumerate(dict_in):
            song_info_to_print.append([i+1, item[0], item[1]['plays'], item[1]['time_played']])
            
            if i >= self.max_print_amount-1:
                break
            
        print(tabulate(song_info_to_print, headers=column_headers))
