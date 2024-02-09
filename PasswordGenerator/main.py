import random

# lista di caratteri - caracter list
Characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    Caratteri = input("numero caratteri: ") # chiede il numero di carateri - asks for the lenght of the password

    if not Caratteri.isdigit():    # controlla se la variabile lenght è un int senno fa vedere un errore - checks if the "lenght" variable is not int and displays error
        print("metti un numero e non una stringa")
        input("premi invio per riprovare")

    else:    # se non c'è errore trasforma la variabile in int - if there is no error it turns the caracter into int type
        Caratteri = int(Caratteri)
        break

# crea la variabile vuota a cui dopo si aggiungeranno i caratteri - creates the variable that characters will be added to
Password = ""

for i in range(caratteri):
    Password += random.choice(characters)    # crea e agginge caratteri alla variabile password - creates and adds characters to the password variable

print(Password)

input("premi invio per chiudere il programma")
