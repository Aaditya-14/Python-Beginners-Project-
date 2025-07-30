
students = {}         
courses = {}          
results = {}          



def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    if student_id in students:
        print("Student already exists.")
    else:
        students[student_id] = {"name": name, "courses": []}
        print("Student added successfully.")

def add_course():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    if course_id in courses:
        print("Course already exists.")
    else:
        courses[course_id] = {"name": name, "credits": credits}
        print("Course added successfully.")

def enroll_student():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    if student_id in students and course_id in courses:
        if course_id not in students[student_id]["courses"]:
            students[student_id]["courses"].append(course_id)
            print("Student enrolled successfully.")
        else:
            print("Student already enrolled in this course.")
    else:
        print("Invalid student or course ID.")

def record_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    if student_id in students and course_id in students[student_id]["courses"]:
        marks = float(input("Enter marks: "))
        results[(student_id, course_id)] = marks
        print("Marks recorded successfully.")
    else:
        print("Student not enrolled in the course.")

def display_report():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print(f"\nReport for {students[student_id]['name']}")
        print("Course\t\tMarks")
        for course_id in students[student_id]["courses"]:
            course_name = courses[course_id]["name"]
            marks = results.get((student_id, course_id), "Not Recorded")
            print(f"{course_name}\t{marks}")
    else:
        print("Student not found.")



def main():
    while True:
        print("\n--- College Management System ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Record Marks")
        print("5. Display Student Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            enroll_student()
        elif choice == "4":
            record_marks()
        elif choice == "5":
            display_report()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Step 4: Run the Program
main()
