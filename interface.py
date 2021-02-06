import sys
from bubble import bubble_sort
from selection import selection_sort
from quick import quick_sort,quick_sort_recursion,quick_sort_algorithm,partition
from merge import merge_sort
from insertion import insertion_sort
from timer import run_sorting_algorithm
from random import randint

# creating an empty list
arr = []

choice = int(input("Select which sorting algorithm to use, 1 for bubble, 2 for selection, 3 for quick, 4 for merge, 5 for insertion: "))

def picker(x):
    return {
        1: bubble_sort(arr),
        2: selection_sort(arr),
        3: quick_sort(arr),
        4: merge_sort(arr),
        5: insertion_sort(arr),
    }.get(x, 'none')


if picker(choice) == 'none':
    print("Please enter a nunmber between 1 and 5")
    sys.exit()


# number of elements as input
n = int(input("Length of the array : "))
print("Type the number and then hit enter to begin typing the next element in the arrau until complete")

# iterating till the range
arr = [randint(0, 1000) for i in range(n)]

# for i in range(0, n):
    # ele = int(input())

    # arr.append(ele) # adding the element

# print("You entered: ",arr)
print("Sorted Array: ",picker(choice))

run_sorting_algorithm(algorithm="sorted", array=arr)

