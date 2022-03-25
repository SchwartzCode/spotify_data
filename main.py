import argparse
from song_data import Library, StreamingHistory

parser = argparse.ArgumentParser(description='Look at music')
parser.add_argument('path', metavar='<path>', type=str, nargs='+',
                    help='path to the playlist json file')
parser.add_argument('-jdt', metavar='--json_data_type', type=str,
                    default="StreamingHistory",
                    help='type of JSON file being read in. Options: ["StreamingHistory", "Library"]')

args = parser.parse_args()

if __name__=="__main__":
    
    json_type = args.jdt
    
    if json_type == 'StreamingHistory':
        dat = StreamingHistory(args.path[0])
        dat.load_streaming_history()
        dat.print_streaming_history()
        
    elif json_type == 'Library':
        dat = Library(args.path[0])
        dat.tally_artist_and_song_appearances()
        dat.print_playlist_data()

    