# selection sort

def selection_sort(array_one):
    for i in range(0, len(array_one) - 1):
        min_index = i  # current minimum
        for j in range(i + 1, len(array_one)):
            if array_one[j] < array_one[min_index]:  # if the condition satisfied then we have new minimum
                min_index = j  # save new minimum index
        if min_index != i:
            array_one[min_index], array_one[i] = array_one[i], array_one[min_index]  # initiate the swap

    return array_one


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr, left, right):
    if left < right:
        partition_position = partition(arr, left, right)
        quick_sort(arr, left, partition_position - 1)
        quick_sort(arr, partition_position + 1, right)
    return arr


def main():
    import timeit

    import numpy as np
    from numpy import random

    n = int(input('Enter array dimensions: '))
    m = int(input('Enter array dimensions: '))

    array = np.random.randint(0, 1000, size=(n, m))  # create matrix NxM

    print('Not sorted array 2D array: ', array, '\n')
    array_one = array.copy().ravel()  # convert to 1d array
    arr = array.copy().ravel()
    array_two = array.copy().ravel()

    t1 = timeit.timeit(lambda: sorted(array_two), number=1)
    t2 = timeit.timeit(lambda: quick_sort(arr, 0, len(arr) - 1), number=1)
    t3 = timeit.timeit(lambda: selection_sort(array_one), number=1)

    print('Time to sort array with quicksort: seconds', t2)
    print('Time to sort array with selection sort: seconds', t3)
    print('Time to sort array with build in sort function: seconds', t1)

    array_one = array_one.reshape(n, m)  # convert array back to 2D
    arr = arr.reshape(n, m)
    print('Sorted 2D', array_one)
    print('Sorted 2D QS', arr)


if __name__ == '__main__':
    main()
