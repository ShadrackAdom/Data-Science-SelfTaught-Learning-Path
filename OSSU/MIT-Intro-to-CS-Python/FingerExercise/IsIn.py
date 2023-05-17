
'''
Write a function isIn that accepts two strings as
arguments and returns True if either string occurs anywhere in the other,
and False otherwise. Hint: you might want to use the built-in str
operation in.
'''
first_string = input("Enter your first string: ")
second_string = input("Enter your second string: ")


def IsIn(stringone, stringtwo):
    if stringone in stringtwo:
        return True 
    else:
        return False

print(IsIn(first_string, second_string))

