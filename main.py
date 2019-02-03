import sys
from sorts import MySort

fileName = sys.argv[1]
fileObject = open(fileName, "r")

myList = []
for line in fileObject:
	myList.append(int(line))
	
fileObject.close()

mySort = MySort()

print("List before sorting: ")
mySort.printMyList(myList)

mySort.bubbleSort(myList)

print("List after sorting: ")
mySort.printMyList(myList)