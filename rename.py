import os
import sys
import glob
import ntpath
import logging

# Change this to any style
# If you change the naming structure don't forget to change line 25 "_".join(TITLE.split("_")[:2]) 
TITLE = "DBS_ep_720p"

def main():
    root, ext = os.path.splitext(sys.argv[0])
    logging.basicConfig(filename=root + '.log', level=logging.INFO)
    logging.info("Started with parameter " + str(sys.argv))

    if len(sys.argv) == 1:
        print("This program require one parameter!")
        sys.exit(1)

    try:
        root, ext = os.path.splitext(sys.argv[1])
        fileName = ntpath.basename(root)
        path, dirs, files = next(os.walk(os.path.dirname(sys.argv[1])))
        splitName = "_".join(TITLE.split("_")[:2])
        ep = len(glob.glob1(path, '*' + ext))
        epCount = len(glob.glob1(path, splitName + '*' + ext)) # Get the number of episode exist
       	epCount += 1 # Total episod exist + 1 = Episode for the current file
       	fileNameNew =  splitName + str(epCount) + '_' + TITLE.split('_')[2] + ext
        # Rename the file
        os.rename(os.path.join(path, fileName + ext), os.path.join(path, fileNameNew))
        logging.info("Rename file success from "  + fileName + ext  + " to " + fileNameNew)

    except:
        print("Error during renaming " + fileName + ext)
        print("Error", sys.exc_info())
        logging.error("Error during renaming " + fileName + str(sys.exc_info()))

if __name__  == "__main__":
    main()
