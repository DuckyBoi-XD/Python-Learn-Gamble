print(" ")
print ("First lesson") # First lesson teaches prints messages with the command 'print' then a message in a ("_______") or ('_____').


print ("How to code? :c")
print (';-;')


print(" ")
print("Second lesson") # Second lesson teaches how to use Syntax or what I call it, 'if' statements.

if 6 < 5:
    print ("6 is greater than 5 stupid ")

# The lesson didn't really touch over 'else' statements, but from my little bit of knowledge of coding, I knew that 'else' statements were used to give a message if the 'if' statement was wrong.

else:
    print ("No, stupid")

print(" ")
print("Thrid lesson") # The third lesson teaches how to use comments with the '#' symbol, which I have use in the first 2 lessons.

print("# and the key to comments")

print(" ")
print("Forth lesson") # The fourth lesson covers on variables where we need to first assign a value to them to use it in our code.

x = 5
y = "Raymont"

# The lesson also shows how to print variables. Instead of print with ("_______"), we can just put in the variable name in (___). 

print(x)
print(y)

print(" ")
print("Fifth lesson")  # The fifth lesson teaches how to use casting to print specific data types.

x = str(7.2) # str means string which is the text of the variable, 7.2 would output as 7.2 and 'apple' would output to apple

y = int(7.2) # int mean integer which is a whole number not a decimal, 7.2 would output as 7 and 'apple' would output as an error due to it not being a number but a text

z = float(7.2) # float means (I guess) floating which means that the output number would be the exact number (I think) and not text. So, 7.2 would output as 7.2 and 'apple' would output as an error due to it not being a number but a text

print(x)
print(y)
print(z)

# When code becomes like this I like to play around with the code to potentioally make it better or break it completely.

X = 4.761 # This varible is to change all the other casting varibles quickly.

x = str(X)
y = int(X)
z = float(X)

print(x)
print(y)
print(z)

print(" ")
print("Sixth lesson") # The sixth lesson talks about how to name variables. It's important to understand how to properly name variables so errors won't occur.

myname = "Niko" # Works perfectly, all lowercase letters

myName = "Valen" # Works perfectly, first letter of second word is capitalized

MyName = "Person" # Works perfectly, first letter of every word is capitalized

my_name = "Ryan" # Works perfectly, underscores are used to separate words

myname2 = "Acon" # Works perfectly, numbers can be used in anywere in the variable's name but the start

# my name = "Niko" will cause an error due to there being a space in the variable's name

# my-name = "Valen" will cause an error due to there being a hyphen in the variable's name

# 2myname = "Ruby" will cause an error due to the variable's name starting with a number

# if = Niko will also cause an error due to 'if' being a special word in Python, as well as 'print', 'else', 'for', 'while', 'def', and many more.

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
#  
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
