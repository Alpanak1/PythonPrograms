#Match Statment
browser_name=input("Enter name of browser \n")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name=="firefox":
            print("Execute firefox browser code")
    case "chrome":
        print("Execute firefox browser code")
    case "safari":
        print("Execute firefox browser code")