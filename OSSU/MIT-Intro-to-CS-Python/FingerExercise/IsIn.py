first_string = input("Enter your first string: ")
second_string = input("Enter your second string: ")

def IsIn(stringone, stringtwo):
    if stringone in stringtwo:
        return True 
    else:
        return False

print(IsIn(first_string, second_string))



def isIn2(string1, string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False

print(isIn2(first_string, second_string))
