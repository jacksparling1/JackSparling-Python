
def main():
    numbGrade = int(input("What grade are you in?"))
    #print (yearinschool(numbGrade))
    longyear = (yearinschool(numbGrade))
    print (longyear)
    myList = [91.5, 88.1, 99.8, 93.4]
    getNumber= (gpa(myList))
    print (getNumber)
    theNumber = (letterGrade(getNumber))
    print (theNumber)



def yearinschool(grade):
    if (grade)==12:
        year = ("You're a Senior")
    elif (grade)==11:
        year = ("You are a Junior")
    elif (grade)==10:
        year = ("You are a Sophmore")
    elif (grade)==9:
        year = ("You are a Freshman")
    else:
        year = ("You arent in high school")
    return (year)


def gpa(myList):
    #print (len(myList))
    if (len(myList))==4:
        results = (myList[0] + myList[1] + myList[2] + myList[3]) / (len(myList))
    elif (len(myList))==5:
        results = (myList[0] + myList[1] + myList[2] + myList[3]) + myList[4] / (len(myList))
    elif (len(myList))==6:
        results = (myList[0] + myList[1] + myList[2] + myList[3]) + myList[4] + myList[5] / (len(myList))
    return (results)

def letterGrade(getNumber):
    if (getNumber)>=90:
        letter = ("You're getting an A")
    elif (getNumber)>=80:
        letter = ("You're getting an B")
    elif (getNumber)>=70:
        letter = ("You're getting an C")
    elif (getNumber)>=60:
        letter = ("You're getting an D")
    else:
        letter = ("You're failing :(")
    return (letter)




main()



