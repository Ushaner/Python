import random

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#probably a better way to define the alphabet, search up later.
name = input("What is your name: ")
Difficulty = int(input("Number of Letter Count: "))
tries = Difficulty*2//1.2
word = []

for i in range(Difficulty):
    word.append(Letters[random.randint(0, (len(Letters)-1))])
    
print(word)
print(tries)