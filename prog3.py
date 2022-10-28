from __future__ import print_function
from asyncio.windows_events import NULL
from importlib.resources import contents
import sys
import math

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
    q = readIn(args[3], args[2])
    if (args[1] == "FIFO"):
        fifo(args[2], q)
        print(f"Our total time is: {totalTime} milliseconds")
    #for i in q:
        #print(f"{i}")
    exit(0)

"""This method opens the file and reads in the data """
def readIn(file, qSize):
    global lastPlaceInQueue
    x = 0
    queueList = []
    with open(file, 'r') as f:
        for line in f.readlines():
            queueList.append(line.rstrip('\n'))
    return queueList



def fillQueue(q, lastIndex, indexToFill):
    if (indexToFill is None):
        nextValue = q[lastIndex]
    return nextValue



"""This method will run the FIFO algorithm to store our data"""
def fifo(qSize, queue):
    global totalTime
    cylinder = 0
    count = 0
    for i in queue:
        if (count <= qSize -1):
            time = (1 + (abs(cylinder - int(i)) * .15) + 1) + 4.2
            cylinder = int(i)
            totalTime += time
            count += 1
            queue.pop()
            queue.append(fillQueue(queue, qSize + 1, None))
        else:
            break
    

def sstf(queue):
    global totalTime
    cylinder = 0
    for i in queue:
        i += i


main()


