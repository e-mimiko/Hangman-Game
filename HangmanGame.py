# This is the Hangman game. The purpose of this program is to mimick the Hangman
# game. User will guess the letters in the word, and they have no more than 6
# tries or the computer wins.

import random

def getWords():
    Hangmanwords=open("Hangmanwords.txt","r")
    words=Hangmanwords.readlines()
    for i in range(len(words)):
        words[i] = words[i].rstrip("\n")
    Hangmanwords.close()
    return words

def Welcome():
    response=input ("WELCOME TO HANGMAN!\nWOULD YOU LIKE TO PLAY? YES/NO: ")
    return response

def play():
    YesOrNo=Welcome()
    if YesOrNo == "Yes":
        Hangman()
    else:
        print ("You chose NO, come back again, Bye!")

def Hangman():
    words=getWords()
    word=random.choice(words)
    soloLetters=list(word)
    hang=list("-" * len(word))
    i=1
    print ("THIS WORD HAS ", len(word), " LETTERS")
    while i <= 6 and hang != list(word):
        print("\nThis is your",i,"of 6th tries")
        letter=input("\nGuess a letter!: ")
        if letter in soloLetters:
            position=soloLetters.index(letter)
            hang[position]=letter
            print()
            print(hang)
            soloLetters[position]= "-"
        else:
            i+=1
    if i > 6:
        print ("GAME OVER! Sorry you used all your tries. Your word was -",
               word.upper(), "- Sorry!")
    elif hang==list(word):
        print ("YOU WIN! Your word was ", word.upper(), "!")

#Top Level
        
play()
