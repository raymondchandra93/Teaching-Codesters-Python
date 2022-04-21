""" List """
"""
# Create list
# 0 - apple, 1 - banana, 2 - cherry
thislist = ["apple", "banana", "cherry"]

# Access List
print(thislist[1])          # 2nd item
print(thislist[-1])         # last item
print(thislist)        # 0 - 2

# check item with if
if "pineapple" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("Nope")

# print each item with loop
for x in thislist:
    print(x)

# print the length of the lists
print( len(thislist) )

# Insert list
thislist.append("orange")
thislist.insert(1, "orange")

# Update List
thislist[1] = "blackcurrant"
print(thislist)

# Delete List
thislist.remove("banana")
thislist.pop(2)
thislist.pop()
print(thislist)
"""

""" Tuples """
"""
# Create a tuple
t = (1, 2, 3, 4, 5)

# This also could work without parantheses
#t = 1, 2, 3, 4, 5

# print the whole tupple
print(t)

# print each item with loop
for x in t:
    print(x)

# print 1 item inside tuple
print("Result: " + str(t[1]))

# print the length of the tuples
print("Length: " + str(len(t)) )

# converting to tupples
t1 = tuple([1,2,3])
print(t1)

t2 = tuple("abc")
print(t2)

# swap tuple list
t3 = 1, 2
print(t3)

t4 = t3[1], t3[0]
print(t4)

# trick to change tupple values
x = ("apple", "banana", "cherry")
print(x)

y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
"""

""" Dictionary """

myList = ["a", "b", "c"]
print(myList[0])

# create a dictionary for student
student = {"Name": "Amy", "Age":11, "Grade":6}

# print student's name
print(student["Name"])

# change a value
student["Age"] = 12
print(student["Age"])

# add a new key value
student["GPA"] = 3.7
print(student["GPA"])

# print the whole dictionary
print(student.items())

# print the whole dictionary's keys
print(student.keys())

# print the whole dictionary's values
print(student.values())

# print the whole dictionary using loop
for (k, v) in student.items():
    print(k, v)
print("\n")

# sorting before printing
for (k, v) in sorted(student.items()):
    print(k, v)
print("\n")

# print the length of the dictionary
print("Length: " + str(len(student)) )

# remove all items
student.clear()
print("New Length: " + str(len(student)) )
