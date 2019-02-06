num = (input("Enter a number: "))
try:
    num = int(num)
    div = num % 2
    if div > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")

except:
    print("This is not an integer")



num = int(input("Enter your number: "))
check = int(input("Enter division number: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
