from tkinter import *
import random
from PIL import ImageTk, Image


#global devant une variable = instruction Python qui l'informe que la variable a 
# qui est utilisée à l'intérieur de la fonction est la même 
# que celle qui est définie à l'extérieur de la fonction

def next_turn(row, column): #Fonction pour le tour par tour des joueurs

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]: 

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"), bg="#343434", fg="light grey") #Annonce le tour du joueur

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"), bg="#343434", fg="light grey") #Annonce le gagnant

            elif check_winner() == "Tie": 
                label.config(text="Tie!", bg="#343434", fg="light grey") #Annonce un tie

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False: 
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():#Fonction pour verifie si il y a un gagnant

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="light green") #Configure la couleur du background
            buttons[row][1].config(bg="light green")
            buttons[row][2].config(bg="light green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="light green")
            buttons[1][column].config(bg="light green")
            buttons[2][column].config(bg="light green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="light green")
        buttons[1][1].config(bg="light green") 
        buttons[2][2].config(bg="light green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="light green")
        buttons[1][1].config(bg="light green")
        buttons[2][0].config(bg="light green")
        return True

    elif empty_spaces() is False: #Si tout est rempli, alors ca renvoie sur un tie.

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="aqua") #change la couleur du background en cas de tie
        return "Tie"

    else:
        return False


def empty_spaces(): #Verifie si il y a des emplacements libre

    spaces = 9

    for row in range(3): #boucle qui permet de verifie que le button n'est pas vide, il enleve 1 dans le compteur 
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game(): #Fonction pour une nouvelle parti

    global player
    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#343434", fg="light grey")


window = Tk()
window.title("Tic-Tac-Toe") #Nom de la fenetre
window.config(bg = "#343434")
players = ["X","O"]
player = random.choice(players)#Choisi un joueur au hasard dans la liste
buttons = [[0,0,0], 
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " Turn", font=('calibri',60), bg="#343434", fg="light grey") #Permet d'inserer un texte ou une image 
label.pack(side="bottom") #Ou se situe la box 

reset_button = Button(text="Restart", font=('calibri',30),padx = 186, command=new_game, bg="#343434", fg="light grey")
reset_button.pack(side="top")#Position du bouton

frame = Frame(window, relief=FLAT)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('calibri',40), bg="#343434", fg="black", width=6, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()