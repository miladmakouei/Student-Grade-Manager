
student_names = []
student_grades = []

PASSING_GRADE = 10


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    grade_text = input("Enter grade (0-20): ")

    if not grade_text.isdigit():
        print("Please enter a valid whole number.")
        return

    grade = int(grade_text)

    if grade < 0 or grade > 20:
        print("Grade must be between 0 and 20.")
        return

    student_names.append(name)
    student_grades.append(grade)

    print("Student added successfully.")


def show_students():
    if len(student_names) == 0:
        print("No students recorded yet.")
        return

    print("\n--- Student List ---")

    for index in range(len(student_names)):
        name = student_names[index]
        grade = student_grades[index]

        if grade >= PASSING_GRADE:
            status = "Passed"
        else:
            status = "Failed"

        print(f"{index + 1}. {name} | Grade: {grade} | {status}")


def show_average():
    if len(student_grades) == 0:
        print("No grades available.")
        return

    total = 0

    for grade in student_grades:
        total = total + grade

    average = total / len(student_grades)

    print(f"Average grade: {average:.2f}")


while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add student")
    print("2. Show students")
    print("3. Show average grade")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        show_average()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
