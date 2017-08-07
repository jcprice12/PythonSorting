import sys
from sorts import MySort

fileName = sys.argv[1]
fileObject = open(fileName, "r")

myList = []
for line in fileObject:
	myList.append(int(line))
	
fileObject.close()

mySort = MySort()

print("Unsorted List: ")
mySort.printMyList(myList)

newList = mySort.bubbleSort(myList)
print("\n")
print("Sorted List: ")
mySort.printMyList(newList)


