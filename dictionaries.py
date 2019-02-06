userDetails = {"name":"Hamza Husein", "age":"21", "location": "Nairobi", "team": "teampili" }
print(userDetails)

# dictionary is a store for key value pairs

# retreive name of user

print(userDetails["name"])

# add an item

userDetails["levelofEducation"] ="Diploma"
print(userDetails)
print(userDetails.values())
# typecasting dictionary values to be a list
userDetailslist=list(userDetails.values())
print(userDetailslist)

# Assignment:typecast dictionary keys to be a list
userDetailslist=list(userDetails.keys())
print(userDetailslist)
# completed

# length of dictionary
print(userDetailslist.__len__())

# loop over all dictionary values
for i in userDetails.values():
    print(i)
# loop over both dictionary values and keys
for key, values in userDetails.items():
    print(key +  " "  +  values)
