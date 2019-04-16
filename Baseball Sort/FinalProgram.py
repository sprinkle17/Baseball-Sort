#Dalton Sprinkle
#CS 222 02
#Final Project
#Due: 5/7/2018
#Turned in: 5/7/2018
#Description: program will take a file and read contents into shell and selection sort, then will diving them into seperate values and correct values to readible format A user search is included to allow the user to search for a date. A menu is provided for ease of access
import time

def selectionSort(alist):
    for fillslot in range (len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

def printList(alist):
    count = 0
    for x in range(len(alist)):
        
        if count % 10 == 0:
            print()
        print("%4s" % alist[x], end = " " +  '\n')
        count += 1
    print('Comparisons are:',count)
    
def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)
        sublistCount = sublistCount // 2
        
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and \
              alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue


def selectionSorted():
    date = []
    minimum = []
    maximum = []
    FullList = []
    condensed = []
    contents = open('Allegany-NY.csv')
    start_time = time.time()
    for line in contents:
        FullList.append(line)
        data2 = line.split(",")                
        date2 = data2[0]
        maximum2 = data2[1]
        minimum2 = data2[2]
        maximum2 = float(maximum2) / 10 *(9/5) + 32
        minimum2 = float(minimum2) / 10 *(9/5) + 32
        date.append(date2)
        minimum.append(minimum2)
        maximum.append(maximum2)
        condensed.append(date2 + ','+ str(maximum2) + ',' + str(minimum2))
    selectionSort(FullList)
    selectionSort(condensed)
    printList(condensed)

    print("--- %s seconds to run Selection Sort ---" % (time.time() - start_time))

    
def shellSorted():
    date = []
    minimum = []
    maximum = []
    FullList = []
    condensed = []
    contents = open('Allegany-NY.csv')
    start_time = time.time()
    for line in contents:
        FullList.append(line)
        data2 = line.split(",")                
        date2 = data2[0]
        maximum2 = data2[1]
        minimum2 = data2[2]
        maximum2 = float(maximum2) / 10 *(9/5) + 32
        minimum2 = float(minimum2) / 10 *(9/5) + 32
        date.append(date2)
        minimum.append(minimum2)
        maximum.append(maximum2)
        condensed.append(date2 + ','+ str(maximum2) + ',' + str(minimum2))
    shellSort(FullList)
    shellSort(condensed)
    printList(condensed)

    print("--- %s seconds to run Shell Sort ---" % (time.time() - start_time))
    
def UserSearch():
    count = 0
    index = 0
    searches = 0
    condensed = []
    contents = open('Allegany-NY.csv')
    for line in contents:
            data2 = line.split(",")                
            date2 = data2[0]
            maximum2 = data2[1]
            minimum2 = data2[2]
            maximum2 = float(maximum2) / 10 *(9/5) + 32
            minimum2 = float(minimum2) / 10 *(9/5) + 32
            condensed.append(date2)
            condensed.append(str(maximum2))
            condensed.append(str(minimum2))
    UserInput = input("Enter date in format 'yyyymmdd' to search minimum and maximum temperatures or enter 'Done':")
    while UserInput != 'Done':
        for i in condensed:
            index = index + 1
            count = count + 1
            if i == UserInput:
                searches = searches + 1
                print('Date:',i, 'Maximum:',condensed[index], 'Minimum:',condensed[index+1])
                print("Average Comparisons(all searches):", count/searches)
                UserInput = input("Enter new date or enter 'Done':")
        index = 0
                
    
def main():
    message = " (Please give program time to run)\n"
    message += " Press 1 for SelectionSort\n"
    message += " Press 2 for Shell Sort\n"
    message += " Press 3 for User Search\n"
    message += " Press 4 to exit\n"
    print(message)
    userOption = int(input(" Enter Option:"))
    while userOption != 4:
        if userOption == 1:
            selectionSorted()
            print(message)
            userOption = int(input(" Enter Option:"))
        elif userOption == 2:
            shellSorted()
            print(message)
            userOption = int(input(" Enter Option:"))
        elif userOption == 3:
            UserSearch()
            print(message)
            userOption = int(input(" Enter Option:"))
    if userOption == 4:
        print('End of program')
main()
