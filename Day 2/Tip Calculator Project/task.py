print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#print("Each Person Should Pay :"+str(((bill*(tip/100))+bill)/people))    #this code can be simplified as written below using variables , "See below code"
bill_with_tip=(bill*(tip/100))+bill
bill_after_split=bill_with_tip/people
print("Each Person Should Pay :$"+str(bill_after_split))



