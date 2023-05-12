# Write a program that asks the user to enter an integer and prints two integers, root
# and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no
# such pair of integers exists, it should print a message to that effect.


import math



num = int(input("Enter an integer: "))
found = False

#set 0 < power < 6
for pwr in range(1,6):
    #found root with built func math.sqrt
    #root = round(num**(1/pwr))
    root = math.sqrt(num)
    #compare if root**power == num entered
    if root**pwr == num:
        found = True
        #if True print(root, power)
        print(f"root = {root} and power = {pwr}")
        print(f"{root}^{pwr} = {num}")

if not found:
    print("No such pair of integers exists.")

###WHILE LOOP VERSION

# num = int(input("Enter an integer: "))
# found = False
# pwr = 2

# while pwr < 6:
#     root = round(num**(1/pwr))
#     if root**pwr == num:
#         found = True
#         print(f"{root}^{pwr} = {num}")
#     pwr += 1

# if not found:
#     print("No such pair of integers exists.")


