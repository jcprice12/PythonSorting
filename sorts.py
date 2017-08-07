class MySort:
	"""Class that sorts a list of numbers from lowest to highest."""

	def __init__(self):
		"""Constructor"""
		pass

	def printMyList(self, myList):
		"""Print a list given"""
		for i in range(len(myList)):
			if i != (len(myList) - 1):
				print((str(myList[i]) + ", "), end='')
			else:
				print(str(myList[i]))

	def bubbleSort(self, myList):
		"""Bubble Sort implementation."""
		newList = list(myList)
		swapped = True
		while swapped:
			swapped = False
			for i in range(1, len(newList)):
				if newList[i] < newList[i-1]:
					temp = newList[i-1]
					newList[i-1] = newList[i]
					newList[i] = temp
					swapped = True
		return newList


