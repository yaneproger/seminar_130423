

def findSmallest(arr):
    smallest = arr[0]
    newArr = []
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    print(smallest, end=",")

    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 9, 4, 0, 8, 7, 2, 1, 6]))
