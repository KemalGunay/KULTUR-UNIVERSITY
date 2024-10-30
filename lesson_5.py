
# loop list

mylist = ["kemal", "mehmet", "sıla", "sevi"]

for x in mylist:
    print(x)


# range(), len()
for i in range(len(mylist)):
    print(mylist[i])


# range(), len()
for i in range(1,2):
    print(mylist[i])



# while loop
mylist = ["kemal", "mehmet", "sıla", "sevi"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1



######################
# list comprehension
######################
mylist = ["kemal", "mehmet", "sıla", "ezgi"]
[print(x) for x in mylist]


# example
mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = []

for x in mylist:
    if "a" in x:
        newlist.append(x)

print(newlist)


# list comprehension example
mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = [x for x in mylist if "a" in x]
print(newlist)



# != not kemal
mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = [x for x in mylist if x != "kemal"]
print(newlist)


# iterable - range()
newlist = []
newlist = [x for x in range(9)]
print(newlist)


newlist = []
newlist = [x for x in range(1, 7)]
print(newlist)


# example
newlist = [x for x in range(10) if x < 5]
print(newlist)


mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = [x.upper() for x in mylist]
print(newlist)

mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = [x.capitalize() for x in mylist]
print(newlist)


# Andrew NG scientist

# example
fruits = ["apple", "kiwi", "cheery", "peanut", "banana"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# sort list - alphabetically
fruits = ["apple", "kiwi", "cheery", "peanut", "banana"]
fruits.sort()
print(fruits)


# sort numbers
numbers = [5, 2, 1, 4, 3]
numbers.sort()
print(numbers)


# sort descending
fruits = ["apple", "kiwi", "cheery", "peanut", "banana"]
fruits.sort(reverse = True)
print(fruits)

# sort numbers
numbers = [5, 6, 2, 1, 4, 3]
numbers.sort(reverse = True)
print(numbers)


# case insensitive sort
# sort method is case sensitive
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
thislist.sort()
print(thislist)


# perform a case-insensitive sort of the list
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
thislist.sort(key = str.lower)
print(thislist)


# copy a list
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
mylist = thislist.copy()
print(mylist)

# another way to make a copy is to use list() method
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
mylist = list(thislist)
print(mylist)


# example
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
mylist = thislist[:3]
print(mylist)


# python join list

thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]
list3 = thislist + numbers
print(list3)




# append() method
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]

for x in numbers:
    thislist.append(x)

print(thislist)


# extend()
thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]

thislist.extend(numbers)
print(thislist)








