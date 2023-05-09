
total_cost = 1000000
annual_salary = 150000 #float(input("Enter your starting salary:") )
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
r = 0.04
months = 36

def savings(portion_saved):
    monthly_salary = annual_salary/12
    current_savings = 0

    for month in range(months):
        current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)
    
        if month%6 == 0:
            monthly_salary += (monthly_salary * semi_annual_raise)    
    return current_savings

print(savings(0.375))