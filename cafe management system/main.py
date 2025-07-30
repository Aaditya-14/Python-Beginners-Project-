menus = {
    "pizza": 230,
    "momo": 110,
    "Burger": 150,
    "Chicken Wings": 220,
    "Biryani": 300,
    "Naam": 120,
}

def Print_menu():
    print("..............MENU.................")
    for item, price in menus.items(): 
        print(f"{item}: Rs {price}")
    print("..................................")


def order_main():
    price = 0
    while True:
        take_order = input("Choose what you want to eat from this menu: ")
        if take_order in menus:
            price += menus[take_order]
            print(f"The total price of your order is Rs {price}")
        else:
            print("The item you chose is not in the menu. Please choose again!")
            
        more=input("Do you want to order more item [Y/N]").lower()
        if more!="y":
            break
        
    print(f"the total price of your order is {price} ")

Print_menu()
order_main()