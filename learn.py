print(" ")
print ("First lesson") # First lesson teaches prints messages with the command 'print' then a  message in a ("_______") or ('_____').


print ("How to code?")
print (';-;')


print(" ")
print("Second lesson") # Second lesson teaches how to use Syntax or what I call it, 'if'  statements.

if 6 < 5:
    print ("6 is greater than 5 stupid ")

# The lesson didn't really touch over 'else' statements, but from my little bit of knowledge of coding, I knew that 'else' statements were used to give a message if the 'if' statement was wrong.

else:
    print ("No, stupid")

print(" ")
print("Thrid lesson") # The third lesson teaches how to use comments with the '#' symbol, which  I have use in the first 2 lessons.

print("# and the key to comments")

print(" ")
print("Forth lesson") # The fourth lesson covers on variables where we need to first assign a  value to them to use it in our code.

x = 5
y = "Raymont"

# The lesson also shows how to print variables. Instead of print with ("_______"), we can just  put in the variable name in (___). 

print(x)
print(y)

print(" ")
print("Fifth lesson")  # The fifth lesson teaches how to use casting to print specific data types.

x = str(7.2) # str means string which is the text of the variable, 7.2 would output as 7.2 and  'apple' would output to apple

y = int(7.2) # int mean integer which is a whole number not a decimal, 7.2 would output as 7  and 'apple' would output as an error due to it not being a number but a text

z = float(7.2) # float means (I guess) floating which means that the output number would be the
# exact number (I think) and not text. So, 7.2 would output as 7.2 and 'apple' would output as an error due to it not being a number but a text

print(x)
print(y)
print(z)

# When code becomes like this I like to play around with the code to potentioally make it better  or break it completely.

X = 4.761 # This varible is to change all the other casting varibles quickly.

x = str(X)
y = int(X)
z = float(X)

print(x)
print(y)
print(z)

print(" ")
print("Sixth lesson") # The sixth lesson talks about how to name variables. It's important to  understand how to properly name variables so errors won't occur.

myname = "Niko" # Works perfectly, all lowercase letters

myName = "Valen" # Works perfectly, first letter of second word is capitalized

MyName = "Person" # Works perfectly, first letter of every word is capitalized

my_name = "Ryan" # Works perfectly, underscores are used to separate words

myname2 = "Acon" # Works perfectly, numbers can be used in anywere in the variable's name  but the start

# my name = "Niko" will cause an error due to there being a space in the variable's name

# my-name = "Valen" will cause an error due to there being a hyphen in the variable's name

# 2myname = "Ruby" will cause an error due to the variable's name starting with a number

# if = Niko will also cause an error due to 'if' being a special word in Python, as well as  'print', 'else', 'for', 'while', 'def', and many more.

# printing this message for fun

print("Naming variables needs to follow these rules: You can use lower case letters, Uppercase letters (they will be treated as a different variable), numbers, and underscores.  You can't use any other symbols or spaces, don't start a variable name with a number and don't you use special words like 'print', 'if', 'else'.")


print(" ")
print("Seventh lesson")  # The seventh lesson teaches how to assign multiple values to variables in.

x, y, z = 'mango', 'watermelon', 'pear' # This prosses is basically assigning a list of variables with a list of values.

print(x)
print(y)
print(z)

# If you want to assign the variables as the anme value you just put '=' everywhere.

x = y = z = 'strawberry'
print(x)
print(y)
print(z)

# If you want to reverse it and get the values from the variables you do something called unpacking.  
fruits = ['mango', 'watermelon', 'pear'] # listing the values into a variable.

x, y, z = fruits # assigning the variables to the valuesin the variable 'fruits'

print(x)
print(y)
print(z)

print(" ")
print("Eighth lesson") # The eighth lesson teaches how to output variables, like text, in 'print' 

x = 'people from the Hackclub community are really helpful!'
print(x)

a = 'People '# Notice there are spaces between the word and the quotation mark, this is to make sure that the words are spaced out when printed.
b = 'from '
c = 'the '
d = 'Hackclub '
e = 'community '
f = 'are '
g = 'really '
h = 'helpful!'
print(a, b, c, d, e, f, g, h) # This is using the ',' symbol to combine the string variables together to make a sentance.

print(a + b + c + d + e + f + g + h) # This can also be done with the '+' symbol.

# With numbers, if you use the '+' symbol, the numbers will be added up instead of being combined.
x = 42
y = 31
print(x + y)

# You can combine 2 variables together even when one is text and one is a number. This is because a number can be a string and a text is already a string.
x = '42'
y = 'Koji'
print(x, y) 

print(" ")
print("Ninth lesson") # The ninth lesson teaches about global variables, where to use them and how they work. (They also use some new words without explaining them, so I had to do some research on them.)

x = 'amazing!' # When not inside a funcion, variables are called global variables. This means that the variables can be accessed from anyware in the code.

def myopinion(): # 'def' is a special word that is used to define the funcion, which in this case is 'myopinion'.

    print('Hackclub is ' + x)

myopinion() # This runs the funcion 'myopinion' in which the code says to prints the message 'Hackclub is amazing!'.

# You can create  local variabes by defining a variable inside of a function.

x = 'amazing!'

def myopinion():
    x = 'supportive!' # since 'x' is defined as 'supportive!' inside the function, it is considered as a local variable. This means that only this fuction can access it meaning the global variable stays the same.

    print('Hackclub is ' + x)

myopinion() # This runs the funcion 'myopinion' with 'x' being a local variable in which the code says to prints the message 'Hackclub is supportive!'.

# P.S. fuctions are like variables but they store code instead of values. etc 'print'

# You can stright up remove the feature from the function and use a keybaord 'global' to make defining the variable in the function a global variable.

x = 'amazing!'

def myopinion():
    global x # This makes 'x' a global variable in this function so insead of being local, the changes are global.
    x = 'supportive!' 

    print('Hackclub is ' + x)

myopinion()


print(" ")
print("Tenth lesson") # The Tenth lesson talks about the different types of data in Python,

print("Text data types: str - (x = 'Hack')") 
# The only text data type is called 'str'. This is used for text because it uses ' or " to classify what is a word and what is a number.

print("Numerical data types: int - (x = 42)  |  float - (x = 42.1)  |  complex - (x = 42j)") 
print(" ")

# Int or interger is used for classifying whole numbers. When using x = 43.54 it will output as 43, because 43.54 isn't a whole number, it removes the decimal numbers.
# float is classifying the entire number. When using x = 43.54 it will output as 43.54.
# complex classifyies complex number (numbers with j). If you use any other data type with j, you will get an error.

print("Sequence data types: List - (x = ['mango', 'watermelon', 'pear'])  |  Tuple - (x = ('mango', 'watermelon', 'pear'))  |   Range - (x = range(6))") 
print(" ")

# Lists are used to store mutiple variables in a single variable. Lists can be changed after defining and can only be created using []. 
# Tuple is a more secure version of lists. Tuples are exactly like lists but they can't be changed after defining it and can only be created using ().
# Range is confusing and wasn't properly explained. I thought it showed the range of a list of numbers but after testing it, it didn't work.

print("Mapping data types: Dict - (x = {'name': 'Hackclub', 'type': 'community'})")
print(" ")

# Dict mean dictionary which stores data in data in groups. There isn't much funcability with this but for naming variable in a variable.

print("Set data types: Set - (x = {'mango', 'watermelon', 'pear'})  |  Frozenset - (x = frozenset({'mango', 'watermelon', 'pear'}))")
print(" ")
# Set is like list where values can be stored in a variable but they are unordered and have to be unique.
# Frozenset is just like tuple where the values can't be changed after defining it. The difference is just like the set with list.
# Forzenset is just an unchangable set like tuple is an unchangeable list.

print("Boolean data types: bool - (x = True or False)")
print(" ")

# Bool is a data type that is only True or False. This can also simplify code where 1 = True and 0 = False.

print("Binary data types: bytes - (x = b'Hackclub')  |  bytearray - (x = bytearray(5))  |  memoryview - (x = memoryview(bytes(5)))")
print(" ")
# Bytes is a data type that stores binary data. Byte can not be changed making them secure. Don't really know to usage of it.
# Bytearray is a data type that stores binary data but can be changed. Still don't know what use it has.
# Memoryview is a data type that allows you to access Bytes with out copying it. You can use indexing with this since Bytes are unchangable.

# You can manually set and find the data type but using a few commands.

# putting a data type and inclosing the variable in a (), manually sets the data type to that data type. When doing this you can now use '()' for any data type.

x = str(('Hackclub')) # str data type
y = int(123) # int data type
z = tuple(('SoM', 'Highway', 'Boba')) # tuple data type

# You can find the data type by using the 'type()' command

print(type(x))
print(type(y)) 
print(type(z))  


print(" ")
print("Eleventh lesson") # The eleventh lesson talkes about numbers in Python.

# Int or intergers are positive or negitive numbers withoiut decimals or in other words, whole numbers.

ix = 68487274
iy = -48265
iz = 6

print(ix) 
print(iy) 
print(iz)
print(" ")

# Float is a number that can have decimals as well as being positive and negitive. 

fx = 1.11
fy = 1.0
fz = -183.6743

print(fx)
print(fy)
print(fz)

# Floats can even use scientific numbers like 'e' to repersent large numbers.

fx = 937e3
fy = 12e-4 
fz = 1.2e6

print(fx)
print(fy)
print(fz)
print(" ")

# Complex numbers are numbers that use imaginary numbers. These number use 'j' to repersent imsginart numbers.

cx = 8 + 9j
cy = 22j
cz = -1j

print(cx)
print(cy)
print(cz)

# You can also change numbers that already has a data type to another type by using the type name and inclose the variable in ().

x = 87
y = 4.56
z = 4 + 20j

a = float(x) # This switches the 'x' variable (87) from a int to a float (87.0).
b = int(y) # This switches the 'y' variable (4.56) from a float to a int (4).
c = complex(y) # This switches the 'y' variable (4.56) from a float to a complex number (4.56 + 0j).

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 
print(" ")

# The next parts taks about random number module which is perfect for my game project.

import random # Python doesn't have a built in random number module, so we need to import it.

print(random.randrange(1, 10))
print(" ")


# My tutorial has a part which tells you more about random number module for python but it parts away from the tutorial. I decided to split off to the random number module to learn for my game.
# The random module tutorial has sections of each function in the random module. I will be going though them as lessons.
# RM = Random Module

print("RM Lesson 1") # The first RM lesson is seed()

random.seed() # Seed / preset
print(random.randrange(1, 10)) # Generator

random.seed(4) # Seed / preset
print(random.randrange(1, 10)) # Generator

random.seed(100) # Seed / preset
print(random.randrange(1, 10)) # Generator

random.seed(100) # Seed / preset
print(random.randrange(1, 10)) # Generator
# The seed() fuction is used to set a seed for the ranom number genetrator. This is like a preset where every number generator using the seed will be the same and wont change.

# The syntax for the seed() function is confusion and doesn't make sense to me.
random.seed(a, version=2)
# a - This is the seed value. 
# version = No clue how it works.
print(" ")


# The second RM lesson is getstate() and setstate()
# Copying code from tutorial to note it.

#print a random number:
print(random.random()) # Generator (random)

#capture the state:
state = random.getstate() # getstate() captures the next state of the random numbert generator and saves it into a variable called 'state'
#print another random number:
print(random.random()) # Genetrator (random)

#restore the state:
random.setstate(state) # setstate() restores the state of the random number generator to the state captured by getstate()
print(random.random()) # Generator (set number)

print(random.random()) # Generator (random)

print(" ")
# I want to try to change the code

print(random.randrange(1, 50)) # Generator (random)(used to show when set state is implemented)

FunRoll = random.getstate() # Captures next random number)
print(random.randrange(1, 50)) # Generator (set number (technaclly random))

random.setstate(FunRoll) # sets the variable 'Funroll' to the next generator
print(random.randrange(1, 50)) # Genertor (set number)

print(random.randrange(1, 50)) # Generator (random)(used to show when set state is implemented)

print(" ")
# All of them is set as a set state so I'm going to try it again with seed()

random.seed() # uses time to generate random number
print(random.randrange(1, 50)) 

ExtraFunRoll = random.getstate() # gets seed and set to variable 'ExtraFunRoll'
print(random.randrange(1, 50)) # generates a random number

random.setstate(ExtraFunRoll) # sets the variable 'ExtraFunRoll' to the next generator
print(random.randrange(1, 50)) # Generator (set number)

random.seed() # uses time to generate random number
print(random.randrange(1, 50)) # generates a random number

print(" ") 
# Can I simplify the code? 

print(random.randrange(1, 50)) 

ExtraFunRoll = random.getstate() # gets seed and set to variable 'ExtraFunRoll'
print(random.randrange(1, 50)) # generates a random number

random.setstate(ExtraFunRoll) # sets the variable 'ExtraFunRoll' to the next generator
print(random.randrange(1, 50)) # Generator (set number)

print(random.randrange(1, 50)) # generates a random number
print(" ")
# I realaised that the code will already be connected to the seed() so I won't be able to simplify it properly.

print("RM Lesson 2") # The second RM lesson is getrandbits()

a = 6
random.getrandbits(a)
print(random.getrandbits(a))
print(" ")

# Not sure what the point of this fuction is too so not much known.

print("RM Lesson 3") # The third RM lesson is randrange() and randint()

print(random.randrange(1, 10)) # This prints a random number between the ranges 1 and 10

# This is the syntax of the randrange() function. Because of this I finnially understood the syntax means. Syntax is basically the instructions of the function.

print(random.randrange(5, 20, 5))
# random.randrange( start, stop, step) 

# Start is a optional number to put to instruct what number to start with. Without it, the start will be 0
# Stop is the number that to put to instruct the function to stop at. This number is required or else it will go forever and become an error
# Step is an optional number to instruct the function on the size of the increments the fuction takes within the range. The defult number is 1.

# The next part talks about the randint() function.

print(random.randint(0, 50)) # This print a random integer between the 2 ranges written down, 0 and 50

# The syntax for the randint() function is 
# randint(start, stop)
# Start is the number that the function will start at
# Stop is the number that the function will stop at

# This code is basically the same as the randrange() function but with some changes. randint only uses integers where the step number is always 1.
# This code also requires the start and stop numbers to be definded or else it will go on forever and become an error.

print(" ")
print("RM Lesson Four") # The fourth RM lesson is choice() and choices()

# A choice() is a function that randomly selects a value from any variable. I could be a range, list, tuple, or string.

NameList = ["Niko", "Raymont", "Koji", "Acon", "Valen"] # Defines what is in the list
print(random.choice(NameList)) # Generates random name out of list

# You can also use the choice() function with strings
print(random.choice("Hackclub")) # Generates a random letter from the string "Hackclub"

# Choice() function basically choses from a list of values

# The next part of the tutorial talks about the choices() function.
# The difference between choice() and choices() is that choices() can generate multiple random values from a list of values and has more configurations.

MultiMoney = [100, 200, 300, 400, 500] # Defines what is in the list
print(random.choices(MultiMoney, k = 3)) # Generates 3 random numbers from the list
# The k means how many times the fuction will generate a random number. This code generates 3

print(random.choices(MultiMoney, weights = [10, 7, 5, 2, 1], k=1)) # Generates 1 random number with probalility
# Weight is beasically the chances of the value in the list being selected. The higher the better

print(random.choices(MultiMoney, cum_weights = [10, 12, 15, 18, 20], k=1)) # Generates 1 random number with cumulative probability
# I don't really understand the use of cum_weights or even the use of it.

print(" ")
print("RM Lesson Five") # The fifth RM lesson is shuffle() and sample()

# The shuffle() function is used to randiomly shuffle the vales in a list. This might be a great idea for my game project.
CardsHearts = ['2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥'] # Defines the list of cards
random.shuffle(CardsHearts) # Shuffles the list of cards
print(CardsHearts) # Prints the shuffled list of cards
# The shuffle() function doesn't create any new list, it changes the original list.

# The nest part is called the sample() function
CardsSpades = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠'] # Defines the list of cards
print(random.sample(CardsSpades, k=5)) # Generates 5 random cards as a hand
# The sample() function is used to generate a random sample from a list of values.

# These fuctions are great of my game project.

print(" ")
print("RM Lesson Six") # The sixth RM lesson is random(), uniform() and triangular()

# The random() function is used to generate a ranfom float from 0 - 1, etc 0.6837265
print(random.random()) # Generates a random float from 0 - 1, very simple

# The uniform() function is used to generate a random float from a range of numbers.
print(random.uniform(1, 500)) # Generates a random float from 1 - 500, just like randrange but with float numbers instead of integers

# The triangular() function is used to generate a random float from a range of numbers with a peak.
print(random.triangular(1, 100, 10)) # Generates a random float between 1 - 100 but it is weighted or has a higher change of being closer to 10.
# The syntax for the triangular() function is triangular(low, high, mode)
# Low is bassically like the randrange function where it is the start of the range
# High is the stop of the range
# Mode is a bit differet where it has a peak, this is where the random number will be more likely

print(" ")
# The rest of the RM lessons are not really useful for my kind of knowledge, the functions are tagged with, 'Ued in statistics' and 'Used in theroy.
#I decided to stop the RM lessons here since I already gotten a lot of information and functions for my game project.
