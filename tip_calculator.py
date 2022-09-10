# This is a Tip calculator Proram

print("Welcome to Tip Calculator!")
bill_amt = float(input("What's the Total Bill?\n"))
no_of_ppl = int(input("How many people to split the Bill?\n"))
tip_percent = int(input("What percentage tip would you like to give? 10 , 12 or 15?\n"))

if tip_percent == 10 or tip_percent == 12 or tip_percent == 15:
    total = ((tip_percent/100 * bill_amt) + bill_amt) / no_of_ppl
    print("Each person should pay" , total)
else:
    print("Invalid Input!!")