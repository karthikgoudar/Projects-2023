'''
Author : Karthik Goudar
Date   : 2 Feb 2023


Simple Merge Sort Algorithm

Merge sort is a divide-and-conquer algorithm that works by dividing the unsorted list into n sub-lists,
each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.


The unsorted list is divided into n sub-lists, each containing one element. The sub-lists are then merged to produce new sorted sub-lists.
This process continues until there is only one sub-list remaining, which is the sorted list.
'''



def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Sorted array is:", mergeSort(arr))
