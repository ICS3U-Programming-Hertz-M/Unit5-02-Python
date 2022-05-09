#!/usr/bin/env python3
#
# Created by: Hertz Antonella
# Created on: May 8, 2022.
# This program asks the user to enter a base & height of a triangle.
# and calculates the area of the triangle.


def calculate_area(base, height):
    # calculate the area of the triangle and display the answer.
    area = (base * height)/2
    print("The area is {:,.1f} cm^2.".format(area))


def main():
    # get  base and height from user
    base_user = input("Enter the base of the triangle (cm): ")
    height_user = input("Enter the height of the triangle (cm): ")
    print("")

    try:
        # convert string into a float.
        base_user = float(base_user)

        try:
            # converts string into float
            height_user = float(height_user)

            # sets a range for both base and height
            if base_user > 0 and height_user > 0:
                # calls function
                calculate_area(base_user, height_user)
            else:
                print("Enter a number higher than zero.")

        # handles error case
        except Exception:
            print("{} is not a valid number.".format(height_user))

    # handles error cases.
    except Exception:
        print("{} is not a valid number.".format(base_user))


if __name__ == "__main__":
    main()
