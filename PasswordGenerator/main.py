import random

# lista di caratteri
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# chiede il numero di caratteri desiderati e riprova a chiedere se l'input non è un numero
while True:
    caratteri = input("numero caratteri: ")

    if not caratteri.isdigit():
        print("metti un numero e non una stringa")
        input("premi invio per riprovare")

    else:
        caratteri = int(caratteri)
        break

# crea la variabile vuota a cui dopo si aggiungeranno i caratteri
password = ""

for i in range(caratteri):
    password += random.choice(characters)

print(password)

input("premi invio per chiudere il programma")