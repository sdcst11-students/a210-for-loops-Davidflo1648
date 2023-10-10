#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
height_width = int(input("Enter a number: "))

if height_width < 1 or height_width > 9:
    print("Invalid input. Please enter an integer value less than 10.")
else:
    for i in range(height_width): 
        print("*"*height_width, end="")
        print()
