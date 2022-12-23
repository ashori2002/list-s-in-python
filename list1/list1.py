# list

myList = ["mohammad", "ashori", 2002, 1.78, "iran"]

print(myList[1])

# Python's append() function inserts a single element into an existing list.
# The element will be added to the end of the old list rather than being returned to a new list.
# Adds its argument as a single element to the end of a list.
myList.append("world")
print(myList)

# The insert() method inserts the specified value at the specified position.
myList.insert(2, "world")
print(myList)

# The del keyword is used to delete objects.
# In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
del myList[1]
print(myList)

# The Python pop() method removes an item at a specified index value from a list.
# This method returns the item you have removed so you know what modification has been made to your list.
# pop() accepts one argument: the index of the item you want to remove.
myList.pop()  # Removes the end of a list
myList.pop(0)  # removes with index
print(myList)

# The remove() method removes the first occurrence of the element with the specified value.
myList.remove(2002)
print(myList)

# ________________________________________________________________________________________

myL = [8, 2, 1, 6, 9]

myL.sort()
print(myL)

myL = ["x", "c", "j", "", "k"]
myL.sort()
print(myL)

# ----------------------------------------------------------------------------------------
myL = [8, 2, 1, 6, 9]
print(sorted(myL))


myL = ["x", "c", "j", "", "k"]
print(sorted(myL))

myL = "ashori2002"
print(sorted(myL))
###########################################################################################

# The reverse() method reverses the sorting order of the elements.
cars = ["BMW", "benz", "volvo", "fiat", "tesla"]
cars.reverse()
print(cars)