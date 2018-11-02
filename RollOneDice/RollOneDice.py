import random

def main():
    setofdice = [0] * 6
    setofdice = define()
    printdice(setofdice)
    #print (setofdice)
    mydice = [0] * 2
    for i in range(0,2):
        roll = rolldice()
        mydice[i] = setofdice[roll]
        #print (mydice[i])

    printdice(mydice)




def define():
   dice = [0] * 6
   top = ' ------ '
   blank = '|       |'
   onedot1 = '| *     |'
   onedot2 = '|   *   |'
   onedot3 = '|     * |'
   twodot1 = '|  * *  |'

   for num in range (0,6):
        if num == 0:
            dice[num] = [top,blank,onedot2,blank,top]
        elif num == 1:
            dice[num] = [top,blank,twodot1,blank,top]
        elif num == 2:
            dice[num] = [top,onedot1,onedot2,onedot3,top]
        elif num == 3:
            dice[num] = [top,twodot1,blank,twodot1,top]
        elif num ==4:
            dice[num] = [top,twodot1,onedot2,twodot1,top]
        else:
            dice[num] = [top,twodot1,twodot1,twodot1,top]

   return dice


def rolldice():
    dicenum = random.randint(0,5)
    return dicenum

def printdice(randDice):
    print ('print dice')
    for row in range(0,len(randDice[0])):
        for col in range (0, len(randDice)):
            print (randDice[col][row], end = '\t')
        print()





main()
