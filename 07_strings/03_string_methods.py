#----------------------------------------------upper() Method---------------------------------------------------------

a = "Hello, World!"#Makes all the letters in uppercase
print(a.upper())

b= "12345"
print(b.upper())

#----------------------------------------------lower() Method---------------------------------------------------------

a = "Hello, World!"#Makes all the letters in lowercase
print(a.lower())

#----------------------------------------------strip() Method---------------------------------------------------------
a = " Hello, World! "
print(a.strip()) # removes white spaces returns "Hello, World!"

a = "Hello, World!"  #Replaces the word
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "HELLO WORLD!"
print(a.capitalize()) #Converts the first character to upper case

a = "HELLO WORLD!"
print(a.casefold()) #Converts string into lower case

a = "HELLO WORLD!"
print(a.center(50)) #Returns a centered string

a = "HELLO WORLD!"
print(a.center(50, "W")) #Returns a centered string

a = "HELLO WORLD!"
print(a.count("L")) #Returns the number of times a specified value occurs in a string

txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

txt = "My name is Stale" #Returns an encoded version of the string
print(txt.encode())

txt = "Hello, welcome to my world." #Returns True or False if the string is present in sentence or not
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "H\te\tl\tl\to" #The expandtabs() method sets the tab size to the specified number of whitespaces.
x = txt.expandtabs(5)
print(x)

txt = "Hello, welcome to my world." #Finds the index where that word starts from
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world." #Finds the index where that word starts from if not present will give -1
x = txt.find("akhil") #Index throws error if that is not present
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e") #Where in the text is the first occurrence of the letter "e"?:
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

txt = "For only {price:.2f} dollars!" #The format() method formats the specified value(s) and insert them inside the string's placeholder.
print(txt.format(price=49))


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

txt = "Hello, welcome to my world. welcome" #finds the first occurrence of the specified value.
x = txt.index("welcome")
print(x)

try:
    txt = "Hello, welcome to my world. welcome" #finds the first occurrence of the specified value.
    x = txt.index("akhil")
    # x = txt.index("e")
    # txt.index("e", 5, 10)
    print(x)
except Exception as ex:
    print("Word entered is not present")

#----------------------------------------------isalnum() Method---------------------------------------------------------
txt = "Company12" #returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
txt2 = "@"
x = txt.isalnum()
y = txt2.isalnum()
print(x)
print(y)

#----------------------------------------------isalpha() Method---------------------------------------------------------
txt = "CompanyX" #returns True if all the characters are alphabet letters (a-z).
txt2 = "abc10"
x = txt.isalpha()
y = txt2.isalpha()
print(x)
print(y)

#----------------------------------------------isascii() Method---------------------------------------------------------
txt = "Company123" #method returns True if all the characters are ascii characters American Standard Code for Information Interchange
txt2 = "?"
x = txt.isascii()
y = txt2.isascii()
print(x)
print(y)

#----------------------------------------------isdecimal() Method---------------------------------------------------------
txt = "\u0033" #unicode for 3
txt2 = "akhil"
txt3 = "0.2"
x = txt.isdecimal() #method returns True if all the characters are decimals (0-9).
y = txt2.isdecimal()
z = txt3.isdecimal()
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(x)
print(y)
print(z)
print(a.isdecimal())
print(b.isdecimal())

#----------------------------------------------isdigit() Method---------------------------------------------------------
txt = "50800" #method returns True if all the characters are digits, otherwise False.
txt2 = "akhil"
x = txt.isdigit()
y = txt2.isdigit()
print(x)
print(y)

#----------------------------------------------isidentifier() Method---------------------------------------------------------
txt = "Demo" #method returns True if the string is a valid identifier, otherwise False.
x = txt.isidentifier()
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#----------------------------------------------islower() Method---------------------------------------------------------
txt = "hello world!" #method returns True if all the characters are in lower case, otherwise False.
txt2 = "Akhil"
print(txt.islower())
print(txt2.islower())
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())

#----------------------------------------------isnumeric() Method---------------------------------------------------------

#method returns True if all the characters are numeric (0-9), otherwise False.
#Exponents, like ² and ¾ are also considered to be numeric values.
#"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
txt = "565543"
txt2 = "akhil"
print(txt.isnumeric())
print(txt2.isnumeric())
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

#----------------------------------------------isprintable() Method---------------------------------------------------------
print("_________________")
txt = "Hello! Are you #1?" #method returns True if all the characters are printable, otherwise False.
txt2 = "Hello!\nAre you #1?"
print(txt.isprintable())
print(txt2.isprintable())

#----------------------------------------------isspace() Method---------------------------------------------------------
txt = "   " #method returns True if all the characters in a string are whitespaces, otherwise False.
print(txt.isspace())
print("".isspace())
print("akhil is a good boy".isspace())

#----------------------------------------------istitle() Method---------------------------------------------------------
txt = "Hello, And Welcome To My World!"
#method returns True if all words in a text start with a upper case letter,
# AND the rest of the word are lower case letters, otherwise False.
print(txt.istitle())
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#----------------------------------------------isupper() Method---------------------------------------------------------
#The isupper() method returns True if all the characters are in upper case, otherwise False.
#Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "THIS IS NOW!"
txt2 = "Akhil"
a = "Hello World!"
b = "hello 123"
print(txt.isupper())
print(txt2.isupper())
print(a.isupper())
print(b.isupper())

#----------------------------------------------join() Method---------------------------------------------------------
#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
print(myDict)

#----------------------------------------------ljust() Method---------------------------------------------------------
txt = "banana" #method will left align the string, using a specified character (space is default) as the fill character.
x = txt.ljust(50)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.ljust(20, "O")
print(x)

#----------------------------------------------lstrip() Method---------------------------------------------------------
txt = "     banana     "#The lstrip() method removes any leading characters (space is the default leading character to remove)
print("of all fruits", txt.lstrip(), "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

#----------------------------------------------maketrans() Method---------------------------------------------------------
#The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

#----------------------------------------------partition() Method---------------------------------------------------------
"""The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
The first element contains the part before the specified string.
The second element contains the specified string.
The third element contains the part after the string."""
txt = "I could eat bananas all day bananas"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

#----------------------------------------------replace() Method---------------------------------------------------------
#The replace() method replaces a specified phrase with another specified phrase.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

#----------------------------------------------rfind() Method---------------------------------------------------------
"""
The rfind() method finds the last occurrence of the specified value.
The rfind() method returns -1 if the value is not found.
The rfind() method is almost the same as the rindex() method. See example below.
"""

txt = "Mi casa, su casa."
print(txt.rfind("casa"))

txt = "Hello, welcome to my world."
print(txt.rfind("e"))

txt = "Hello, welcome to my world."
print(txt.rfind("e",5,10))
print(txt.rfind("q"))

#----------------------------------------------rindex() Method---------------------------------------------------------
"""
The rindex() method finds the last occurrence of the specified value.
The rindex() method raises an exception if the value is not found.
The rindex() method is almost the same as the rfind() method. See example below.
"""
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

#----------------------------------------------rjust() Method---------------------------------------------------------
#The rjust() method will right align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.rjust(5)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.rjust(20, "O")
print(x)

#----------------------------------------------rpartition() Method---------------------------------------------------------
"""
The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
The first element contains the part before the specified string.
The second element contains the specified string.
The third element contains the part after the string.
"""
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

#----------------------------------------------rsplit() Method---------------------------------------------------------
"""
The rsplit() method splits a string into a list, starting from the right.
If no "max" is specified, this method will return the same as the split() method.
"""

txt = "apple, banana, cherry"
x = txt.rsplit(",")
print(x)

txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

#----------------------------------------------rstrip() Method---------------------------------------------------------
#The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

#----------------------------------------------split() Method---------------------------------------------------------
"""
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
"""
txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

#----------------------------------------------splitlines() Method---------------------------------------------------------
#The splitlines() method splits a string into a list. The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

#----------------------------------------------startswith() Method---------------------------------------------------------
#The startswith() method returns True if the string starts with the specified value, otherwise False.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

#----------------------------------------------strip() Method---------------------------------------------------------
"""
The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters 
(space is the default leading character to remove)
"""
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

#----------------------------------------------swapcase() Method---------------------------------------------------------
#The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#----------------------------------------------title() Method---------------------------------------------------------
"""
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
If the word contains a number or a symbol, the first letter after that will be converted to upper case.
"""
txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "Welcome to my 2nd world"
x = txt.title()
print(x)

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)

#----------------------------------------------zfill() Method---------------------------------------------------------
"""
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
If the value of the len parameter is less than the length of the string, no filling is done.
"""
txt = "50"
x = txt.zfill(10)
print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))