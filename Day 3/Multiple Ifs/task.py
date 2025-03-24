print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0;
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Child tikcets are"+str(bill)+"$")
    elif age <= 18:
        bill=7
        print("Youth tickets are"+str(bill)+"$")
    else:
        bill=12
        print("Adult tickets are"+str(bill)+"$")
    wants_photo=input("Do you want to take phots? Type Y for yes and N for no")
    if wants_photo=='Y':
        # if age <= 12:
        #     bill=5
        #     print("Child tikcets are 5$ and photo price 3$ -----> Total="+str(bill))
        # elif age <= 18:
        #     bill=7
        #     print("Please pay $7 and photo price 3$ -----> Total="+str(bill))
        # else:
        #     bill=15
        #     print("Please pay $12 and photo price 3$ -----> Total="+str(bill))

        bill+=3
    print("Your Final bill is :"+str(bill)+"$")


else:
    print("Sorry you have to grow taller before you can ride.")
