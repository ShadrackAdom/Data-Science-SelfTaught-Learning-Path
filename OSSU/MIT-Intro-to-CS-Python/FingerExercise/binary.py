def decimal_to_binary(n):
    #check if number == 0
    if n == 0:
        return '0'
    

    binary = ''
    while n > 0:
        #divide the number n by 2 and append the remainder (either 0 or 1)
        binary = str(n % 2) + binary
        n //= 2
    
    return binary

#print result
print(decimal_to_binary(75))
