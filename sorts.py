class MySort:
	"""Class that sorts a list of numbers from lowest to highest."""

	def __init__(self):
		"""Constructor"""
		pass

	def __swap(self, list, x, y):
		temp = list[x]
		list[x] = list[y]
		list[y] = temp

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
