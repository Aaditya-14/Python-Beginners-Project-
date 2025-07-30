import random

name=input("Enter your name: ").strip().title()

while True:
    try:
        age=int(input("Enter your age :"))
        break
    except ValueError:
        print("Enter valid varaibles: ")


country=input("Which country are you living: ").strip().title()
city=input("Tell the name of city: ").strip().title()


lists=[
    f"My name is {name}. I am {age} years old. I live in {country}.the capital city of my country is{city} "
    f"I am {name}. i have been to {age} country.the best country i  have visit is {country}. the best city i have been is{city} "
    f"He is {name}. He is {age} years old. He live in {country}. The best city of my country is{city} "]

choice=random.choice(lists)
print(choice)