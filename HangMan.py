import random
words = [ "UMBRELLA", "COMPUTER", "JAKE","ELLE"]
# f = open("words.txt", "r")
# data = f.readline()
# words = data.split
# word = random.choice(words)
# word = word.upper()
# make a txt file (words.txt) where diff words are stored

word = random.choice(words)
total_chances = 7
guessed_word = "_" * len (word)

while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]== letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
            if guessed_word == word:
                print("Congrats you won!!!")
                print("The word is ")
                break
    else:
        total_chances -= 1
        print("Incoreect guess")
        print("You only have", total_chances, "chances")
else:
        print("Game Over")
        print("You Lost!!")
        print("No more chances")
        print("The correct word is "+word)

