d = int(input("Enter day you were born: "))
m = int(input("Enter month you were born: "))
y = int(input("Enter year you were born: "))
today_d = 22
today_m = 2
today_y = 2026
my_age = today_y - y
if today_m < m:
    my_age = my_age - 1
elif today_m == m and today_d < d:
    my_age = my_age - 1
total_months = my_age * 12
total_days = my_age * 365
total_hours = total_days * 24
total_mins = total_hours * 60
wait_for_100 = 100 - my_age
print("Years old: ", my_age)
print("Total months: ", total_months)
print("Total days: ", total_days)
print("Total hours: ", total_hours)
print("Total minutes: ", total_mins)
print("Years left until I turn 100: ", wait_for_100)