# Global constants
Bc_tax = 0.05
tip = 0.12

# Calculating the tax, tip, and grand total based on the user input
initial_total = float(input("Enter the price of a meal: "))
total_tax = float(initial_total * Bc_tax)
total_tip = float(initial_total * tip)
grand_total = initial_total + total_tax + total_tip

# Print the desired values
print("Total tax is: $" + str(total_tax))
print("Total tip is: $" + str(total_tip))
print("Grand_total is: $" + str(grand_total))