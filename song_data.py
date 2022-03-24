import json
import string

class Library():
    
    def __init__(self, path: str):
        print(f'Loading data from: {path}')

        f = open(path)
        self.lib = json.load(f)
        
    def load_song_data_all_playlists(self):
        playlists = self.lib['playlists']
        
        data = {'artists':{}, 'songs':{}}
        
        
        for plst in playlists:
            try:
                
                print(f"Loading in playlist: {plst['name']}")
                
                for song in plst['items']:
                    song_name = song['track']['trackName']
                    if song_name in data['songs'].keys():
                        data['songs'][song_name] += 1
                    else:
                        data['songs'][song_name] = 1
                    
                    artist_name = song['track']['artistName']
                    if artist_name in data['artists'].keys():
                        data['artists'][artist_name] += 1
                    else:
                        data['artists'][artist_name] = 1
            except:
                print("error")
                continue
        
        sorted_songs = sorted(data['songs'].items(), key=lambda x: x[1], reverse=True)
        print(f"{len(data['songs'].keys())} unique songs in library")
        print('Top Songs:\t[number of appearances]')
        
        for i, item in enumerate(sorted_songs):
            print(f"{i}\t {item[0]} \t\t {item[1]} ")
        
            if i > 50:
                break

        
        sorted_artists = sorted(data['artists'].items(), key=lambda x: x[1], reverse=True)
        print(f"\n\n{len(data['artists'].keys())} unique artists in library")
        print('Top Artists: \t[number of songs in playlists]')
        
        for i, item in enumerate(sorted_artists):
            print(f"{i}\t {item[0]} \t\t {item[1]}")
        
            if i > 50:
                break
        
        return data

        

        
  
class StreamingHistory():
    
    def __init__(self, path: str):
        print(f'Loading data from: {path}')

        f = open(path)
        self.hist = json.load(f)
        
    def load_streaming_history(self):
        
        data = {}
        
        for elem in self.hist:
            song_name = elem["trackName"]
            time_played = elem["msPlayed"] / 3600000
            
            if song_name in data.keys():
                data[song_name] += time_played
            else:
                data[song_name] = time_played
        
        sorted_songs = sorted(data.items(), key=lambda x: x[1], reverse=True)
        print(len(data.keys()))
        
        for i, item in enumerate(sorted_songs):
            print(f"{i}\t {item[0]} \t\t {item[1]:.2f} [hours]")
        
            if i > 50:
                return data
