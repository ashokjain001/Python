from datetime import datetime
import os
import glob

def createFile():
    #using datetime as file name
    D = datetime.now()
    outfile = D.strftime("%Y-%m-%d-%I-%M-%S-%f")

    #obtaining all the files from the path that needs to be merged
    os.chdir("/Users/ashokjain/Desktop/Python/Sample-Files")
    inputfile = glob.glob("*.txt")

    #preserving original path where write file needs to be saved after merge
    savedpath = "/Users/ashokjain/Desktop/Python"
    completeName = os.path.join(savedpath, outfile + ".txt")

    #actual merge
    with open(completeName, "w") as writefile:
        for files in inputfile:
            with open(files, "r") as infile:
                writefile.write(infile.readline())

    writefile.close()
    os.chdir(savedpath)

print createFile()