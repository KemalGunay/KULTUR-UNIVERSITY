# tuples
mytuple = ("apple", "Kiwi", "cheery", "peanut", "Orange")

# unchangeable
# ordered
# tuples are written with round brackets
# tuple items are indexed, fist index 0, the second index is 1
# allow dublicates

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple)

# tuple length
print(len(mytuple))


# create tuple with one item
thistuple = ("kemal",)
print(type(thistuple))


# tuple items can be any data type
# string, int, float, boolean
tuple1 = (True, False, True) # boolean
tuple2 = (1, 2, 3, 4) # int
tuple3 = ("apple", "apple", "kiwi")

# a tuple can contain different data types
tuplelistem = ("kemal", 99, True, 22, "kedi")
print(tuplelistem)
type(tuplelistem)



# tuple() constructor
mytuple = tuple(("kemal", "mehmet"))
print(mytuple)


# access tuple items
mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[3])

# negative index
mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[-2:])


# range of index
mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[2:5])


# range of index
mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[:3])

# range of index
mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[3:])



# check if item exist
mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
if "apple" in mytuple:
    print("yes, 'apple' is in the list")


# change tuple items
x = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
type(x) # tuplemış

y = list(x)
type(y)

x = tuple(y)
type(x)


print("hi")


# EXAMPLE
x = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
type(x) # tuple

y = list(x)
y[1] = "kemal"
x = tuple(y)
type(x)


# add items with append() method
x = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
y = list(x)
y.append("dragonfood")
x = tuple(y)
x


# add tuple to tuple, you are allowed to add tuples to tuples
# tek değerli tuple
x = ("apple", "orange")
y = ("peanut",)
x += y
print(x)


# remove()
x = ("apple", "kiwi", "cheery", "peanut", "orange")
y = list(x)
y.remove("kiwi")
x = tuple(y)
print(x)
type(x)

# you can delete tuple via del
x = ("apple", "kiwi", "cheery", "peanut", "orange")
del x
print(x)


# unpacking tuple
x = ("apple", "kiwi", "cheery")
(red, green, pink) = x
print(red)
print(green)
print(pink)


# using *
x = ("apple", "kiwi", "cheery", "peanut", "orange")
(red, green, *pink) = x
print(red)
print(green)
print(pink)


# example
x = ("apple", "kiwi", "cheery", "peanut", "orange", "drangon")
(red, *green, pink) = x
print(red)
print(green)
print(pink)



# loops in tuples
mytuple = ("apple", "kiwi", "cheery", "peanut", "orange", "drangon")
for x in mytuple:
    print(x)


# loop through the index numbers
mytuple = ("apple", "kiwi", "cheery", "peanut", "orange", "drangon")
for i in range(len(mytuple)):
    print(mytuple[i])


# example
mytuple = ("apple", "kiwi", "cheery", "peanut", "orange", "drangon")
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1

# diğer dosyada devam ediyor









