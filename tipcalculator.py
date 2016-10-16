#tip calculator

def tipcalc(bill):
    tip = 0.15 * bill
    print("Your tip should be: $" + str(tip))
    
amount = float(raw_input("How much was your total bill? "))
tipcalc(amount)


