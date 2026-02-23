#input
age = int(input("Enter Age: "))
day=input("Enter Day of the week: ").strip().capitalize()
no_tickets = int(input("Enter number of tickets: "))
#Calculations
if age < 3:
    price = 0
    category="free"
elif 3 <= age <= 12:
    price = 150
    category="child"
elif 13 <= age <= 59:
    price = 300
    category="adult"
else:
    price = 200
    category="senior"
# Day-based discount
weekend=["Friday", "Saturday", "Sunday"]
discounted_price= 0.20 if day in weekend else 0
discounted_amount = price * discounted_price
final_price_per_ticket = price - discounted_amount
total_cost = final_price_per_ticket * no_tickets
#Results
print(f"\nCategory:{category}")
print(f"Base Price:{price}")
print(f"Discount:{discounted_amount}")
print(f"Price after discount:{final_price_per_ticket}")
print(f"Total Amount for {no_tickets} ticket:{total_cost}")
