import time

import numpy as np

n = int(input('Enter array dimensions: '))
m = int(input('Enter array dimensions: '))

array = np.random.randint(0, 1000, size=(n, m))     # create matrix NxM

print('2D array: ', array, '\n')
array_one = array.copy().ravel()      # convert to 1d array
# print('1D array', array_one, '\n')


# selection sort
def selection_sort(array_one):
    start = time.time()
    for i in range(0, len(array_one) - 1):
        min_index = i   # current minimum
        for j in range(i+1, len(array_one)):
            if array_one[j] < array_one[min_index]:  # if the condition satisfied then we have new minimum
                min_index = j  # save new minimum index
        if min_index != i:
            array_one[min_index], array_one[i] = array_one[i], array_one[min_index]  # initiate the swap
    end = time.time()
    result = end - start
    print('selection_sort took', result, 'seconds')
    return array_one


selection_sort(array_one)

array_one = array_one.reshape(n, m)  # convert array back to 2D

print('Sorted 2D', array_one)
# print('\nUnsorted array', array)

array_one = array.copy().ravel()

def quick_sort(array_one):
    start = time.time()
    length = len(array_one)
    if length <= 1:
        return array_one
    else:
        pivot = array_one.pop()


    end = time.time()
    result = end - start
    print('quick_sort took', result, 'seconds')
    return array_one