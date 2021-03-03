#HANGMAN v.02

import random
print("Let's play HANGMAN!!!!")
with open("list.txt","r") as file:
    words = file.readlines()
length = len(words)


index = random.randint(0,length+1)
word = words[index]
guessword = '_'*(len(word)-1)

chance = 7
    
for index in range(0,len(word)-1):
    print(guessword[index], end = ' ')
print("\n")

print("You have 7 chances to guess the word!!")

while chance != 0:
    letter = input("Please guess a letter: ").lower()
    if letter in word:
        for index in range(0,len(word)):
            if word[index] == letter:
                guessword = guessword[:index] + letter + guessword[index+1:]
    else:
        chance = chance - 1
        if chance ==6:
            print("You are H")
        if chance ==5:
            print("You are HA")
        if chance ==4:
            print("You are HAN")
        if chance ==3:
            print("You are HANG")
        if chance ==2:
            print("You are HANGM")
        if chance ==1:
            print("You are HANGMA")
        if chance ==0:
            print("You are HANGMAN")
        
    for index in range(0,len(word)-1):
        print(guessword[index], end = ' ')
    print('\n')

    if guessword != word:
        print("you have", chance, "chances left")
    if guessword == word:
        print("You won!!")
        break
    else:
        continue
    
if guessword!=word:
    print('''You ran out of turns.
Better luck next time :)''')
