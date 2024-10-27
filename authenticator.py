name=input("enter your name")
email=input("enter your email")
password=input("enter your password")
if name =="":
    print("name cannot be empty")
else:
    if "@" not in email:
        print("invalid email")
    else:
        if len(password)<8:
            print("password must be at least 8 characters")
        else:
            print("registered")