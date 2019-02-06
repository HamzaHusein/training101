# Task 1
s= input()
if s=="yes" or s=="YES" or s=="Yes":
    print ("Yes")
else:
    print ("No")

#Task 2
def findLargest(number1, number2, number3):

    if (number1 > number2) and (number1 > number3):
        biggest = number1
    elif (number2 > number1) and (number2 > number3):
        biggest = number2
    else:
        biggest = number3
    print("The biggest number between",number1,",",number2,"and",number3,"is",biggest)
number1 = 100
number2 = 101
number3 = 101
findLargest(number1, number2, number3)


# Task 3
def streetList(a):
    b = [a[0],a[-1]]
    print(b)

a =[5, 10, 15, 20, 25, 30]
streetList(a)


# # Task 4
# num = int(input("Enter a number: "))
# div = num % 2
# if div > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

#Extra Task 4
num = int(input("Enter your number: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")


# #Task 5
tupleLi = (1,2,3,4,5,6,7,8,9,10)
tuple1 = tupleLi [:int(len(tupleLi)/2)]
tuple2 = tupleLi [int(len(tupleLi)/2):]
print (tuple1)
print (tuple2)
