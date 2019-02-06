maths = int(input("Enter Your Mathematics Marks"))
english = int(input("Enter Your English Marks"))
kiswahili = int(input("Enter Your Kiswahili Marks"))
geography = int(input("Enter Your Geography Marks"))
biology = int(input("Enter Your Biology Marks"))
chemistry = int(input("Enter Your Chemistry Marks"))
physics = int(input("Enter Your Physics Marks"))

a,b,c,d,e,f,g = maths, english, kiswahili, geography, biology, chemistry, physics

total = a+b+c+d+e+f+g

average = total/7

if average >= 80:
    print("Grade A")
elif average >=70 and average <80:
    print("Grade B")
elif average >=60 and average <70:
    print("Grade C")
elif average >=50 and average <60:
    print("Grade D")
else:
    print("Fail")

print(total

# Nested if
