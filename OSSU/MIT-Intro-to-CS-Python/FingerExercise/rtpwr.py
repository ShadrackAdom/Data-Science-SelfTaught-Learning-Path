# Write a program that asks the user to enter an integer and prints two integers, root
# and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no
# such pair of integers exists, it should print a message to that effect.

#get integer

import math

num = int(input("Enter an integer: "))
found = False


for pwr in range(1,6):
    #root = round(num**(1/pwr))
    root = math.sqrt(num)
    if root**pwr == num:
        found = True
        print(f"root = {root} and power = {pwr}")
        print(f"{root}^{pwr} = {num}")

if not found:
    print("No such pair of integers exists.")

