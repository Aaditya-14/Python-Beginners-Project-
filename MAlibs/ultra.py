import random

# Input with basic validation
name = input("Enter your name: ").strip().title()
while True:
    age = input("Enter your age: ").strip()
    if age.isdigit():
        break
    print("Please enter a valid number for age.")

country = input("Which country are you living in? ").strip().title()
city = input("Tell the name of your city: ").strip().title()

# Sentence templates
sentences = [
    f"My name is {name}. I am {age} years old and I live in {country}. The capital city I love the most is {city}.",
    f"Hi, I'm {name}. I have visited {age} countries in my life. Among them, {country} was the best, and {city} was the most amazing city.",
    f"This is {name}, aged {age}, from {country}. If you ever visit, don't miss out on the beauty of {city}.",
    f"{name} is a {age}-year-old resident of {country}. According to them, {city} is the most vibrant city.",
    f"Allow me to introduce myself—{name}, currently {age} years old, enjoying life in {country}, especially in {city}.",
    f"People call me {name}. I'm {age} years old. I reside in {country}, and trust me, {city} is a must-visit!"
]

# Randomly choose and print a sentence
print("\n--- Your Story ---")
print(random.choice(sentences))
