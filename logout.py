name = input("Enter student name: ")

marks1 = float(input("Enter marks in Python: "))
marks2 = float(input("Enter marks in Java: "))
marks3 = float(input("Enter marks in Database: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 85:
    print("Grade: Z"):
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
