print("==============================")
print("      STUDENT REPORT CARD     ")
print("==============================")

name = input("Student: ")

x = float(input("Math: "))
if x < 0 or x > 100:
    print("error the grade will be at 0 to 100!")
    exit()

y = float(input("Python: "))
if y < 0 or y > 100:
    print("error the grade will be at 0 to 100!")
    exit()

z = float(input("Physics: "))
if z < 0 or z > 100:
    print("error the grade will be at 0 to 100!")
    exit()



print("------------------------------")

avg = (x + y + z ) / 3
avg = round(avg, 2)
print("Average:", avg)

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else:
    grade = "F"

print("Letter grade: ", grade)
gpa = round(avg / 25, 2)
print("GPA:", gpa)

if (x > 70 and y > 70 and z > 70 and avg >= 90):
    print("Scholarship: 52000")
else:
    print("You don't have scholarship")



print("==============================")