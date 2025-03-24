def format_name(f_name,l_name):
     return f_name+" "+l_name
f_name=input("Enter your First name\n").title()
l_name=input("Enter your last name\n").title()
full_name=format_name(f_name,l_name)
print(full_name)