__author__ = 'seancheong'

from Sort.BubbleSort import BubbleSort
from Sort.SelectionSort import SelectionSort

UNSORTED_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20, 33, 21, 56, 99, 1, 15, 67, 18, 81, 45, 66]
bubble_list = list(UNSORTED_LIST)
selection_list = list(UNSORTED_LIST)

BubbleSort(bubble_list).sort()
SelectionSort(selection_list).sort()