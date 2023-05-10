#Newton-Rashpson for square root 
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k =24.0
guess = k/2.0
steps = 0

while abs(guess*guess - k) >= epsilon:
    steps+=1
    guess = guess -(((guess ** 2)- k )/ (2* guess))
    
print("Square root of", k, "is about ", guess)
print("took about", steps, "steps")