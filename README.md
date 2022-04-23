# Parse Personal Spotify Streaming History

![output_full_data](https://user-images.githubusercontent.com/496532/164879502-6e2c7ed2-dd96-46d5-ab9d-35cea890e5a9.png)

## Setup
To install dependencies, run `pip install -r requirements.txt`

### Getting spotify data
[Information on how to get your data from Spotify here](https://support.spotify.com/us/article/data-rights-and-privacy-settings/)

The data you request from the Privacy Settings has your streaming history for the past year, and has a song_data.StreamingHistory json type. You can get your full history by [requesting it from Spotify](https://support.spotify.com/us/article/contact-us/) (the "send us a message" option gets a response in a few minutes), and that folder will contain several song_data.BigStreamingHistory json files titled endsong_x.json, with x starting at 0 and increasing.

### Cleaning spotify data
You might need to delete some special characters from the imported JSON files. VScode's `vscode-position` extension is very helpful with tracking these down from the error messages.

I stored some repeat offenders of this in `json_breaking_characters.txt`. Using regex to do search and replace sped up the process a lot. For example, if you want to replace the characters Á and À with A, you can search for `[ÁÀ]` (ctrl+f in VScode) and then replace all occurences of those characters with `A` (ctr+h in VScode). You can also delete all occurences of characters by replacing them with nothing.

## How to run the script

`python main.py <path>`

Where <path> is either the path to the folder of your entire data history (BigDataStreamingHistory) or the json file for your last year of streaming history (StreamingHistory) or playlists (Library). Default behavior assumes BigDataStreamingHistory.
  
Optional Arguments
  -jdt=<data_type>
  
  Where <data_type> is either StreamingHistory, Library, or BigDataStreamingHistory. Default is BigDataStreamingHistory.
