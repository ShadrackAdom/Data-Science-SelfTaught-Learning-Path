import string



def this(alpha):
	for a in range(len(alpha)):
		if type(alpha[a]) != type(alpha[12]):
			continue
		if alpha[a] > alpha[12]:
			alpha[a] = 0
		else:
			alpha[a] = 1
	return alpha
           
alpha = list(string.ascii_lowercase)
# if alpha[12] > alpha[1]:
# 	# print(alpha[1])

this(alpha)

my_array = [1, 2, '3', 4, '5']

# for i in range(len(my_array)-1):
#     if type(my_array[i]) != type(my_array[i+1]):
#         continue  # Skip comparison if types are different
#     if my_array[i] > my_array[i+1]:
#         print(f"{my_array[i]} is greater than {my_array[i+1]}")
#     elif my_array[i] < my_array[i+1]:
#         print(f"{my_array[i]} is less than {my_array[i+1]}")
#     else:
#         print(f"{my_array[i]} is equal to {my_array[i+1]}")
