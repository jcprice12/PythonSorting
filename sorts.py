class MySort:
	"""Class that sorts a list of numbers from lowest to highest."""

	def __init__(self):
		"""Constructor"""
		pass

	def __swap(self, list, x, y):
		temp = list[x]
		list[x] = list[y]
		list[y] = temp

	def __mergeSortImpl(self, myList, start, end):
		if (end - start) > 0:
			middle = (start + end) // 2
			self.__mergeSortImpl(myList, start, middle)
			self.__mergeSortImpl(myList, middle + 1, end)
			
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

	def printMyList(self, myList):
		"""Print a given list"""
		for i in range(len(myList)):
			if i != (len(myList) - 1):
				print((str(myList[i]) + ", "), end='')
			else:
				print(str(myList[i]))

	def bubbleSort(self, myList):
		"""Bubble Sort implementation."""
		swapped = True
		while swapped:
			swapped = False
			for i in range(1, len(myList)):
				if myList[i] < myList[i-1]:
					self.__swap(myList, i-1, i)
					swapped = True

	def insertionSort(self, myList):
		"""Insertion Sort Implementation."""
		for i in range(1, len(myList)):
			while i > 0 and myList[i] < myList[i-1]:
				self.__swap(myList, i-1, i)
				i -= 1

	def mergeSort(self, myList):
		"""Merge Sort Implmenentation"""
		self.__mergeSortImpl(myList, 0, len(myList) -1)