# grade_system.py
# Simple Student Grade System

mark = float(input("Enter your mark (0-100): "))

if mark < 0 or mark > 100:
    print("Invalid mark. Please enter a number between 0 and 100.")

elif mark >= 90:
    grade = "A"
    print(f"Your mark is {mark:g} and your grade is {grade}.")

elif mark >= 80:
    grade = "B"
    print(f"Your mark is {mark:g} and your grade is {grade}.")

elif mark >= 70:
    grade = "C"
    print(f"Your mark is {mark:g} and your grade is {grade}.")

elif mark >= 60:
    grade = "D"
    print(f"Your mark is {mark:g} and your grade is {grade}.")

else:
    grade = "E"
    print(f"Your mark is {mark:g} and your grade is {grade}.")