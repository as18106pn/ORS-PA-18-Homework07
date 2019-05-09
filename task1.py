"""
===================   TASK 1   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You can use `rand` module to simulate dice
* rolling.
===================================================
"""
import random
def roll_the_dice():
    n = int(input("How many times should the dice be rolled?"))
    a1 = a2 = a3 = a4 = a5 = a6 = 0
    for i in range(n):
        number = random.randrange(1, 7)
        if number == 1:
            a1 += 1
        if number == 2:
            a2 += 1
        if number == 3:
            a3 += 1
        if number == 4:
            a4 += 1
        if number == 5:
            a5 += 1
        if number == 6:
            a6 += 1


    print("Number of repeat number 1:", a1, "number 2: ", a2, "number 3:", a3, "number 4:", a4, "number 5:", a5,
                  "number 6:", a6)



roll_the_dice()