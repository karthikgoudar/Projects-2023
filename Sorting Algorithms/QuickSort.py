'''
Author : Karthik Goudar
Date   : 1 Feb, 2023


Simple Quick Sort Algorithm

Quick sort is a divide-and-conquer algorithm that works by selecting a "pivot" element
from the array and partitioning the other elements into two sub-arrays,
according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.


the pivot element is selected and used to partition the array into two sub-arrays.
 The sub-arrays are then sorted recursively using the same process.
  This process continues until the entire array is sorted in ascending order.

'''



def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
n = len(arr)
print("Sorted array is:", quickSort(arr, 0, n-1))
