# Mucking about with my spotify data

To install dependencies, run `pip install -r requirements.txt`

You might need to delete some special characters from the imported JSON files. VScode's `vscode-position` extension is very helpful with this.

I stored some repeat offenders of this in `json_breaking_characters.txt`. Using regex to do search and replace sped up the process a lot. For example, if you want to replace the characters Á and À with A, you can search for `[ÁÀ]` in VScode (ctrl+f) and then replace all occurences of those characters with `A` (ctr+h in VScode). You can also delete all occurences of characters by replacing them with nothing.
