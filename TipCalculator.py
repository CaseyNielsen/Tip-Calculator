print("Welcome to the tip calculator!")

bill = float(input("What was your final bill total?\n"))
person = int(input("How many people are paying or splitting the bill?\n"))
tip = int(input("Would you like to tip 10, 15, or 20 percent?\n"))

tip_per = (tip / 100)+1
split_total = (bill/person)*tip_per

print(f"Each person should pay {(round(split_total,2))}.")