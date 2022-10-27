from __future__ import print_function
import sys

totalTime = 0
lastPlaceInQueue = 0

"""Enter parameters as such: "Please enter in Algorith Type (C-SCAN, SSTF, or FIFO) | Queue Size | Input file name"""
def main():
    len(sys.argv)
    args = []
    args = sys.argv
    #for i in args:
        #print(f"{i}")
    #Converting args[2] to an integer
    args[2] = int(args[2])
    if len(args) != 4:
        print("You are missing a parameter please enter algorithm type, queue size, and input file.... exiting")
        exit(0)
    if (args[1] != "FIFO"):
        print("Please enter in a valid algorithm - FIFO, SSTF, C-SCAN")
    if (isinstance(args[2], int) == False):
        print("Enter an integer value for parameter two.... exiting")
        exit(0)
    q = []
    q = openFile(args[3], args[2])
    for i in q:
        print(f"{i}")

"""This method opens the file and reads in the data """
def openFile(file, qSize):
    valid = True
    x = 0
    queueList = []
    with open(file, 'r') as f:
        for line in f.readlines():
            #print(f"{line}")
            if (x <= qSize - 1):
                queueList.append(line.rstrip('\n'))
                x += 1
            else:
                break
    return queueList

#Test

main()


