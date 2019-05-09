
"""
===================   TASK 2  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here
def summ(n):
    if not n :
        return 0
    return n[0] + summ(n[1:])





def main():
    # Test your function here
    lisst = [1,2,3,4,5]
    sum_ = summ(lisst)
    print("Sum is: ", sum_)
    pass

if __name__ == "__main__":
    main()
