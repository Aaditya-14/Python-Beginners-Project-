try:
    a=int(input("Enter first number:"))
    b=int(input("Second number :"))
    print("What do you want to do \n multiply \n add \n Subract \n Divided \n ")
    
    operation=input("Enter what do you want to do ")
    
    match operation:
        case "multiply":
            print(f"the multiplication of {a} and {b} is :{a*b}")
        case "add":
            print(f"the multiplication of {a} and {b} is :{a+b}")
        case "Divided":
            print(f"the multiplication of {a} and {b} is :{a/b}")
        case "Subract":
            print(f"the multiplication of {a} and {b} is :{a-b}")

except Exception as e:
    print("please enter valid value ")
    
    
#this is simple calculator using 