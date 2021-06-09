#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 8, 2021
# Generates random numbers and find they're average

import random


def main():
    rows_and_columns = []
    sums = []
    user_rows = (input("Enter your amount of rows: "))
    user_columns = (input("Enter your amount of columns: "))

    try:
        rows = int(user_rows)
        try:
            columns = int(user_columns)
            for loop_counter_rows in range(0, rows):
                temp_list = []
                for loop_counter_columns in range(0, columns):
                    a_random_number = random.randint(1, 50)
                    temp_list.append(a_random_number)
                    print("{0} ".format(a_random_number), end="")

                print("")
                sum_row = sum(temp_list)
                sums.append(sum_row)
                rows_and_columns.append(temp_list)
            total_sum = sum(sums)
            average = total_sum / (rows * columns)
            print("The sum of these numbers is: {}".format(total_sum))
            print("The average of these numbers is: {:.2f}".format(average))
        except Exception:
            print("{} is not an integer".format(user_columns))
    except Exception:
        print("{} is not an integer".format(user_rows))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
