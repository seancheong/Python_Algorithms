__author__ = 'seancheong'

import datetime

class BubbleSort:
    def  __init__(self, sort_list):
        print "\nPerforming bubble sort on: \n" + str(sort_list)
        self._sort_list = sort_list

    def sort(self):
        list_size = len(self._sort_list)
        exchange = True
        before_time = datetime.datetime.now()

        while list_size > 0 and exchange:
            exchange = False
            for i in range(list_size - 1):
                if self._sort_list[i] > self._sort_list[i+1]:
                    exchange = True
                    self._sort_list[i], self._sort_list[i+1] = self._sort_list[i + 1], self._sort_list[i]
            list_size -= 1
        total_time = datetime.datetime.now() - before_time
        print "Total time used: " + total_time.microseconds.__str__() + " micro seconds"
        print self._sort_list