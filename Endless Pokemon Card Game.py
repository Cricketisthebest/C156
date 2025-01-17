from tkinter import*
from PIL import ImageTk, Image
root = Tk()
root.title("Endless Pokemon Card Game")
root.geometry("600x400")

root.configure(background="cyan")

img = ImageTk.PhotoImage(Image.open(""))

player1 = Label(root, text="Player 1", bg="blue", fg="white")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text="Player 2", bg="blue", fg="white")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player1_score_label = Label(root, bg="blue", fg="white")
player1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score_label = Label(root, bg="blue", fg="white")
player2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

random_pokemon_label = Label(root, bg="green", fg="black")
random_pokemon_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()