print("Welcome to Bill Calculator\n")

try:
    total_bill = float(input("What was the total bill?\n$"))
    tip = int(input("What percentage tip would you like to give?\n"))
    no_of_people = int(input("How many people to split the bill?\n"))

except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

tip_percentage = tip / 100
total_amount = total_bill + (total_bill * tip_percentage)
bill_per_person = total_amount / no_of_people
final_amount = round(bill_per_person, 2)
print(f"\nEach person should pay: ${final_amount}\n")