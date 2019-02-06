
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
