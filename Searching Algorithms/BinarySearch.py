'''

Binary Search

Author : Karthik Goudar
Date   : 3 Feb, 2023


Simple Binary Search program usng python

'''



def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = [1, 3, 4, 5, 6, 7, 8, 9]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
