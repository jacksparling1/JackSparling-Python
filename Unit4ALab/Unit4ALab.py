
def main():
    print ("Type random letters!")
    letters = input(str())
    print (letters)
    deVowel(letters)
    print (deVowel(letters))

def deVowel(letters):
    print (letters)
    letters2 = ""
    for let in letters:
        if let !='a' and let !='e' and let !='i' and let !='o' and let !='u':
            letters2 = letters2 + let

    return letters2









main()
