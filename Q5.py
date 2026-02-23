#input
subtotal = float(input("Enter total bill: ₹"))
people = int(input("Enter number of people: "))
tax_percentage = float(input("Enter tax percentage: "))
tip_percentage = float(input("Enter tip percentage: "))
#Calculations
tax_amount = subtotal * (tax_percentage / 100)
after_tax = subtotal + tax_amount
tip_amount = after_tax * (tip_percentage / 100)
total_amount = after_tax + tip_amount
#Results
print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
print(f"Amount after tax: ₹{after_tax:.2f}")
print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
print(f"per person: ₹{total_amount / people:.2f}")
print(f"Total Amount: ₹{total_amount:.2f}")
