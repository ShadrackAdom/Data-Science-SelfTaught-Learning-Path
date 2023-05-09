annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
months = 0
semi_annual_raise = float(input("Enter the semi-annual_raise as decimal: "))


while current_savings < down_payment:
    current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)
    
    if months%6 == 0:
        monthly_salary += (monthly_salary * semi_annual_raise)
    months += 1

print("Number of months:", months)
