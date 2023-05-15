# binary search

def binary_search(array, element, low, high):  # find the element
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == element:
            return mid

        elif array[mid] < element:
            low = mid + 1

        else:
            high = mid - 1
    return -1


def main():
    import numpy as np
    from numpy import random

    array = np.random.randint(0, 5000, size=7)
    element = random.choice(array)

    print(array)
    print(element)
    array = sorted(array)
    print(array)

    result = binary_search(array, element, 0, len(array)-1)

    if result != -1:
        print('Element is in array at index ' + str(result))
    else:
        print('Element is NOT in array')


if __name__ == '__main__':
    main()