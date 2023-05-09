# Part C: Finding the right amount to save away

# Define variables
total_cost = float(input("Enter the cost of your dream home: "))
annual_salary = float(input("Enter annual_salary:"))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
annual_return = 0.04
months = 36

# Define function to calculate savings after a certain number of months
def savings_after_months(portion_saved, annual_salary):
    current_savings = 0
    monthly_salary = annual_salary / 12
    for month in range(1, months + 1):
        current_savings += current_savings * annual_return / 12 + portion_saved * monthly_salary
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    return current_savings

# Use bisection search to find the optimal portion_saved
epsilon = 100
low = 0
high = 10000
steps = 0

while abs(down_payment - savings_after_months(high / 10000, annual_salary)) >= epsilon:
    steps += 1
    if down_payment > savings_after_months(high / 10000, annual_salary):
        low = high
    else:
        high = low + high
        low = high - low
        high = high - low
optimal_portion_saved = high / 10000

# Print results
print("Best savings rate:", optimal_portion_saved)
print("Steps in bisection search:", steps)
