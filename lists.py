# list = ["bike", "cricketKit", "travelBag", 2, "drawers", "rail", "suitcase"]
#
# print(list)
#
# # length of list
# print(list.__len__())
#
# #  item in a list
# print(list[6])
# print(list[2])
# print(list[0])
#
# # add an item in a list
# list.append("bed")
# print(list)
# list.append("bike")
# # remove item
# list.remove("rail")
# print(list)
# # delete by position
# list.__delitem__(2)
# print(list)
# # count similar item
# print(list.count("bike"))

# max and min value in list
myNumbers = [3,4,7,1]
# max_value= max(myNumbers)
# print(max_value)
# min_value=min(myNumbers)
# print(min_value)

greatest = 0
for each in myNumbers:
    if each > greatest:
        greatest = each

print("greatest number is", greatest)

# clear the whole list
myNumbers.clear()
print(myNumbers)

# Assignment : use as if statement and a for loop to find the smallest number in a list 