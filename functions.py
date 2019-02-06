# # # function is a bunch of code you create to be used somewhere else
# #
# # # function definition
# # def likhwu(string):
# #     print(string)
# # # calling a function
# # likhwu("Hamza")
# # # reusing the function
# # likhwu(1+1)
#
# igcse = [85, 76, 80, 69,  62, 75]
# # create a function to calculate total marks
# def calculateTotal(marks):
#     sum = 0
#     for i in marks:
#         sum += i
#     return sum
#
# # use that function to calculate marks for igcse
# total = calculateTotal(igcse)
# print(total)
#
# def streetList(a, houseThings):
#     b = [a[0],a[-1]]
#     c = [houseThings[0],houseThings[-1]]
#     print(b, c)
#
#
# houseThings = ["sofa","lights", "cables", "charger", "bat" ]
# a =[5, 10, 15, 20, 25, 30]
# streetList(houseThings,a)

def things(a, b):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print("Both same length")

a= input("Enter word:")
b= input("Enter word:")
things(a, b)


def thingsDef(a='Hamza', b='Husein'):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print("Both same length")

a= input("Enter word:")
b= input("Enter word:")
thingsDef()


