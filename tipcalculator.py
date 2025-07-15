print("Welcome to tip calculator")
bill=float(input("what was the total bill?= $"))
tip=int(input("How much tip would you like to give? 10%, 12%, or 15%?"))
people=int(input("How many people want to split bill"))
total_tip=bill*tip/100
total_bill=total_tip+bill
bill_per_person=(total_bill/people)
print(bill_per_person )
