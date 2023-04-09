print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
num_people = float(input("How many people to split the bill?"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?")) / 100

bill_with_tip = total_bill + (total_bill * tip)
pay_per_person = round(bill_with_tip / num_people, 1)

print(f"Each person should pay : {str(pay_per_person)}")