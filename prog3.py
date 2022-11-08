from __future__ import print_function
from asyncio.windows_events import NULL
from importlib.resources import contents
import sys
import math

totalTime = 0
global qList

"""Enter parameters as such: "Please enter in Algorith Type (C-SCAN, SSTF, or FIFO) | Queue Size | Input file name
This is the main function call for our program. This takes in three parameters and then will return our total time and QSize
"""
def main():
    len(sys.argv)
    args = []
    args = sys.argv
    args[2] = int(args[2])
    if len(args) != 4:
        print("You are missing a parameter please enter algorithm type, queue size, and input file.... exiting")
        exit(0)
    #if (args[1] != "FIFO" or "CSCAN" or "SSTF" ):
        #print("Please enter in a valid algorithm - FIFO, SSTF, CSCAN")
        #exit(0)
    if (isinstance(args[2], int) == False):
        print("Enter an integer value for parameter two.... exiting")
        exit(0)
    global qList
    qList = readIn(args[3])
    q = initialQ(qList, args[2])
    if (args[1] == "FIFO"):
        fifo(args[2], q)
    elif(args[1] == "SSTF"):
        sstf(args[2], q)
    elif(args[1] == "CSCAN"):
        cscan(args[2], q)
    print(f"Our total time is and after div: {totalTime, totalTime/len(qList)} milliseconds with QSize: {args[2]}")
    exit(0)

"""This method opens the file and reads in the data and strips any newline found 
Params:
file - This is the input file object that will be read.
returns:
queueList - A list of every element in the file
"""
def readIn(file):
    global lastPlaceInQueue
    queueList = []
    with open(file, 'r') as f:
        for line in f.readlines():
            queueList.append(int(line.rstrip('\n')))
    return queueList

"""Creating our initial queue with the elements we want to start reading
Params:
queue - This is a list of items we will be initializing
qSize - Maximum number of elements in the queue
Returns:
q - A list of items in the queue
"""
def initialQ(queue, qSize):
    count = 0
    q = []
    for i in queue:
        if(count < qSize):
            q.append(str(i) + ',' + '0')
            count += 1
        else:
            break
    return q

"""Adds time to our queue values dependent on time parameter
Params:
q - A list of queue items
time - a value in milliseconds
Return:
q - A list of elements with updated times in the queue
"""    
def addTime(q, time):
    i = 0
    for item in q:
        qElement = item.split(',')
        q[i] = str(qElement[0] + ',' + str((float(qElement[1]) + time)))
        i += 1
    return q

"""This returns the next queue integer value after parsing it out of the string
Params:
q - A list of queue items
index - default is None type indicating that it needs to grab the first element in the list and convert it, otherwise the specified one
Returns:
cyl - The integer value of the cylinder specified
"""
def parseQ(q, index=None):
    cyl = 0
    if not index:
        item = q[0].split(',')
        cyl = int(item[0])
    else:
        item = q[index].split(',')
        cyl = int(item[0])
    return cyl
        
"""This returns the time in float type after parsing it out of the string
Params:
q - A list of queue items
index - default is None type indicating that it needs to grab the first element in the list and convert it, otherwise the specified one
Returns:
time - A float value of the time the element has been in the queue
"""
def parseTime(q, index=None):
    time = 0
    if not index:
        item = q[0].split(',')
        time = float(item[1])
    else:
        item = q[index].split(',')
        time = float(item[1])
    return time


"""This fillQueue method will find our next value from the list of values and append it to the list
Params:
q - A list of queue elements
lastIndex - the last index that the queue was filled with in reference to all elements found in the original file
Returns:
q - A list of all queue items including a new queue element pulled from what is left from the file
"""
def fillQueue(q, lastIndex):
    global qList
    q.append(str(qList[lastIndex]) + ',' + '0')
    return q
        
            

"""This method will run the FIFO algorithm to determine time it takes for us all elements to be processed
Params:
qSize - Our queue size in integer
queue - A list of all our elements in the queue
Returns:
None
"""
def fifo(qSize, queue):
    global totalTime
    global qList
    lastPlaceInQueue = qSize
    totalValues = len(qList) - 1
    cylinder = 0
    count = 0
    while True:
        if (count <= totalValues):
            if ((abs(cylinder - parseQ(queue))) == 0):
                time = 4.2
            else:
                time = ((1 + (abs(cylinder - parseQ(queue)) * .15) + 1) + 4.2)
            queue = addTime(queue, time)
            totalTime += parseTime(queue)
            cylinder = parseQ(queue)
            #print("starting cylinder: %d, ending cylinder %s, Current seek time: %.2f, Time added: %.2f, AccTime: %.2f" % (cylinder, parseQ(queue), time, parseTime(queue), totalTime))
            queue.pop(0)
            if (lastPlaceInQueue <= totalValues):
                queue = fillQueue(queue, lastPlaceInQueue)
                lastPlaceInQueue += 1
            count += 1
        else:
            break

"""This method will find the shortest location of our next element
Params:
queue - A list of queue elements
cylinder - What is the cylinder we are currently at
Returns:
reorder - A list of elements reordered so the next element is the shortest location in relation to our cylinder
"""    
def shortestLocation(queue, cylinder):
    shortest = abs(parseQ(queue) - cylinder)
    reorder = queue
    index = 0
    retainerIndex = 0
    for i in queue:
        if ((abs(cylinder - parseQ(queue, index))) < shortest):
            shortest = abs(cylinder - parseQ(queue, index))
            temp = reorder[0]
            reorder[0] = reorder[index]
            reorder[index] = temp
        index += 1
    return reorder

"""This method starts the SSTF algorithm which sorts and returns our next queue item based on the SSTF procedure
Params:
qSize - A integer value of our maximum queue size
queue - A list of elements in our queue
Returns:
None
"""
def sstf(qSize, queue):
    global totalTime
    global qList
    totalValues = len(qList) - 1
    lastPlaceInQueue = qSize
    cylinder = 0
    count = 0
    while True:
        if (count <= totalValues):
            queue = shortestLocation(queue, cylinder)
            if ((abs(cylinder - parseQ(queue))) == 0):
                time = 4.2
            else:
                time = ((1 + (abs(cylinder - parseQ(queue)) * .15) + 1) + 4.2)
            queue = addTime(queue, time)
            totalTime += parseTime(queue)
            #print("starting cylinder: %d, Current seek time: %.2f, Time added: %.2f, AccTime: %.2f" % (cylinder, time, parseTime(queue), totalTime))
            cylinder = parseQ(queue)
            queue.pop(0)
            if (lastPlaceInQueue <= totalValues):
                queue = fillQueue(queue, lastPlaceInQueue)
                lastPlaceInQueue += 1
            count += 1
        else:
            break
         
"""This method finds the next element in line for our CSCAN method and returns the index of it
Params:
queue - A list of all queue elements
cylinder - Our current cylinder value
Returns:
index - The index of the next cylinder determined by the CSCAN algorithm
"""
def cscanLocation(queue, cylinder):
    arrOfHighValues = []
    arrOfLowValues = []
    returnQ = []
    index = 0
    count = 0
    for i in queue:
        if (parseQ(queue, count) >= cylinder):
            arrOfHighValues.append(i)
        elif (parseQ(queue, count) < cylinder):
            arrOfLowValues.append(i)
        count += 1
    if (len(arrOfHighValues) > 0):
        returnQ = sortCscan(arrOfHighValues)
        index = queue.index(returnQ[0])
    elif (len(arrOfLowValues) > 0):
        returnQ = sortCscan(arrOfLowValues)
        index = queue.index(returnQ[0])
    return index

"""This method is used to scan through our arrays in cscanLoaction to find the next closest element
Params:
array - An array of elements from our queue
Returns:
array - An array of elements with the nearest cylinder location in index 0
"""
def sortCscan(array):
    highI = 0
    ret = None
    for x in array:
        if (parseQ(array, highI) <= parseQ(array)):
            temp = array[0]
            array[0] = array[highI]
            array[highI] = temp
        highI += 1
    return array

"""This method completes the computation of our CSCAN algorithm
Params:
qSize - The maximum size our our queue
queue - A list of elements in our queue
Returns:
None
"""
def cscan(qSize, queue):
    global totalTime
    global qList
    totalValues = len(qList) - 1
    lastPlaceInQueue = qSize
    cylinder = 0
    count = 0
    queue = shortestLocation(queue, cylinder)
    index = 0
    while True:
        if (count <= totalValues):
            if ((abs(cylinder - parseQ(queue, index))) == 0):
                time = 4.2
            else:
                time = ((1 + (abs(cylinder - parseQ(queue, index)) * .15) + 1) + 4.2)
            queue = addTime(queue, time)
            totalTime += parseTime(queue, index)
            #print("starting cylinder: %d, Current seek time: %.2f, Time added: %.2f, AccTime: %.2f" % (cylinder, time, parseTime(queue), totalTime))
            cylinder = parseQ(queue, index)
            queue.pop(index)
            if (lastPlaceInQueue <= totalValues):
                queue = fillQueue(queue, lastPlaceInQueue)
                lastPlaceInQueue += 1
            index = cscanLocation(queue, cylinder)
            count += 1
        else:
            break



#Initializes our program
main()


