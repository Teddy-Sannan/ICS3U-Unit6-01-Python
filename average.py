#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: December 2019
# This program shows average of 10 random numbers

import random


def main():
    # this function uses an array

    random_numbers = []
    total_number = 0

    # input
    for loop_counter in range(0, 9+1):
        number = random.randint(0, 100+1)
        random_numbers.append(number)

    print("")
    print("The ten marks are:")

    for loop_counter in range(0, 9+1):
        print("{0} ".format(random_numbers[loop_counter]), end="")

    print("")
    print("The average of the ten numbers is")

    for loop_counter in range(0, 9+1):
        total_number = random_numbers[loop_counter] + total_number

    total_number = total_number/10

    print("{0}".format(total_number))


if __name__ == "__main__":
    main()
