import os
import argparse

def scrub_files(files, scrub_chars_txt):
    print("bla")

parser = argparse.ArgumentParser(description='Scrub out characters in JSON files that make json.load angry')
parser.add_argument('json_folder_path', metavar='<path>', type=str, nargs='+',
                    help='path to the playlist json file')
parser.add_argument('characters_to_scrub_txt', metavar='<chars_to_scrub.txt>', type=str,
                    help='text file of characters to remove from json files')

if __name__=="__main__":
    
    print("aa")