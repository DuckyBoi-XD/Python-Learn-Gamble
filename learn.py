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

var1 = 5
var2 = "Raymont"

# The lesson also shows how to print variables. Instead of print with ("_______"), we can just  put in the variable name in (___). 

print(var1)
print(var2)

print(" ")
print("Fifth lesson")  # The fifth lesson teaches how to use casting to print specific data types.

str1 = str(7.2) # str means string which is the text of the variable, 7.2 would output as 7.2 and  'apple' would output to apple

int1 = int(7.2) # int mean integer which is a whole number not a decimal, 7.2 would output as 7  and 'apple' would output as an error due to it not being a number but a text

float1 = float(7.2) # float means (I guess) floating which means that the output number would be the
# exact number (I think) and not text. So, 7.2 would output as 7.2 and 'apple' would output as an error due to it not being a number but a text

print(str1)
print(int1)
print(float1)

# When code becomes like this I like to play around with the code to potentioally make it better  or break it completely.

X = 4.761 # This varible is to change all the other casting varibles quickly.

str2 = str(X)
int2 = int(X)
float2 = float(X)

print(str2)
print(int2)
print(float2)

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

m, w, p = 'mango', 'watermelon', 'pear' # This prosses is basically assigning a list of variables with a list of values.

print(m)
print(w)
print(p)

# If you want to assign the variables as the anme value you just put '=' everywhere.
straw1 = straw2 = straw3 = 'strawberry'
print(straw1)
print(straw2)
print(straw3)

# If you want to reverse it and get the values from the variables you do something called unpacking.  
fruits = ['mango', 'watermelon', 'pear'] # listing the values into a variable.

m1, w2, p2 = fruits # assigning the variables to the valuesin the variable 'fruits'

print(m1) # This will print the first value of the variable 'fruits', which is 'mango'
print(w2) # This will print the second value of the variable 'fruits', which is 'watermelon'
print(p2) # This will print the third value of the variable 'fruits', which is 'pear'

print(" ")
print("Eighth lesson") # The eighth lesson teaches how to output variables, like text, in 'print' 

Opinion = 'people from the Hackclub community are really helpful!'
print(Opinion)

a11 = 'People '# Notice there are spaces between the word and the quotation mark, this is to make sure that the words are spaced out when printed.
b11 = 'from '
c11 = 'the '
d11 = 'Hackclub '
e11 = 'community '
f11 = 'are '
g11 = 'really '
h11 = 'helpful!'
print(a11, b11, c11, d11, e11, f11, g11, h11) # This is using the ',' symbol to combine the string variables together to make a sentance.

print(a11 + b11 + c11 + d11 + e11 + f11 + g11 + h11) # This can also be done with the '+' symbol.

# With numbers, if you use the '+' symbol, the numbers will be added up instead of being combined.
x = 42
y = 31
print(x + y)

# You can combine 2 variables together even when one is text and one is a number. This is because a number can be a string and a text is already a string.
x2 = '42'
y2 = 'Koji'
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

print("Twelfth lesson") # The twelfth lesson which talks about casting
# Casting the fuction where you change the data type of a cariable to another
# Pythin automatically assaignes a data type to a variables when you defind it

x = 5
y = 45.32
z = "Hackclub"

print(type(x)) # Prints the data type of x, which is int
print(type(y)) # Prints the data type of y, which is float
print(type(z)) # Prints the data type of z, which is str

print(" ")

# You can change the data type of a variable by using the casting function
fx = float(x) # Changes the data type of x from int to float
iy = int(y) # Changes the data type of y from float to int
sz = str(x) # Changes the data type of x from int to str

print(fx) # Prints the value of fx, which is 5.0
print(type(fx)) # Prints the data type of fx, which is float
print(iy) # Prints the value of iy, which is 45
print(type(iy)) # Prints the data type of iy, which is int
print(sz) # Prints the value of sz, which is '5'
print(type(sz)) # Prints the data type of sz, which is str

print(" ")

print("Thirteenth lesson") # The thirteenth lesson talks about strings or str
# Strings are a data type that is used to store text. 
# Strings can be defined by using single quotes or double quotes. I think double quotes is better because you might need to use single quotes in a string
# If you use single quotes in a string using singe quotes to define it, it will come out as an error.

x = "Hackclub is awesome" # Defines a string using double quotes
y = 'Hackclub is awesome' # Defines a string using single quotes
print(x) # Prints the value of x
print(y) # Prints the value of y
# They will output as the same thing, so it doesn't matter which one you use

print(" ")

x = "Hackclub's programs are supportive" # This string uses single quotes in the string. Since I used double quotes to deifine it, it'a ok
# y = 'Hackclub's programs are supportive'
# # This string uses single quotes in the string. Since I used single quotes to define it, it will come out as an error
print(x) # Prints the value of x

# To assign a string to a variable you need to do this:
X = "Hackclub" 
Y = 'Hackclub'
# Names variable at the start
# Defines a string using double quotes or single quotes

print(" ")

# Milti-line strings are impornt when writing strings that are more than 1 line.
x = """There are many types of coding languages
Python
Java
C++
and many more""" 
# You can have string with multiple lines by using either triple single quite ''' or triple double quotes """
# If you don't use tripe quotes, when you move to the next line, it will be considered as a new line of code
print(x) # Prints the value of x, which is a multi-line string

# String are arrays (sort of like lists)
# Because string is like arrays you can access each caracter of a string using indexing
x = "Hackclub"
print(x[0]) # Prints the first character of the string, which is 'H'

print(" ")

# You can also use loops to access each character of a string
# The tutorial also splits off the string lesson to the loop lesson. I will be going through the loop lesson later on so I decided to stay on the strings.
for x in "Hackclub":
    print(x) # Prints each character of the string on a new line

print(" ")
# To find the length of a string you can use the len() functiom
x = "Summer of Making"
print(len(x)) # Prints the length of the string

print(" ")

# To check if a string contains a certain phrase or character 
Hackinfo = "Hackclub is a community which helps teens create awesome projects"
print('community' in Hackinfo) # Prints a boolean value which is either ture of false
# You can also use an 'if' statements to take advantage of the boolean value
if 'community' in Hackinfo:
    print("Yes, 'community' is in the string") # This prints the message if there is 'community' in the string

print(" ")

# To check if a string doesn't contain a certain phrase or character
Hackinfo = "Hackclub is run by many teens to are passantate about coding and helping others"
print('mean' not in Hackinfo) # Prints a boolean value which is either true or false
if 'mean' not in Hackinfo:
    print("No, 'mean' is not in the string") # This prints the message if there is no 'community' in the string

print(" ") 

print("Fourteenth lesson") # The fourteenth lesson talks about string slicing
# Strng slicing is the way to access parts of a string's character by using indexing
FruitFav = "My favourite fruit it mango"
print(FruitFav[2:7])

# If you just want to start on the first character and pick the last character, you can just leave the first number blank
print(FruitFav[:12]) # This will print the first 12 characters of the string
# if you want to do the opposte you do the opposite
print(FruitFav[13:]) # This will print the string starting from the 13th character to the end of the strin

# This is because the syntax of this function is:
# print(variable[start:end])

# You can also use negative indexing to start from the edn of the string
print(FruitFav[-5:-1]) # This will start the slice from the last 5 character and end on the last character.

print(" ")

print("Fifteenth lesson") # The fifteenth lesson talks about string modification

# First there is a fucntion called upper() which converts all the characters in the string to uppercase
UpperFunction = "hackclub"
print(UpperFunction.upper()) # This will print the string in uppercase

# Next there is a function that does the opposite and converts all the character into lowercase
LowerFunction = "HACKCLUB"
print(LowerFunction.lower()) # This will print the string in lowercase

# Then there is a function called strip() which remove any whitespace at the start and end of the string
StripFunction = "   HackClub   "
print(StripFunction.strip()) 

# After that there is a function called replace() which replaces the string with another string
# How this works is that the first value you put in the replace() function is what value your changing and the second value is what your changing it to.
ReplaceFunction = "Hackclub is a community"
print(ReplaceFunction.replace("community", "supportive")) # This will replace the word 'community' with 'supportive'

# Next there is a function all split() which splits the string into 2 values
# For this you need to add a value that you want to split the string
SplitFunction = "Hackclub is a community"
print(SplitFunction.split("is")) # This will split the string into 2 values

print(" ")

print("Sixteenth lesson") # The sixteenth lesson teaches about concatenating strings

# To combine stings you use the + operator
FirstString = "Hackclub is"
SecondString = "very helpful!"
CombinedString = FirstString + SecondString # This will combine the 2 strings, FirstString and SecondString
print(CombinedString) # This will print the combined string

# You can also add the string " " to add a space between the 2 strings
CombinedString2 = FirstString + " " + SecondString # This will combine the 2 strings with a space in between
print(CombinedString2) # This prints the CombinedString2 variavble

print(" ")

print("Seventeenth lesson") # The seventeenth lesson teaches about string formatting

# String formatting is used for formatting string so it can be added to a number
# In python you can use the + operator with the a string variable and a number variable so you need to use the format function

Age = 5
# Defines age
CatAge = f"My cat's age is {Age}" # Combines both variables using formatting
print(CatAge) # Prints formmating
# This works because:
# 'f' formats the string and it allows you to add a variable inside '{}' for the text to be finished

# You can use something like this as Place holders
Price = random.uniform(0.99, 9.99)
Price2 = random.uniform(10, 15.99)
Option = f"The price is {Price2}, but with a discount it is {Price}" # This will create a variable with this text
print(Option) # Prints the variable Option
# Here is similar to the previous one but uses the variables as placeholders
# I used the unifrom function for fun with this but there is a problem with this, the numbers are too big

# You can format the variable different ly by using different commands
Price3 = 8
Price4 = 96
Option2 = f"The price is {Price2:.2f}, but with a discount it is {Price:.2f}" # This will format the variable to 2 decimal places
print(Option2) # Prints the variable Option2
# This code basically just formats the variable place holders to 2 decimal places with the command '.2f'.
# You can change the number of decimal places by changing the '2' in '.2f'

print(" ")
print("Eighteenth lesson") # The eighteenth lesson teaches about escaped characters
# Escape characters are really interesting. It basiaclly becomes an override feature for the string 

# If you use any illigel (causes an error) characters in a string, for example a single quote in a string that is defined by single quotes, it will come out as an error.
# To fix this you can use a backslash '\' before the illegel character
EscapeCharater = 'Hackclub\'s programs are creative' # This string removes the error in front of the backslash and continues on
print(EscapeCharater) # Prints the variable even with the single quote in the string

# There is even a list of commands that you can use with the backslash
# \' will make '
# \" will make "
# \\ will make \
# \n will make a new line
# \r will make a new line (carriage return)(Basically called 'override line')
# \t will make a tab (big spaces for readability)
# \b will make a backspace (removes the character before the \b)
# \f will make a form feed (not really useful for modern code)
# \ooo will make a character with the octal value ooo (to hard for me))
# \xhh will make a character with the hex value hh (to hard for me)
print(" ")

print("Nineteenth lesson") # The nineteenth lesson teaches about string methods
# There is a lot of methods so I'll have to list and explain them

# capitalize() - This method capitalizes the first character of the string
CapitalizeMethod = "hackclub is amazing"
print(CapitalizeMethod.capitalize()) # This will capitalize the first character of the string

# casefold() - This method converts the string to lowercase
CasefoldMethod = "HACKCLUB IS AMAZING"
print(CasefoldMethod.casefold()) # This will convert the string to lowercase

# center() - This method centers the string into a new string with characters on both side
CenterMethod = "Niko"
print(CenterMethod.center(20, "_")) # This will put 'Niko' into the centre of a new string where '_' centres it
# The number '20' hold the vale of the length of the new string

# count() = This method counts the number of values in a string
CountMethod = "Like when I like to like things, I often like to use things that are like similar to what I like"
print(CountMethod.count("like")) # This will count the number of times 'like' appears in the string

# encode() - This method encodes the string into bypes
EncodeMethod = "Mango2267"
print(EncodeMethod.encode()) # This will encode the string into bytes

# endswith() - This method checks at the end of the string to find a punctuation value you have assaigned by outputing a boolean value
EndswitchMethod = "Summer of Making!"
print(EndswitchMethod.endswith("!")) # This will output a boolean if there is a '!' in my string

# expandtabs - This method expands the tabs used in a string
ExpandTabs = "h\ta\tc\tk\t"
print(ExpandTabs.expandtabs(8)) # This will expand the tabs spaces by the value placed

# find() = This method finds where the first occurance of a value is
FindMethod = "Summer of Making rewards prizes!"
print(FindMethod.find("prizes")) # This will find and calcualte the number or character to the string in the string
# You can also look for letter and search for values in specifc spots
FindMethod2 = "Huddle around! Get your news here."
print(FindMethod2.find("u", 15, 34)) # This will find and calcualte the character from the start to the string in the string from the 15th caracter to the end
# If the method can't find any values in the area, it will output -1

# index() - This method is similar to the find() method but it will output an error if it can't find the value
IndexMethod = "Summer of Making is a great program!"
print(IndexMethod.index("great")) # This will calcutate the number of character to the value
# You can use index() pretty muchb exactly like the find() method

# There is still so much more methods but I feel like I gotten the main ones so I'll just stop here and look back at it if i need it.

print(" ")
print("Twentieth lesson") # The twentieth lesson teaches about boolean

# Boolean is a data type that can only be True or False. This is used to check if a condition is met or not.
# There are many ways to use boolean
print(9>3) # This is true
print(5==5) # This is also true
print(2==3) # This is false
print(3<1) # This is also false
# This is coalled conditional statements. This is used to check if a condition is met or not.

# You can use this in an if statement to check if a condition is met or not and run a code if it is met or not

PlayerFund = random.randrange(1, 30)
Player2Fund = random.randrange(1, 30)

if PlayerFund < Player2Fund:
    print("Niko is poor")
elif Player2Fund < PlayerFund:
    print("Niko is rich")
else:
    print("Lol")

# Boolean function can also evaluate a value

Boolean1 = "Pan Fry"
Boolean2 = 6363.64
Boolean3 = "582 pancakes"

print(bool(Boolean1))
print(bool(Boolean2))
print(bool(Boolean3))
print(" ")


print("Twenty-first lesson") # The twenty-first lesson teaches about operations and operators

# There are many types of operators in Python which are similar to math operators so it's really simple
ExamplePlus = 5 + 3 
print(ExamplePlus)

ExampleMinus = 5 - 3
print(ExampleMinus) 

ExampleMultiply = 5 * 3
print(ExampleMultiply)

ExampleDivide = 5 / 3
print(ExampleDivide)

ExampleModulus = 5 % 3
print(ExampleModulus) # This will output the remainder of the division

ExampleExponent = 5 ** 3
print(ExampleExponent)

ExampleFloorDivision = 5 // 3
print(ExampleFloorDivision) # This will divide the number and outut as a whole number
print(" ")

# There is also operators that can assaign values as while using the value it is defining
ExampleEquals = 42
print(ExampleEquals)

ExamaplePlusEquals = 42
ExamaplePlusEquals += 42
print(ExamaplePlusEquals) # This will add 42 to the variable 

ExampleMinusEquals = 42
ExampleMinusEquals -= 42
print(ExampleMinusEquals) # This will subtract 42 from the variable 

ExampleMultiplyEquals = 42
ExampleMultiplyEquals *= 42
print(ExampleMultiplyEquals) # This will multiply 42 to the variable 

ExampleDivideEquals = 42
ExampleDivideEquals /= 42
print(ExampleDivideEquals) # This will divide the variable by 42

ExampleModulusEquals = 42
ExampleModulusEquals %= 42
print(ExampleModulusEquals) # This will output the remainder of the division

ExampleFloorDivisionEquals = 42
ExampleFloorDivisionEquals //= 42
print(ExampleFloorDivisionEquals) # This will divide the variable by 42 and output as a whole number

ExampleExponentEquals = 42
ExampleExponentEquals **= 42
print(ExampleExponentEquals) # This will raise the variable to the power of 42

ExampleBitwiseAnd = 42
ExampleBitwiseAnd &= 42
print(ExampleBitwiseAnd) # I've tried to understand what it does but because I couldn't but I knew I wouldn't need it. As well as the last few

ExampleBitwiseOr = 42
ExampleBitwiseOr |= 42
print(ExampleBitwiseOr) # This will do a bitwise OR operation on the variable

ExampleBitwiseXor = 42
ExampleBitwiseXor ^= 42
print(ExampleBitwiseXor) # This will do a bitwise XOR operation on the variable

ExampleRightShift = 42
ExampleRightShift >>= 42
print(ExampleRightShift) # This will shift the bits to the right by 42

ExampleLeftShift = 42
ExampleLeftShift <<= 42
print(ExampleLeftShift) # This will shift the bits to the left by 42

print(ExampleDirectDefind := 42) # This operation is good for defining a variable directly in a print statement or a function
print(ExampleDirectDefind)
print(" ")

# There are also operators that can compare values
ExampleEqual = 42 == 42
print(ExampleEqual) # This will look for if the values are the same

ExampleNotEqual = 42 != 42
print(ExampleNotEqual) # This will look for if the values are different

ExampleGreaterThan = 42 > 42
print(ExampleGreaterThan) # This will look for if the left value is greater than the right value

ExampleLessThan = 42 < 42
print(ExampleLessThan) # This will look for if the left value is less than the right value

ExampleGreaterThanOrEqual = 42 >= 42
print(ExampleGreaterThanOrEqual) # This will look for if the left value is greater than or equal to the right value

ExampleLessThanOrEqual = 42 <= 42
print(ExampleLessThanOrEqual) # This will output True if the left value is less than or equal to the right value
print(" ")

# There is also logical operators
ExampeAnd = 2 + 2 == 4 and 3 * 4 == 12
print(ExampeAnd) # This will check if both statements are true

ExampleOr = 99 / 3 == 33 or 100 - 1 == 98
print(ExampleOr) # This will check if at least one of the statements is true

ExampleNot = not 2 + 2 == 4
print(ExampleNot) # This will check if the statement is false. This basiacally the same as the 'And' operator but just outputs the opposite

# There is a set of operators which is really unque. It looks if 2 variables are the same or not

Isx = 'potato'
Isy = 'potato'

ExampleIs = Isx is Isy
print(ExampleIs) # This will check if the vlaues are the same

Isz = 'apple'
Isa = 'banana'

ExampleIsNot = z is not a
print(ExampleIsNot) # This will check if the values are not the same

# There is a set of operations to check if a variable is in a variable or not
Inx = "helpful"
Iny = "Hackclub includes a helpful community"

ExampleIn = Inx in Iny
print(ExampleIn) # This will check if the value of Inx is in the value

NotInx = "mean"
NotIny = "Hackclub includes a helpful community"

ExampleNotIn = NotInx not in NotIny
print(ExampleNotIn) # This will check if the value of NotInx is not in the value of NotIny

# There is a set of operators that are used for bitwise operations which I won't wanna look into
# The tutorials talks about how operations have order but it's just like in math so im going to skip over it

print(" ")
print("Twenty-second lesson") # The twenty-second lesson teaches about lists

# Lists are a data type that is used to store multiple values in a single variable.
# There are 4 types of lists, list, tuple, set, and dictionary

# A list is used to store multiple values in a single variable. Lists can be changed.
# Lists have a defiend order meaning when you add another value, it will be added to the end
# Lists are also changable meaning they can be changed after being definded
# Lists are also indexed meaning you can access each value in the list using indexing
ExampleList = ["Summer of Making", "Boba", "Highway"] # A list is defined by using '[]', square brackets 
print(ExampleList)

# A tuple is used to store mutiple values in a simgle variable just like lists but can't be changed after defining.
# Tuples are ordered and inexed but unchangable 
ExampleTuple = ("Summer of Making", "Boba", "Highway") # A tuple is defined by using '()', round brackets
print(ExampleTuple)

# A set is used to store multiple values in a single variable.
# Sets are very strict where they are unordered, unchangable, unindexed and doesn't allow duplicates
ExampleSet = {"Summer of Making", "Boba", "Highway"} # A set is defined by using '{}', curly brackets
print(ExampleSet)

# A dictionary is used to store multiple values in a single variable but it is unordered and indexed. Dictionaries can have duplicate values.
# Dictionaries are changable and ordered but doesn't allow duplicate values
ExampleDictionary = {"Summer of Making": "Hackclub", "Highway": "Hackclub", "Boba": "Hackclub"} # A dictionary is defined by using '{}', curly brackets but with colons to key values
print(ExampleDictionary)
print(" ")

print("Twenty-third lesson") # The twenty-third lesson teaches about changing values in lists

# You can change the values in a list by using indexing
ExampleList = ["Summer of Making", "Boba", "Highway"]
ExampleList[1] = "Pizza Party" # This will change the second value to "Pizza Party"
print(ExampleList)

# You can change a range of values using colons to define the values
ExampleList2 = ["Niko", "Raymont", "Koji", "Acon", "Valen", "Ruby", "Alexren", "Cyao"]
ExampleList2[1:5] = ["Qincai", "Person"] # This will change the values from index 1 to 5 to "Qincai" and "Person"
print(ExampleList2) 
print(" ")


print("Twenty-fourth lesson") # The twenty-fourth lesson teaches about adding values to lists

# You can add values to a list by using the append() function
ExampleList4 = ["Python", "Java", "C++"]
ExampleList4.append("JavaScript") # This will add the new vlaues to the list
print(ExampleList4) 

# If you want to insert (not add) a value to a list you can do it by using the insert() function
ExampleList3 = ["Python", "Jave", "C++"]
ExampleList3.insert(1, "JavaScript") # This will add "JavaScript" at index 1
print(ExampleList3) 

# If you want to transfer all the values from one list to another you can use the extend() function
CodeLanguages = ["Python", "Java", "C++"]
ExampleList4 = ["JavaScript", "C#", "Bash"]
CodeLanguages.extend(ExampleList4) # This will add all the values from ExampleList4 to CodeLanguages
print(CodeLanguages) 
# extend() can also be used with sets, tuples, and dictionaries

print(" ")

print("Twenty-fifth lesson") # The twenty-fifth lesson teaches about removing values from lists

# You can remove a value from a list by using the remove() function
ExampleList5 = ["Python", "Java", "C++", "JavaScript"]
ExampleList5.remove("Java") # This will remove Java from the list
print(ExampleList5)
# If there is mutiple occurances of the value, it will only remove the first one

# If you want to remove a value from a list by index you can use the pop() function
ExampleList6 = ["Python", "Java", "C++", "JavaScript"]
ExampleList6.pop(2) # This will remove the value at index 2 'C++'
print(ExampleList6)

# You can also use the del command to do the same thing as pop()
ExampleList7 = ["Python", "Java", "C++", "JavaScript"]
del ExampleList7[2] # This will remove the value at index 2 'C++'

# You can also nuke the list with the del command
del ExampleList7 # This will remove the entire list
# print(ExampleList7) # This will cause an error because the list has been deleted
# There is also a clear() function where it will clear the values in the variavle/list but not nuke the list varaiable
ExampleList8 = ["Python", "Java", "C++", "JavaScript"]
ExampleList8.clear() # This will clear the values in the list
print(ExampleList8) 
print(" ")


print("Twenty-sixth lesson") # The twenty-sixth lesson teaches about looping through lists
# Looping is basically going through the entire list and taking each value one by one.
# THere are 3 methods to loop through a list in Python, for loop, indexing, while loops, and list comprehensions

# You can loop a list by using a for loop
ExampleList9 = ["Highway", "Boba", "SoM"]
for x in ExampleList9: 
    print(x) 
# This works by taking each value in the list and assigning it to the variable x, then printing it
print(" ")

# You can loop a list using indexing
ExampleList10 = ["Highway", "Boba", "SoM"]
for i in range(len(ExampleList10)): 
    print(ExampleList10[i])
# This works by using the range() and len() function to get the length of the list and then using indexing to print each value
print(" ")

# You can loop a list using the while loop
ExampleList11 = ["Highway", "Boba", "SoM"]
l = 0 # This will start the loop at index 0
while l < len(ExampleList11): # This will loop through the list until it reaches the end
    print(ExampleList11[l]) # This will print the value at index l
    l += 1 # This will increase the index by 1
# This works by using a while loop to loop through the list until it reaches the end, then printing each value
print(" ")

# You can also use list comprehensions to loop through a list
ExampleList12 = ["Highway", "Boba", "SoM"]
print([x for x in ExampleList12]) 
# I don't really understand how this works but it works
print(" ")


print("Twenty-seventh lesson") # The twenty-seventh lesson teaches about list comprehensions

# List comprehensions are a way to create lists in a single line of code than 3 lines of code using for statements
# In my opinion, list comprehensions are a bit confusing but I will try to explain it

# This code is just me playing around
HackyPeople = ["Niko", "Acon", "Person", "Rowan", "Valen", "Alexren"]
HackyPeople2 = ["Niko", "Valen", "Acon"]

ExampleListComprehension = [VIP for VIP in HackyPeople if VIP not in HackyPeople2]
print(ExampleListComprehension)

# There is many imporntant components to a list comprehension

# This is the syntax for a list comprehension:
#[(changes) for (Each Value) in (variable/list) if (condition/rules)]

# The first part is the changes.
# The' changes' part addes a modification to the output of the code. However this is not needed and you can repeat the 'Each Value' part
# For example, if you want to add 1 to each value as the output, you would write: [x + 1 for x in y], x = 'Each Value', y = variable/list

# The second part is the 'Each Value' part.
# The 'Each Value' part definds each value in the varabile/list into one value but uses them separatly.
# This values is not important and it more of a place holder value when afterwards it's used, it won't be used again.

# The third part is the variable/list.
# The variable/list is the list you are using to create the new one.

# The fourth part is the 'condition/rules' part.
# The 'condition/rules' part is used to filter the values in the list/variable for the output.
# This is simmilar to the first part or 'changes' but it filters the values instead of changes them.

Pets = ["Dog", "Cat", "Fish", "Hamster", "Bird"]
ExampleListComprehension2 = [x for x in Pets if 'a' in x or 'i' in x]
print(ExampleListComprehension2)
print(" ")


print("Twenty-eighth lesson") # The twenty-eighth lesson teaches about sort() function

# The sort() function is used to sort the values in a list in different ways
SortList = ["Cat", "Dog", "Fish", "Hamster", "Bird"]
SortList.sort()
print(SortList)

# You can reverse the sort function too
SortList2 = ["Cat", "Dog", "Fish", "Hamster", "Bird"]
SortList.sort(reverse = True)
print(SortList)

# You can even make your own sort function but I won't bother with doing that

# There are a lot of feature in this. There is one called incasesensitive
# The sort() function will prioritise capatailized letters. This feature will ignore that
SortList3 = ["Cat", "dog", "Fish", "hamster", "Bird"]
SortList3.sort(key = str.lower)
print(SortList3)

# There is a revere function just like the sort(reverse)
SortList4 = ["Cat", "dog", "Fish", "hamster", "Bird"]
SortList4.reverse()
print(SortList4)
print(" ")


print("Twenty-ninth lesson") # The twenty-ninth lesson teaches about the copy() function
# There is many ways to copy lists to another list because you can't simply do x = y

# copy() function 
ExampleCopy = ["Highway", "Boba", "SoM"]
ExampleCopy2 = ExampleCopy.copy()
print(ExampleCopy2)

# list() function
ExampleCopyList = ["Highway", "Boba", "SoM"]
ExampleCopyList2 = list(ExampleCopyList)
print(ExampleCopyList2)

# slice operator
ExampleCopySplit =  ["Highway", "SoM"]
ExampleCopySplit2 = ExampleCopySplit[:]
print(ExampleCopySplit)
print(" ")

print("Thirtieth lesson") # The thirtieth lesson teaches about joining 2 or more lists together

# The first and simpe way to combine list is to use the '+' operator
ExampleCombinePlus = [1, 2, 3, 4, 5]
ExampleCombinePlus2 = ["Potato", "Advocado", "Lettuce", "Cabbage", "Carrot"]
ExampleCombinePlus3 = ExampleCombinePlus + ExampleCombinePlus2
print(ExampleCombinePlus3)

# Another way is to use append()
ExampleCombineAppend = [1, 2, 3, 4, 5]
ExampleCombineAppend2 = ["Potato", "Advocado", "Lettuce", "Cabbage", "Carrot"]
for x in ExampleCombineAppend:
  ExampleCombineAppend2.append(x)
print(ExampleCombineAppend2)

# The last way is to use the extend() functiom
ExampleCombineExtend = [1, 2, 3, 4, 5]
ExampleCombineExtend2 = ["Potato", "Advocado", "Lettuce", "Cabbage", "Carrot"]
ExampleCombineExtend.extend(ExampleCombineExtend2)
print(ExampleCombineExtend)

# The last lesson has all the methods that I have already touched is great
print(" ")


print("Thirty-first lesson") # The thirty-first lesson teaches about if else statements
# if statements are important to check if a condition is met or not
# if else and elif statements are used to check multiple conditions
# This is going to be one of my last tutorials follows then I will be creating a a master document for all my knowledge

# if statements are used to check if a condition is met or not from using mathimatical and logical operators.
a = 22
b = 22
c = 44
if a < b: 
    print("b is greater than a")
# Elif is a second check one the first one is false
elif a > b:
    print("a is greater than b")
# Else is the last check if none is true. This is a 'if not then' code
else:
    print("EQUALITY")

# You can make the if statment 1 line if there is just 1 statement
if a == b: print("EQUAL")

# You can also make a if statement and an else statment 
print("Sure it's bigger") if a > b else print("NO")

# You can use 'and' to add more conditions
if a == b and c == a*2: print("Wow exact")

# You can use 'or' to have even more conditions
if a < b or a == c: print("Yaya")

# You can use 'not' to clasifty if it doesn't comply
if not a < b:
    print("no")

# If there is an if statement in an if statement, its called nested if statements 
if a == 21:
    print(1)
    if b == 23:
        print(2)
    else:
        print("bannana")

# If you need an if statement but without it finished just add pass without getting an error
if a == c:
    pass
print(" ")


print("Thirty-second lesson") # The thirty-second lesson teaches about the match statment

# The match statement is to write long lines of if stamtents quickly
Day = 6
match Day:
    case 1:
        print("Sad day")
    case 2:
        print("Sad day")
    case 3:
        print("Sad day")
    case 4:
        print("Sad day")
    case 5:
        print("Sad day")
    case 6:
        print("Fun day")
    case 7:
        print("Fun day")
    case 8 | 9 | 10 | 11: # Combines mutiple values with '|'
        print("HUH?")
    case _:
        print("Confusing day") # This is the default case if none of the cases match

# You can make it even more confusing by adding if statements
Month = 10
Day = 27
match Day:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if Month == 6:
        print("June")

    case 8 | 9 | 10 | 11 | 12 if Month == 7:
        print("July")

    case 13 | 14 | 15 | 16 | 17 | 18 | 19 if Month == 8:
        print("August")
        
    case 20 | 21 | 22 | 23 | 24 | 25 | 26 if Month == 9:
        print("September")
        
    case 27 | 28 | 29 | 30 | 31 if Month == 10:
        print("October")
    case _:
        print("Confusing month")

# This code is acutally really useful and fun to use
print(" ")


print("Thirty-third lesson") # The thirty-third lesson teaches about while loops and for loops

# Loops are used to repeat a block of code multiple times until a condition is met or not met
# There are 2 types of loops, while loops and for loops

# While loops are used to repeat a piece of code until a condition is met or not met
a = 1
while a < 10:
    print(a)
    a += 1
print(" ")

# You can use if statmentas with this using 'break'
b = 1
while b < 5:
    print(b)
    if b == 2:
        print("LOL")
        break
    b += 1
print(" ")

# You can use the continue command to skip a number
c = 0
while c < 7:
    c += 1
    if c == 5:
        continue
    print(c)
print(" ")
 # You can use else statements to run code until a contition is no longer met
d = 5
while d > 2:
    print(d)
    d -= 1
else:
    print("NO")
print(" ")

# For loops are used to execute a set of statments for each value in a list
HackyPeople1 = ["Acon", "Amber", "Alexren", "Rowan"]
for x in HackyPeople1:
    print(x)
print(" ")

# You can use the break statment to stop the code when a condition is made
for x in HackyPeople1:
    print(x)
    if x == "Alexren":
        print("Alexren Cool")
        break
print(" ")

# You can do this in a way to show a end message too
for x in HackyPeople1:
    print(x)
    if x == "Alexren":
        break
    print("and")
print(" ")

# Like in the while loop, if use use continue with the for loop it will skip over the value
for x in HackyPeople1:
    if x == "Alexren":
        continue
    print(x)
print(" ")

# You can also print out each value of a number range
for x in range(6):
    print(x)
print(" ")
for x in range(2, 6): # This gives a range '2 - 6/5'
    print(x)
print(" ")
# Basically what ever you can do with range

# You can also use else statments in this
for x in range(1, 101):
    print(x)
else:
    print("Download complete")
print(" ")
# For and whiles loops are pretty similar so most features can corrispond to both.

# You can also use nested lists
Descriptive = ["Favourful", "Long", "Juicy"]
Fruits1 = ["Mango", "Banana", "Strawberry"]

for x in Descriptive:
    for y in Fruits1:
        print(x, y)
# This is like mutiplying nuber but with string
# for every values in Decriptive they trigger every values for the Fruits1
# There is also a pass statement the everyone I already knew
print(" ")


print("Thirty-fourth lesson") # The thirty-fourth lesson teaches about functions
# Functions is my last lesson that I'm going through
# I don't think I've learnt everything I'll need to use, but I recon I've learnt most of the basics

# Functions are a group of code where it runs when used
# it can look into data in parameters to use

def my_function(): # defineds function's name
    print("Hello, from a function") # code inside function

my_function() # runs code inside function
# Functions are just like variables but for code
print(" ")

# You can add arguments which is basiaclly making a sentence and adding the value last
def GreatPeople(GPN):
    print(GPN + " is a good person")

GreatPeople("Alexren")
GreatPeople("Acon")
GreatPeople("Niko")
print(" ")

# You can add multiple arguments too
def GoodPeople2(FFN, FLN):
    print(FFN + FLN + " is a good person")

GoodPeople2("Alex", "ren")
GoodPeople2("Ac", "on")
GoodPeople2("Ni", "ko")
print(" ")

# If you don't know how many arguments there is going to be you can use *

def GoodPeople3(*Person):
  print(Person[random.randrange(0, 2)] + " is a good person")

GoodPeople3("Alexren", "Acon", "Niko")
print(" ")
# I also used a random function for fun

# This uses keywords
def GoodPeople4(P1, P2, P3):
    print(P2 + " is a human ")
GoodPeople4(P1 = "Qincai",P2 = "Koji", P3 = "Valen" )
print(" ")

# If you don't know how many key words there is going to be, you can use **
def GoodPeople5(**Person):
    print(Person["P1"] + " is a human")
GoodPeople5(P1 = "Ruby", P2 = "Kyle")
print(" ")

# You can also have a default value argument
def Countries(country = "earth"):
    print("I'm from " + country)
Countries("Aisa")
Countries("Oceania")
Countries()
print(" ")

# You can pass lists as arguments too
def ListVeg(Veggies):
    for x in Veggies:
        print(x)
Vegs = ["Carrot", "Lettuce", "Onion"]
ListVeg(Vegs)

# You can also return numbers with functions
def numbers(x):
    return x * 5

print(numbers(81))
print(numbers(9))
print(numbers(0.43))

# As again, if you don't have any instuctions but sitll want to keep it you can use pass

