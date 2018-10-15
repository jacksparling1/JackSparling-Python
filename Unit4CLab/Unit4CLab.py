def draw7():
    for i in range (0,8):
        for i in range (0,8):
            print ('*', end = ' ')
        print()


#draw7()

def starsandstripes():
    for i in range (0,1):
        for i in range (0,8):
            print ('*', end = ' ')
        print()
    stripes()


def stripes():
    for i in range (0,1):
        for i in range (0,8):
            print ('-', end = ' ')
        print()
    starsandstripes()




starsandstripes()
stripes()



