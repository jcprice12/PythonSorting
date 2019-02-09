from random import randint

def _swap(list, x, y):
	temp = list[x]
	list[x] = list[y]
	list[y] = temp

def _mergeSortImpl(myList, start, end):
	if (end - start) > 0:
		middle = (start + end) // 2
		_mergeSortImpl(myList, start, middle)
		_mergeSortImpl(myList, middle + 1, end)
		
		combinedList = list()
		i = start
		j = middle + 1
			
		while i <= middle and j <= end:
			if myList[i] < myList[j]:
				combinedList.append(myList[i])
				i += 1
			else :
				combinedList.append(myList[j])
				j += 1

		for k in range(j, end + 1) if i > middle else range(i, middle + 1):
			combinedList.append(myList[k])

		myList[start:end + 1] = combinedList

def _partition(myList, start, end):
	_swap(myList, end, randint(start,end))
	pivot = end
	left = start
	right = end - 1

	while True:
		while left <= right and myList[left] <= myList[pivot]:
			left += 1
		while right >= left and myList[right] >= myList[pivot]:
			right -= 1
		
		if left > right:
			_swap(myList, left, pivot)
			return left
		else:
			_swap(myList, left, right)

def _quickSortImpl(myList, start, end):
	if start < end :
		partitionIndex = _partition(myList, start, end)
		_quickSortImpl(myList, start, partitionIndex - 1)
		_quickSortImpl(myList, partitionIndex + 1, end)

def printMyList(myList):
	for i in range(len(myList)):
		if i != (len(myList) - 1):
			print((str(myList[i]) + ", "), end='')
		else:
			print(str(myList[i]))

def bubbleSort(myList):
	swapped = True
	while swapped:
		swapped = False
		for i in range(1, len(myList)):
			if myList[i] < myList[i-1]:
				_swap(myList, i-1, i)
				swapped = True

def insertionSort(myList):
	for i in range(1, len(myList)):
		while i > 0 and myList[i] < myList[i-1]:
			_swap(myList, i-1, i)
			i -= 1

def mergeSort(myList):
	_mergeSortImpl(myList, 0, len(myList) - 1)

def quickSort(myList):
	_quickSortImpl(myList, 0, len(myList) - 1)