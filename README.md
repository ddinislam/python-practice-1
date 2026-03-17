for me: this code calculates a student's academic performance and scholarship. Student AITU


print( "==============================")
print("      STUDENT REPORT CARD       ")
print( "==============================")

name = input ("Student: ")
x = float(input("Math: "))
if x < 0 or x > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

y = float(input("Python: "))
if y < 0 or y > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

z = float(input("Psychology: "))
if z < 0 or z > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

a = float(input("Basketball: "))
if a < 0 or a > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

b = float(input("Political Science: "))
if b < 0 or b > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

c = float(input("Algorithm: "))
if c < 0 or c > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

d = float(input("Practice: "))
if d < 0 or d > 100:
    print("error the grade will be at 0 to 100! ")
    exit()


print ("------------------------------")
avg = (x + y + z + a + b + c + d) / 7
avg = round(avg,2)
print(avg)
gpa = round(avg / 25, 2)
print (gpa)
if (x > 70 and y > 70 and z > 70 and a > 70 and b > 70 and c > 70 and d > 70):
    print("Scholarship: 52000")
else:
    print("you dont have scholarship( ")
print("==============================")


