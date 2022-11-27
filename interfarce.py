from tkinter import *
import random
import os

class Interface():
    def __init__(self):
        self.fenetre = Tk()
        self.x = 500
        self.y = 400
        self.fenetre.geometry(f"{self.x}x{self.y}")
        self.fenetre.title("Brain Master")
        self.fenetre.configure(bg='#333333')
        self.compteur = 0
        self.compteur_score = 0
        self.score_victory = 0
        self.current_file = str(os.path.dirname(__file__)).split('dist')[0]

    def close_window(self):
        with open(self.current_file + "\\user_word.txt", "r+", encoding = 'utf-8') as wt:
            wt.truncate(0)
            wt.close()

        self.fenetre.destroy()

    def get_lenFile(self):
        with open(self.current_file + "\\user_word.txt", "r+", encoding = 'utf-8') as wt:
            len_file = len(wt.readlines()) 

        return len_file

    def delete_all(self):
        if self.compteur_score > self.score_victory:
            self.score_victory = self.compteur_score

        self.entry_text.destroy()
        self.score.destroy()
        self.button_validate.destroy()
        self.label.destroy()

        self.compteur = 0
        self.compteur_score = 0
        self.MainWindow()

        with open(self.current_file + "\\user_word.txt", "r+", encoding = 'utf-8') as wt:
            wt.truncate(0)
            wt.close()

    def keydown(self, e):
        if e.char == "+":
            self.get_word()
        
        elif e.char == "-" and self.get_lenFile() != 0:
            self.GameWindow()

    def write_text(self, word):
        with open(self.current_file + "\\user_word.txt", "a", encoding = 'utf-8') as wt:
            wt.write(f"{word}\n") 

    def get_input(self):
        word_input = self.entry_text.get()
        document_word = self.get_valeur().split("\n")[0]

        if word_input == document_word:

            self.compteur_score += 1
            self.score.config(text=self.compteur_score)
            self.entry_text.delete(0, END)

            if self.get_lenFile() == 0:
                self.delete_all()

        elif word_input != document_word:
            self.delete_all()

        else:
            self.delete_all()

    def MainWindow(self):
        self.label = Label(self.fenetre, text="Brain MASTER", fg="pink", bg='#333333', font=('Helvetica', '35'))
        self.label.pack(pady=20)

        self.Frame1 = Frame(self.fenetre, borderwidth=5, relief=GROOVE, bg='#333333')
        self.Frame1.pack(pady=60)

        self.main_text = Label(self.Frame1, text="Appuyer sur le + pour continuer", fg="white", bg='#333333', font=('Helvetica', '20'))
        self.main_text.pack()

        self.compteur_round = Label(self.fenetre, text=self.compteur, fg="pink", bg='#333333', font=('Helvetica', '40'))
        self.compteur_round.pack()

        self.victory = Label(self.fenetre, text=f"meilleur score : {self.score_victory}", fg="white", bg='#333333', font=('Helvetica', '15'))
        self.victory.pack(anchor="center")

    def GameWindow(self):
        self.Frame1.destroy()
        self.main_text.destroy()
        self.compteur_round.destroy()
        self.victory.destroy()

        self.entry_text = Entry(self.fenetre, font=("Arial",20), bg="white")
        self.entry_text.pack(pady=60)

        self.score = Label(self.fenetre, text=self.compteur_score, fg="pink", font=('Helvetica', '35'), bg='#333333')
        self.score.pack(pady=10)

        self.button_validate = Button(self.fenetre, text="Valider", fg="white", font=('Helvetica', '20'), bg='#333333', width=30,command=self.get_input)
        self.button_validate.pack()
        
    def get_word(self):
        with open(self.current_file + "\\word.txt", "r") as file:
            allText = file.read()
            words = list(allText.split())
        
            result = random.choice(words)
        
        self.main_text.config(text=result)
        self.write_text(result)
        self.compteur += 1
        self.compteur_round.config(text=self.compteur)

    def get_valeur(self):
        with open(self.current_file + "\\user_word.txt",'r+',encoding = 'utf-8') as document_word:
            first_line = document_word.readline()

            data = document_word.read() 
            document_word.seek(0) 
            document_word.write(data) 
            document_word.truncate()
      
        return first_line
        
    def Start(self):
        self.MainWindow()
        self.fenetre.bind("<KeyPress>", self.keydown)

        self.fenetre.protocol("WM_DELETE_WINDOW", self.close_window)
        self.fenetre.mainloop()

tk = Interface()
tk.Start()