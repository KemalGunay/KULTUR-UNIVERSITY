# text data - string
# numeric types - integer, float
# squence types: list, tuples, range
# mapping type: dict
# boolen type: true or false


# Data Type
x = 5
print(type(x))


# string

x = "hello class" # str
x = 5 # int
x = 1.4 # float


list1 = ["banan", "apple", "cheery"]
list1

x = range(5) # range

dict = {"name": "john", "age": 18} # dictionary

# boolen is true or false
x = bool(4)
x


z = -34688 # integer
type(z)

# Type conversion
x = 1 # int


a = float(x)
a

y = 2.8 # float
b = int(y)
b


# random number
import random # call random module with import

print(random.randrange(1,10))


# string

# 'kemal' is the same as "kemal"
print("hello")  # same
print('hello') # same


print("it's allright")
print("kemal"'')
print("his dog is called 'Bella'"')
# red line is the error

a = """
eleklkere
relkgerltw 
glwgrewilkrtw
you can write your notes in this way
"""

# string are arrays
x = "kemal is a lecturer"
print(x[1]) # prints e

x = "kemal is a lecturer"
print(x[2]) # prints m

x = "kemal is a lecturer"
print(x[0]) # k

# NOTE: (important) index starts with 0

for x in "kemal":
    print(x)


# len
# get the length of a string
a = "kemal"
len(a)

b = "hello ai"
print(len(b))


txt = "kemal has a dog"
print(txt)


print("dog" in txt)


txt = "kemal has a dog"
if "dog" in txt:
    print("yes, 'dog' is in it")

txt = "kemal has a dog"
print("cat" not in txt)
print("dog" not in txt)


# slicing strings

x = "hello class!"
print(x[0:2])

y = "hello class!"
print(x[:7]) # starts at the beginnig bcz there is no number

z = "hello class!"
print(z[2:])

# negative index

x = "hello class!"
print(x[-5:-2])


# upper case
a = "kemal"
print(a.upper())

# lower case
a = "KEMAL"
print(a.lower())


# strip()

x = " kemal      gunay "
print(x.strip())

# replace(

a = "kemal"
print(a.replace("k", "c"))


# split()
x = "kemal gunay, mert uzuner, eren kocaömer"
print(x.split(","))


x = "kemal gunay - mert uzuner - eren kocaömer"
print(x.split("-"))

# concatenation
a = "qasim"
b = " kazmi"

c = a + b
print(c)

a = "qasim"
b = " kazmi"

c = a + " " + b
print(c)


age = 18
name = "My name is Bengisu, I am" + age
print(name)

age = 18
name = f"My name is Bengisu, I am {age}"
print(name)


price = 60
x = f"car price is {price} turkish lira"
print(x)

price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)


txt = f"the price is {20 + 60} dollars"
print(txt)


txt = "I am a lecturer."kemal" "
print(txt)


txt = "I am a lecturer. \"kemal\" "
print(txt)


# boolean values
# true or false
print( 10 > 9)
print( 10 == 9)
print(10 < 9)


a = 100
b = 20

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# evaluate values
print(bool("hi"))
print(bool(15))

bool("abc")
bool(123)
bool(["appel", "orange"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])


def myFunction():
    return True

print(myFunction())



def myFunction():
    return True

if myFunction():
    print("yes")
else:
    print("no")


x = 100
print(isinstance(x, str))

b = str(x)


type(b)

# operators
# + addition
# - subtraction
# * multiplication
# / division
# +=   x + = 3   x = x + 3

x  =+ 3
x

x = 100
x += 3
x


x = 100
x -= 3
x


x = 100
x *= 3
print(x)


# == equal x == y
# != not equal x !=y
# >= greater than or equal to x >= y
# <= less than or equal to z <= y


x = 3
y = 3
print(x == y)



x = 3
y = 3
print(x != y)


# and operator
print(x < 4 and x < 10)

print(x > 1 and x < 4 and x < 10)

# or operator
x = 3
print(x < 4 or x > 10)


# not operator
x = 3
print(not(x < 5 and x < 10))

x = 5
print(not(x < 5 and x < 10))


# is
x = 3
y = 3
print(x is y)


# is not
x = 3
y = 3
print(x is not y)




