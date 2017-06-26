# Series Renamer

I made this script for personal use. This script make use of the awesome tvdb_api.

## Scenario

I have too many series especially anime with crappy naming scheme. So i decided to write a script to rename it all at once and fetch the information from thetvdb.com api by using the open source tvdb_api module for python. Now all i have to do is select all and send to renamer.cmd and boom.:smile:

## Details

This script using the batch functionality and *send to* in windows inspired by [subtitle-downloader](https://github.com/manojmj92/subtitle-downloader).

If anyone want to use this for other series you have to change the TITLE, SEASON, NAME_FORMAT in the *renamer.py*

Current pattern that the script detect:
- name with underscore ex: "seriesname_ep01_"
- name with spacees ex: "seriesname 001 blablabal"
- name with pattern like {anysymbols}XXX{anysymbols} ex: "--001--"(mostly from animeheaven)

Example:

TITLE = 'Hunter x Hunter (2011)'

SEASON = 1

NAME_FORMAT = 'HxH'

Old file name "Hunter-x-Hunter-1-720p.mp4"

New file name will be NAME_FORMAT + (episode) + episodename

So *"Hunter-x-Hunter-1-720p.mp4"* --> *"HxH 001 - Departure x And x Friends.mp4"*

How to make it work:
- Open exploere.exe type *shell:sendto*
- Copy and past the *renamer.cmd* here
- Put *renamer.py* in *D:\\*

Now just right click the file > Send To > renamer.cmd (*Note: do it in order from episode 1 to final episode*)
You can also select multiple files.

## Notes

If the file name do not have the episode it will not be rename. Obviously internet connection required to fetch the series informations.

If anyone have better suggestion feel free to edit.
