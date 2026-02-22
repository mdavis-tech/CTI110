# Misti Davis
# 02/22/2026
# P1HW2 - Travel Budget Calculator
# This program calculates a user's remaining travel budget
# after entering planned expenses for gas, accommodation, and food.

"""
Pseudocode (Program Logic)

1. Display program title.
2. Ask user to enter their total travel budget.
3. Ask user to enter their travel destination.
4. Ask user to enter amount they will spend on gas.
5. Ask user to enter amount they will spend on accommodation.
6. Ask user to enter amount they will spend on food.
7. Add gas, accommodation, and food expenses together.
8. Subtract total expenses from total budget.
9. Display destination.
10. Display total budget.
11. Display each expense.
12. Display remaining balance.
"""

# Display program title
print("----- Travel Budget Calculator -----")
print()

# Get user inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? "))
accommodation = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food? "))

# Calculate expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n----- Travel Expenses -----")
print("Destination:", destination)
print("Budget:", budget)
print("Gas:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)