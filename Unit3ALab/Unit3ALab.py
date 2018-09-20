def schools():
    print ("Bellarmine")
    print ("Python")


def agestuff():
    age = input("How old are you?")
    schoolyears = (int(age) - 6)
    print ("You've been in school for " + str(schoolyears) + " years")


def yourcitygrade(city, grade):
    print ("You're from " + city)
    print ("You're in " + str(grade) + " grade")

from random import *

def randomNumbers():
    x = input("Choose 1 number")
    y = input("Choose one more number")
    myNumber = randint(int(x), int(y))
    print (str(myNumber) + " is a random number between")
    print (str(x) + " and " + str(y))


def boxArea():
    x = input("What's the length of the box?")
    y = input("What's the width of the box?")
    area = (int(x) * int(y))
    print ("The area equals " + str(area) + "cm^2")
    return(area)


def boxPerim():
    x = input("Enter the same length for the box")
    y = input("Enter the same width for the box")
    perim = (int(x) * 2 + int(y) * 2)
    print ("The perimeter of the box is " + str(perim))
    return(boxPerim)



schools()
agestuff()
yourcitygrade("Tacoma", int(12))
randomNumbers()
boxArea()
boxPerim()
