#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 10, 2021
# Generates random numbers and find their average

import random


def random_number_grid(rows, columns, sums):
    # Function that finds the average of the random number grid
    total_sum = sum(sums)
    average = total_sum / (rows * columns)
    return average


def main():
    # Function for input and output
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
                    random_number = random.randint(1, 50)
                    temp_list.append(random_number)
                    print("{0} ".format(random_number), end="")
                print("")
                sum_row = sum(temp_list)
                sums.append(sum_row)
                rows_and_columns.append(temp_list)
            final_average = random_number_grid(rows, columns, sums)
            
            print("The average of these numbers is: {:.2f}".format
                  (final_average))
        except Exception:
            print("{} is not an integer".format(user_columns))
    except Exception:
        print("{} is not an integer".format(user_rows))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
