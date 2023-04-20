"""1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.
Twinkle, twinkle, little star, How I wonder what you are" """

"""
Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. """

def answer_for_first_question():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")

answer_for_first_question()
#--------------------------------------------------------------------------------------------------------------------------------------------
"""2. Write a Python program to find out what version of Python you are using."""
def answer_for_second_question():
    import sys
    print("python version is {}".format(sys.version))

answer_for_second_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""

def answer_for_third_question():
    import datetime
    print("Present date and time is {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

answer_for_third_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""4. Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504"""

def answer_for_fourth_question(area: float):
    from math import pi
    print(pi*area**2)

answer_for_fourth_question(1.1)

#--------------------------------------------------------------------------------------------------------------------------------------------

"""5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them."""

def answer_for_fifth_question():
    frstname = str(input("Enter first name"))
    lastname = str(input("Enter last name"))
    print(lastname + " "+ frstname)

answer_for_fifth_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"""

def answer_for_sixth_question():
    my_input = input("Enter the comma seperated values")
    print("list:",my_input.split(","))
    print("tuple:",tuple(my_input.split(",")))


answer_for_sixth_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""7. Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
Sample filename : abc.java
Output : java"""

def answer_for_seventh_question():
    my_input = input("Enter the file name")
    print(my_input.rpartition(".")[-1])

answer_for_seventh_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""8. Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]"""

def answer_for_eigth_question():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0],color_list[-1])

answer_for_eigth_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014"""

def answer_for_ninth_question():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : {}/{}/{}".format(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
    print("The examination will start from : %i / %i / %i" % exam_st_date)

answer_for_ninth_question()

#--------------------------------------------------------------------------------------------------------------------------------------------

"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615"""

def answer_for_tenth_question(a: int):
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a, a))
    n3 = int("%s%s%s" % (a, a, a))
    print(n1 + n2 + n3)
answer_for_tenth_question(5)