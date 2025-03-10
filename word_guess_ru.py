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
        print("Удачно!")
    else:
        print("Таких букв нет!")
    return word
        

word_bank = ["слово", "яблоко", "книга", "солнце", "река", "стол", "кошка", "музыка", "ветер", "окно", "цветок", "дорога", "чашка", "звезда", "ночь", "утро", "дождь", "песня", "город", "море", "лес", "огонь", "снег", "друг", "счастье", "время", "жизнь", "мечта", "работа", "школа", "дом", "рука", "нога", "голова", "глаз", "ухо", "рот", "нос", "сердце", "душа", "мысль", "слово", "число", "буква", "бумага", "карандаш", "стена", "дверь", "окно", "свет", "тень", "воздух"]
g_word = random.choice(word_bank)
a_word = "_" * len(g_word)
attempt = 10
alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alp_n = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print("Загаданное слово:", "_ " * len(g_word))


while a_word != g_word and attempt != 0:
    answer = input("Угадай букву: ")
    while not(answer in alp) or answer in alp_n: 
        print("Такую букву нельзя вводить!")
        answer = input("Введите букву ещё раз: ")
    os.system("cls")
    
    a_word = guessing(g_word, answer, a_word)
    print("Загаданное слово: ", end="")
    for i in a_word: print(i, end=" ")
    attempt -= 1
    print("\nПопыток осталось:", attempt, "\n")
    alp = alp.replace(answer, alp_n[alp.index(answer)])
    print(alp)

if a_word == g_word:
    print("Поздравляю! Слово отгадано!")
else: 
    print("Попытки закончились! Слово было:", g_word)
    