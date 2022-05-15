#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The numbers caculator


def main():
    # this program shows the sum of all numbers from 0 to number
    counter = 0
    sum = 0
    number_counter = 1

    # input
    number = input("Enter number to add too (integer): ")

    # process & output
    try:
        number_int = int(number)
        for counter in range(number_int):
            added_number = input("Enter number {0} (integer): ".format(number_counter))
            added_number_string = int(added_number)

            if added_number_string < 0:
                continue

            sum = sum + added_number_string
            counter = counter + 1
            number_counter = number_counter + 1
        print("The sum of all numbers is  {0}".format(sum))

    except Exception:
        print("Not a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
