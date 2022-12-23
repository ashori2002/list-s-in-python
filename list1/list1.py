# list

myList = ["mohammad", "ashori", 2002, 1.78, "iran"]

print(myList[1])

# Python's append() function inserts a single element into an existing list.
# The element will be added to the end of the old list rather than being returned to a new list.
# Adds its argument as a single element to the end of a list.
myList.append("world")
print(myList)

#The insert() method inserts the specified value at the specified position.
myList.insert(2, "world")
print(myList)

#The del keyword is used to delete objects.
# In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
del myList[1]
print(myList)

#
myList.pop()#Removes the end of a list
myList.pop(0)#removes with index
print(myList)
