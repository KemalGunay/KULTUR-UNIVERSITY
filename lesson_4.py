###############
# LIST
###############

x = ["kemal", "eren", "kuzey", "halil"]
x

print(x)

# List are stored multiple items
# List items are ordered, changeable, and allow duplicate
# list items are indexed, first item index is 0

# I want to call eren
print(x[1])
print(x[3])


y = ["kemal", "eren", "kuzey", "halil", "kemal"]
print(y)


len(y)



# List items can be of any data type
list1 = ["kemal", "eren", "kuzey", "halil"] # str
list2 = [1, 2, 3, 4, 5] # int
list3 = [True, False, True] # boolean

# what type is list3
type(list3)


# list() constructor
list4 = list(("kemal", "eren", "kuzey", "halil"))
print(list4)


# negative indexing
list1 = ["kemal", "eren", "kuzey", "halil"]
list1[-1]

list5 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
print(list5[2:5])
# the search will start at index 2 (included), and end at index 5 (excluded)
# index start with 0

list5 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list5[:4]
list5[1:4]
list5[2:]
list5[-3:-1] # negative index

list5 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
if "kuzey" in list5:
    print("yes, 'kuzey' in the list")




################
# Python Collection (Arrays)
###############
# There are four collection data type
# List is collection which is ordered and changeable. Allow dublicates
# Tuple is collection which is ordered and unchangeable. Allow dublicates


list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[0] = "bengisu"
print(list6)

# example
list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[1:2] = ["mustafa", "yusuf"]
print(list6)


list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[1:4] = ["abdurahman"]
print(list6)

# insert() method
list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.insert(2, "abdurahman")
print(list7)


list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.insert(3, "melike")
print(list7)

# append() method: add new items
list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.append("melike")
print(list7)


# extend()
list8 = ["kemal", "eren", "kuzey", "halil"]
list9 = ["banana", "orange"]
list8.extend(list9)
print(list8)




list8 = ["kemal", "eren", "kuzey", "halil"]
mytuple = ("banana", "orange")
list8.extend(mytuple)
print(list8)




list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.remove("kemal")
print(list7)












