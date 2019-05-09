"""
===================   TASK 3  ====================
* Name: Insertion Sort
*
* Write a function that will implement insertion sort
* algorithm. Generate list of 1000 random integer
* numbers and sort the list using your function.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
import random
def funk(lnum):
    a = []
    while len(lnum) >= 1:
        minimum = lnum[0]
        for el in lnum:
            if el < minimum:
                minimum = el


        a.append(minimum)
        lnum.remove(minimum)

    return a


def main():
    # Test your function here
    lnum = []
    for i in range(0,1000):
        lnum.append(random.randint(0,1000))
    res = funk(lnum)
    print(res)
    pass

if __name__ == "__main__":
    main()
