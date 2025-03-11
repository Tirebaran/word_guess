import random
import os

def guessing(secret, letter, word):
    index = 0
    places = []
    for i in secret:
        if i == letter:
            places.append(index)
        index += 1
    for j in places:
        word = word[0:j] + letter + word[j + 1:]
    if len(places):
        return [word, 1]
    else:
        return [word, 0]

word_bank = ["word", "apple", "book", "sun", "river", "table", "cat", "music", "wind", "window", "flower", "road", "cup", "star", "night", "morning", "rain", "song", "city", "sea", "forest", "fire", "snow", "friend", "happiness", "time", "life", "dream", "work", "school", "house", "hand", "leg", "head", "eye", "ear", "mouth", "nose", "heart", "soul", "thought", "word", "number", "letter", "paper", "pencil", "wall", "door", "window", "light", "shadow", "air"]
g_word = random.choice(word_bank)
a_word = "_" * len(g_word)
attempt = 10
alp = "abcdefghijklmnopqrstuvwxyz"
alp_n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Secret word:", "_ " * len(g_word))

while a_word != g_word and attempt != 0:
    answer = input("Guess a letter: ")
    while not(answer in alp) or answer in alp_n: 
        print("This letter cannot be entered!")
        answer = input("Enter a letter again: ")
    os.system("cls")
    if not(guessing(g_word, answer, a_word)[1]):
        attempt -= 1
        print("No such letters!")
    else:
        print("Success!")
    a_word = guessing(g_word, answer, a_word)[0]
    print("Secret word: ", end="")
    for i in a_word: print(i, end=" ")
    print("\nAttempts left:", attempt, "\n")
    alp = alp.replace(answer, alp_n[alp.index(answer)])
    for i in alp:print(i + " ", end="")

if a_word == g_word:
    print("Congratulations! The word has been guessed!")
else: 
    print("Out of attempts! The word was:", g_word)