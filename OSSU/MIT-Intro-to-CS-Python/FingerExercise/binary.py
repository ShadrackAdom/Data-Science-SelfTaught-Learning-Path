# #Decimal to Binary  Fucnction

# i = 1
# binarray = []
# while i <= 128:
#     binarray.append(i)
#     i += i

# nbinarray = binarray[::-1]
    
# print(nbinarray)


# num_check = 0
# num = 75
# i = 0


# for i in len(nbinarray + 1):
    
# 	if num == 0:
#         print("f")
#     else:
        


        
    
def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return binary

print(decimal_to_binary(75))