'''
Author : Karthik Goudar
Date   : 2 Feb 2023


Simple Bubble Sort Algorithm

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements
if they are in the wrong order.

'''



def bubbleSort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array is:", bubbleSort(arr))
