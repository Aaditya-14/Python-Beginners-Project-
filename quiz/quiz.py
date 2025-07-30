questions = [
    ["What is the national animal of Nepal?", "Cow", "Dog", "Cat", "Mouse", "1"],
    ["What is the value of 2 + 2?", "3", "4", "5", "6", "2"],
    ["What is the capital city of Nepal?", "Kathmandu", "Bhaktapur", "Lalitpur", "Chitwan", "1"]
]

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    answer = input("Enter your answer  ")
    i=1

    if question[5]==answer:
        print("Correct answer")
    else:
        print("Better luck next time")
        i=i+1


if i==3:
    print("Well done! 🏆 All answers correct.")
else:
    print(f"Khullit 😅 You got out of correct.")
    
        

    

    