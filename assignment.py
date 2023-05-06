'''
Problem: Find the minimum number of rotations.

Author : Karthik Goudar
Data   : 5, May 2023 

Time Complexity  :  O(n)
Space Complexity :  O(1)

'''


def min_rotations(s1, s2):
    """Find the minimum number of rotations to obtain s2 from s1.

    Args:
        s1 (str): The initial string
        s2 (str): The target string

    Returns:
        int: The minimum number of rotations required to obtain s2 from s1.
            If s2 cannot be obtained by rotating s1, returns -1.
    """
     
    if len(s1) != len(s2):
        return -1

    s1 = s1 + s1

    # rotating s1 to the left by 1 character at a time

    for i in range(len(s1) - len(s2) + 1):
        rotated = s1[i:i+len(s2)]
        if rotated == s2:
            return i
        
    # If we cannot obtain s2 by rotating s1, return -1
    return -1


# returned result is subtracted by the length of the input string for the final answer

s1 = "orvicej"
s2 = "jorvice"
print(len(s1) - min_rotations(s1, s2)) # Output: 1


s1 = "rvicejo"
s2 = "jorvice"
print(len(s1) - min_rotations(s1, s2)) # Output: 2
