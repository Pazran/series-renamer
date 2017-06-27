import os
import re
import sys
import logging
import tvdb_api
from os.path import basename

TITLE = "Seven Mortal Sins"
NAME_FORMAT = "Seven Mortal Sins"
SEASON = 1

## choose style
## Anime Style 1 = NAME_FORMAT + EP + EPISODE NAME
## TV Show Style 2 = NAME_FORMAT + SXXEXX + EPNAME

STYLE = 1
rename = False

def getInfo(fpath):
    
    try:

        t = tvdb_api.Tvdb()
        root, ext = os.path.splitext(fpath)
        consPath, consDir, consFile = next(os.walk(os.path.dirname(fpath)))
        pattern = ["(-+)(\d+)(-+)","(-+|\s|_+)(ep\d+|EP\d\+|\d+)(-+|\s|_+)",
                   "(s\d+|S\d+)(e\d+|E\d+)","\s\d+(\s|.)","(-+)(\d+)","Ep[.-](\d+)"] # Filename patterns

        ### Search if filename pattern exist in pattern list ###

        for pt in pattern:
            result = re.search(pt,basename(root))
            if result:
                rawEp = (result.group()).lower()
                ep = rawEp.replace('-','').replace('_','').replace('ep','').replace("s" + "{0:0=2d}".format(SEASON), '').replace('e','').replace('-','').replace('.','')
                rename = True
                print("Renaming episode: " + ep)
                break # stop the pattern search after it found one to prevent duplicate

            elif result == None:
                rename = False

        if ext not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2" , ".srt"]:
            return

        ### rename = True if one of the filename pattern exist ###

        if rename:
            info = t[TITLE][SEASON][int(ep)]
            epName = info['episodename'].replace('?','').replace(':','')

            ### Naming style. Anime or Season TV Show. ###

            if STYLE == 1:
                newFileName = NAME_FORMAT + " " + str("{0:0=3d}".format(int(ep))) + ' - ' + epName + ext
            elif STYLE == 2:
                newFileName = NAME_FORMAT + " S" + str("{0:0=2d}".format(int(SEASON))) + "E" + str("{0:0=2d}".format(int(ep))) + " - " + epName + ext

            if (fpath != os.path.join(consPath, newFileName)):
                os.rename(fpath, os.path.join(consPath, newFileName))
                logging.info("Rename file success from " + fpath + " to " + consPath + newFileName)

        else:
            return

    except:
        print("Error during renaming " + fpath)
        print("Error", sys.exc_info())
        logging.error("Error during renaming " + fpath + str(sys.exc_info()))

def main():

    root, ext = os.path.splitext(sys.argv[0])
    logging.basicConfig(filename=root + '.log', level=logging.INFO)
    logging.info("Started with parameter " + str(sys.argv))

    if len(sys.argv) == 1:
        print("This program require one parameter!")
        sys.exit(1)

    ### Iterate for multiple files

    for path in sys.argv[1:]:
        if os.path.isdir(path):
            for dirPath, subDir, files, in os.walk(path):
                for file in files:
                    filePath = os.path.join(dirPath, file)
                    getInfo(filePath)
        else:
            getInfo(path)

if __name__  == "__main__":
    main()
