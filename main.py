print( "==============================")
print("      STUDENT REPORT CARD       ")
print( "==============================")

name = input ("Student: ")
x = float(input("Math: "))
if x < 0 or x > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

y = float(input("Physics: "))
if y < 0 or y > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

z = float(input("Python: "))
if z < 0 or z > 100:
    print("error the grade will be at 0 to 100! ")
    exit()

print ("------------------------------")
avg = (x + y + z) /3
avg = round(avg,2)
print(avg)
gpa = round(avg / 25, 2)
print (gpa)
if avg > 90:
    print("Scholarship: 35000KZT")
else:
    print("you dont have scholarship( ")
print("Scholarship:", avg >= 90)
print("Perfect score:", avg == 100)
print("==============================")