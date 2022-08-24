# MKVToolNix Sequential Batch Mapper

## Notes:

 - I created this as way to process a bunch of mkv files in a series using the original MKVToolNix-batch program as a reference .
 - It's not that hard to use and you only need Python 3.
 - It's really useful for merging individual subtitles or dub tracks; anything that needs to be mapped to something.
 - I also nicked the GitHub readme for this from the MKVToolNix-batch
   repo sorry.

## Dependencies:

-  [MKVToolNix](https://www.fosshub.com/MKVToolNix.html)

-  [Python 3](https://www.python.org/downloads/)

## Usage:

1. Make sure all your MKV files have the same name apart from the number of the episode. 

2. Open `mkvtoolnix-gui.exe`.

3. Insert all the media for your first episode of the batch.

5. Do your edits here in the GUI including naming the output file whatever you want at the bottom if you'd like. (Leave the episode number how it is for now)

6. Go to `Menu Bar > Multiplexer > Create option file`, and save it as 'options.json' in the same directory where all MKV files to be processed are. You can then close the GUI.

7. Open said JSON file with your favourite editor:

- Where there is an episode number (S01E**01**), replace the number with the text `EPNUM` (S01E**EPNUM**)

- Do this for all the file paths in the JSON file.

6. Download [mkvtoolnix_merge_mapper.py](https://raw.githubusercontent.com/montypx/MKVToolNix-Sequential-Batch-Mapper/main/mkvtoolnix_merge_mapper.py) from this repository and put it in the working directory with all the files so far.

7. Find the `mkvmerge.exe` executable within MKVToolNix and get its path (`Shift + Right-Click > Copy as path` from Windows File Explorer).

8. Edit `mkvtoolnix_merge_mapper.py` and insert your path to `mkvmerge.exe` from step 6 into the quotes after the variable `mkv_merge_path` . You MUST include two backslashes `\\` in the path, where there is only one, for this to work.

9. Run `mkvtoolnix_merge_mapper.py` by double-clicking it.
  
10.  When prompted enter the first episode number and last episode number and your files will be sequentially created in the `mkvmerge_out` directory as it goes on.

11. Pretend you didn't see any of the hideous code that took me like 3 hours to write.

## License

Code licensed under GNU General Public License v3.0.
