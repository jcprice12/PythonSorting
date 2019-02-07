import sys
import sorts

fileName = sys.argv[1]
fileObject = open(fileName, "r")

myList = []
for line in fileObject:
	myList.append(int(line))
	
fileObject.close()

print("List before sorting: ")
sorts.printMyList(myList)

sorts.mergeSort(myList)

print("List after sorting: ")
sorts.printMyList(myList)