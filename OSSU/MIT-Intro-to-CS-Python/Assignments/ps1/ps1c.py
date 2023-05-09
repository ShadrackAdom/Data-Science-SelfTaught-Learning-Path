
# Part C: Finding the right amount to save away

# Define variables
total_cost = 1000000
annual_salary = float(input("Enter your starting salary:") )
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
r = 0.04
months = 36


# Define function to calculate savings after a certain number of months
def savings(portion_saved):
    monthly_salary = annual_salary/12
    current_savings = 0

    for month in range(months):
        current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)
    
        if month%6 == 0:
            monthly_salary += (monthly_salary * semi_annual_raise)    
    return current_savings


#print(savings(0.4411))

# Use bisection search to find the optimal portion_saved

if savings(1) >= down_payment:
    epsilon = 100
    low = 0
    high = 10000
    portion_saved = ((low + high)/2)/10000
    steps = 0

    while abs(savings(portion_saved) - down_payment) >= epsilon:
        #print(f"stating: {savings(portion_saved)}, {down_payment}")
        if savings(portion_saved) > down_payment:
            high = portion_saved*10000
            portion_saved = ((low + high)/2)/10000
            #print(high, portion_saved, savings(portion_saved), down_payment)

        else:
            low = portion_saved*10000
            portion_saved = ((low + high)/2)/10000
            # print("it low so,")
            # print(low, portion_saved, savings(portion_saved), down_payment)
            # print(" ")


        steps+=1

    print("Best saving rate is: ", portion_saved)
    print("steps in bisection search", steps)
    #print(savings(portion_saved))

else:
    print("it is not possible to [pay the down payment in three years")




