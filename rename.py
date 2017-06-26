import os
import re
import sys
import logging
import tvdb_api

TITLE = "Hunter x Hunter (2011)"
SEASON = 1
NAME_FORMAT = 'HxH'

def getInfo(fpath):
    
    try:
        t = tvdb_api.Tvdb()
        root, ext = os.path.splitext(fpath)
        consPath, consDir, consFile = next(os.walk(os.path.dirname(fpath)))
        pattern = ["(-+)(\d+)(-+)","(-+|\s|_+)(ep\d+|EP\d+|\d+)(-+|\s|_+)"] # AnimeHeaven files name pattern

        for pt in pattern:
            result = re.search(pt,fpath)
            if result:
                rawEp = (result.group()).lower()         
                ep = rawEp.replace('-','').replace('_','').replace('ep','').replace('-','')

        if ext not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
            return
        
        if result or result2:
            print(ep)
            info = t[TITLE][SEASON][int(ep)]
            epName = info['episodename'].replace('?','').replace('!','')
            newFileName = NAME_FORMAT + " " +str("{0:0=3d}".format(int(ep))) + ' - ' + epName + ext

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
