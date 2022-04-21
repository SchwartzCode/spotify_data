import argparse
from song_data import BigDataStreamingHistory, Library, StreamingHistory

parser = argparse.ArgumentParser(description='Hello there :D')
parser.add_argument('path', metavar='<path>', type=str, nargs='+',
                    help='path to the playlist json file')
parser.add_argument('-jdt', metavar='-jdt', type=str,
                    default="BigDataStreamingHistory",
                    help='type of JSON file being read in. Options: ["StreamingHistory", "Library", "BigDataStreamingHistory]')

args = parser.parse_args()

if __name__=="__main__":
    
    json_type = args.jdt
    print(json_type)
    
    if json_type == 'StreamingHistory':
        dat = StreamingHistory(args.path[0])
        dat.load_streaming_history()
        dat.print_info()
    
    elif json_type == 'BigDataStreamingHistory':
        dat = BigDataStreamingHistory(args.path[0])
        dat.print_info()
        
    elif json_type == 'Library':
        dat = Library(args.path[0])
        dat.tally_artist_and_song_appearances()
        dat.print_playlist_data()

    