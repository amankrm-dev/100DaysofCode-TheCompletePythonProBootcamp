try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have Entered an invalid number. Use numerical values as age , such as : 20 !")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
