print("==============================")
print("      STUDENT REPORT CARD     ")
print("==============================")

name = input("Student: ")

x = float(input("Math: "))
if x < 0 or x > 100:
    print("error the grade will be at 0 to 100!")
    exit()

y = float(input("Physics: "))
if y < 0 or y > 100:
    print("error the grade will be at 0 to 100!")
    exit()

z = float(input("Python: "))
if z < 0 or z > 100:
    print("error the grade will be at 0 to 100!")
    exit()

print("------------------------------")

avg = (x + y + z) / 3
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

print("Letter grade:", grade)

scholarship = (x >= 70 and y >= 70 and z >= 70 and avg >= 90)
print("Scholarship:", scholarship)

grades = [x, y, z]
subjects = ["Math", "Physics", "Python"]

for i in range(len(grades)):
    if grades[i] >= 90:
        print(subjects[i] + ":", "Excellent")
    elif grades[i] >= 75:
        print(subjects[i] + ":", "Good")
    elif grades[i] >= 60:
        print(subjects[i] + ":", "Satisfactory")
    else:
        print(subjects[i] + ":", "Fail")

print("------------------------------")
print("Name uppercase:", name.upper())
print("Name lowercase:", name.lower())
print("Name length:", len(name))
print("Masked name:", name.replace(name[0], "*", 1))
print("==============================")