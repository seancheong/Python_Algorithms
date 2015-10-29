# Python_Algorithms

As the title says, this repository is all about Algorithms that are implemented in Python.

1. Buble sort algorithm:

It's a simple sorting algorithm that repeatedly steps through the list to be sorted, 
compares each pair of adjacent items and swaps them if they are in the wrong order. 
The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 
The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list. 

Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. 
It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly in position.


2. Selection sort algorithm:

Basically, it will divide the input list into two parts: 
the sublist of items already sorted, which is built up from left to right at the front (left) of the list, 
and the sublist of items remaining to be sorted that occupy the rest of the list. 

Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, 
exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), 
and moving the sublist boundaries one element to the right.
