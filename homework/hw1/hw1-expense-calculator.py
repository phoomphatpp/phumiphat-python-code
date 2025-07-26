"""
Personal Finance Calculator
Student: Phumiphat Chuancharoen
Date: 25/07/2025
Purpose: Calculate monthly budget and savings
"""

monthly_income = float(input("Enter Monthly in THB: "))
rent_cost = float(input("Enter monthly rent/housing in cost: "))
food_budget = int(input("Enter monthly food budget in THB: "))
transportation_cost = float(input("Enter monthly transportation in THB: "))
entertainment_budget  = int(input("Enter monthly enterainmainment budget: "))
emergency_fund_percent = float (input("Enter percentage for emergency fund: "))
investment_percent = float (input("Enter percentage for investing fund: "))



total_fixed_expenses = rent_cost + transportation_cost 
total_varibale_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_varibale_expenses

remaining_fund = monthly_income -  total_expenses
emergencay_fund = monthly_income * (emergency_fund_percent / 100)
investment_fund = monthly_income * (investment_percent / 100)
available_saving = remaining_fund - emergencay_fund - investment_fund
expense_ratio = (total_expenses / monthly_income ) * 100
expense_ratio = round(expense_ratio,2)


print("=== MONTHLY BUDGET REPORT ===")
print("Income:",monthly_income,"THB")
print("Fixed Expenses:",total_fixed_expenses,"THB")
print("Variable Expense:",total_varibale_expenses,"THB")
print("Total Expense:",total_expenses,"THB")
print("Remaining :",remaining_fund,"THB")
print()
print(f"Emergency Fund ({emergency_fund_percent}): {emergencay_fund} THB")
print(f"Emergency Fund ({investment_percent})%: {investment_fund} THB")
print("Available for Savings:",available_saving)
print()
print("=== ANALYSIS ===")
print("Expense Ratio:",expense_ratio,"%")