from __future__ import print_function
from asyncio.windows_events import NULL
from importlib.resources import contents
import sys
import math

totalTime = 0
lastPlaceInQueue = 0
global qList

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
    global qList
    qList = readIn(args[3], args[2])
    q = initialQ(qList, args[2])
    #totalEntries = len(q)
    if (args[1] == "FIFO"):
        fifo(args[2], qList)
        print(f"Our total time is: {totalTime} milliseconds")
    elif(args[1] == "SSTF"):
        #for i in q:
            #print(f"{i}")
        sstf(args[2], q)
        print(f"Our total time is: {totalTime}")
    exit(0)

"""This method opens the file and reads in the data """
def readIn(file, qSize):
    global lastPlaceInQueue
    queueList = []
    with open(file, 'r') as f:
        for line in f.readlines():
            queueList.append(int(line.rstrip('\n')))
            #print(f"Value appended: {line}")
    return queueList


"""This fillQueue method will find our next value from the list of values and append it to the list"""
def fillQueue(q, lastIndex, indexToFill):
    if (indexToFill is None):
        nextValue = q[lastIndex]
    return nextValue

def initialQ(queue, qSize):
    count = 0
    q = []
    for i in queue:
        if(count < qSize):
            q.append(i)
            count += 1
        else:
            break
    print(f"Count from initialQ: {count}")
    return q
        
            

"""This method will run the FIFO algorithm to store our data"""
def fifo(qSize, queue):
    global totalTime
    global lastPlaceInQueue
    lastPlaceInQueue = qSize - 1
    totalValues = len(queue) - 1
    #print(f"our len of queue is: {totalValues}")
    cylinder = 0
    count = 0
    while True:
        if (count <= totalValues):
            #print(f"Our totalValues:{totalValues}")
            time = ((1 + (abs(cylinder - queue[0]) * .15) + 1) + 4.2)
            #print(f"Time: {time}")
            cylinder = queue[0]
            #print(f"Cylinder {cylinder}")
            totalTime += time
            count += 1
            queue.pop(0)
            if (lastPlaceInQueue < totalValues):
                queue.append(fillQueue(queue, lastPlaceInQueue, None))
                lastPlaceInQueue += 1
            #print(f"Last place in Queue {lastPlaceInQueue}")
            #print(f"count: {count}")
        else:
            break
    
def shorestLocation(queue, cylinder):
    #firstValue = queue[0]
    #proximity = abs(cylinder - firstValue)
    print(f"cyl: {cylinder}")
    shortest = abs(queue[0] - cylinder)
    index = 0
    retainerIndex = 1
    for i in queue:
        #print(f"i: {i}")
        index += 1
        if ((abs(cylinder - i)) < shortest):
            #print(f"cyl, i, abs, shortest, index: {cylinder, i, abs(cylinder - i), shortest, index}")
            shortest = abs(cylinder - i)
            retainerIndex = index
            #print(f"Closest Value is {proximity}")
    #print(f"Our closest values is: {proximity}")    
    #print(f"Our final index is: {retainerIndex}")
    #print(f"abs of cylinder and i is and proximity is and return index is: {first, retainerIndex - 1}")
    return retainerIndex - 1

def sstf(qSize, queue):
    global totalTime
    global qList
    totalValues = len(queue) - 1
    global lastPlaceInQueue
    lastPlaceInQueue = qSize - 1
    cylinder = 0
    count = 0
    while True:
        if (count <= totalValues):
            index = shorestLocation(queue, cylinder)
            time = ((1 + (abs(cylinder - queue[index]) * .15) + 1) + 4.2)
            print(f"Our returned value is: {queue[index]}")
            totalTime += time
            cylinder = queue[index]
            #print(f"cyl: {cylinder}")
            queue.pop(index)
            count += 1
        else:
            break


main()


