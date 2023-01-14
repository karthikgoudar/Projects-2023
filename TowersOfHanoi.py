'''

    Author  : Karthik Goudar
    Date    : 14 JAN, 2023


    Problem:   TOWERS OF HANOI

    Towers of Hanoi is a mathematical puzzle which can be solved by using Recursion.
    It consists of 3 rods(towers), and a number of discs of different sizes which can
    slide onto any rod.
    Initially, all the disks are stacked in decreasing value of diameter i.e.,
    the smallest disk is placed on the top and they are on rod A(start).
    The objective of the puzzle is to move the entire stack to another rod C (here considered stop),
     obeying the following simple rules:

    * Only one disk can be moved at a time.
    * Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e.
      a disk can only be moved if it is the uppermost disk on a stack.
    * No disk may be placed on top of a smaller disk

    Algorithm:

    * move the top n - 1 disks from A(start) to auxiliary tower b(aux)
    * move the nth disk from A(start) to Destination tower C(end)
    * move the n - 1 disks from Auxiliary tower B(aux) to Destination tower C(end)
    * Transferring the top n - 1 disks from A to B tower can again be thought of as a fresh problem
       and can be solved in the same manner. Once we solve Towers of Hanoi with three disks, we can solve it
       with any number of disks with the above algorithm


'''


def TOH(numbers: int, start: str, aux: str, end: str) -> str:
    if numbers == 1:
        print("Move disc 1 from rod {} to rod {} ".format(start, end))
        return

    TOH(numbers - 1, start, end, aux)
    print("Move disc {} from rod {} to rod {} ".format(numbers, start, end))

    TOH(numbers - 1, aux, start, end)


aim = Toh(3, "A", "B", "C")

print(aim)
