__author__ = 'seancheong'

import datetime

class SelectionSort:
    def __init__(self, sort_list):
        print "\nPerforming selection sort on: \n" + str(sort_list)
        self._sort_list = sort_list

    def sort(self):
        list_size = len(self._sort_list)
        before_time = datetime.datetime.now()
        while list_size > 1:
            max_val = 0
            max_pos = 0
            for i in range(list_size):
                if self._sort_list[i] > max_val:
                    max_val = self._sort_list[i]
                    max_pos = i
            self._sort_list[max_pos], self._sort_list[list_size - 1] = self._sort_list[list_size - 1], max_val
            list_size -= 1
        total_time = datetime.datetime.now() - before_time
        print "Total time used: " + total_time.microseconds.__str__() + " micro seconds"
        print self._sort_list