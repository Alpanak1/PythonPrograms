user_type=input(("Enter user type,admin,manager,guest \n"))
user_type =user_type.lower()
match user_type:
    case "admin":
        print("Execute admin")
    case "manager":
        print("Execute manager")
