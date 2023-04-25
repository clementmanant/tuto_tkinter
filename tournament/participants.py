from tkinter import *
from tkinter import ttk
import numpy as np

root = Tk()

class participants:
    datas = []
    pseudo = StringVar()
    ville = StringVar()
    charactervar = StringVar()
    select = Listbox()

    def __init__(self, root):
        root.title("Smash Tournament")
        
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        Label(mainframe, pady="5", text = 'Pseudo', font='arial 12 bold').grid(column=1, row=1, sticky=(W, E))
        Entry(mainframe, textvariable = self.pseudo,width=50).grid(column=2, row=1, sticky=(W))

        Label(mainframe, pady="5", text = 'Ville', font='arial 12 bold').grid(column=1, row=2, sticky=(W, E))
        Entry(mainframe, textvariable = self.ville,width=50).grid(column=2, row=2, sticky=(W))

        Label(mainframe, pady="10", text = 'Personnage', font='arial 12 bold').grid(column=1, row=3, sticky=(W, E))
        character = ttk.Combobox(mainframe, textvariable=self.charactervar)
        character['values'] = self.get_characters()
        character.state(["readonly"])
        character.grid(column=2, row=3, sticky=(W, E))

        Button(mainframe,text="Add",font="arial 12 bold",command=self.add).grid(column=1, row=4, sticky=(W, E))
        Button(mainframe,text="View",font="arial 12 bold",command=self.view).grid(column=1, row=5, sticky=(W, E))
        Button(mainframe,text="Delete",font="arial 12 bold",command=self.delete).grid(column=1, row=6, sticky=(W, E))
        Button(mainframe,text="Delete all",font="arial 12 bold",command=self.delete_all).grid(column=1, row=7, sticky=(W, E))
        Button(mainframe,text="Reset",font="arial 12 bold",command=self.reset).grid(column=1, row=8, sticky=(W, E))

        self.select = Listbox(mainframe)
        self.select.grid(column=2, row=4, rowspan=5, sticky=(N, W, E, S))
        scroll_bar = Scrollbar(mainframe, orient=VERTICAL, command=self.select.yview)
        scroll_bar.grid(column=3, row=4, rowspan=5, sticky=(N, S, W))
        self.select['yscrollcommand'] = scroll_bar.set

    def add(self):
        if (np.size(self.datas) > 64 * 3):
            print("Nombre Max atteint")
            return None
        self.datas.append([self.pseudo.get(),self.ville.get(),self.charactervar.get()])
        self.update_book()

    def view(self):
        self.pseudo.set(self.datas[int(self.select.curselection()[0])][0])
        self.ville.set(self.datas[int(self.select.curselection()[0])][1])
        self.charactervar.set(self.datas[int(self.select.curselection()[0])][2])

    def delete(self):
        del self.datas[int(self.select.curselection()[0])]
        self.update_book()

    def delete_all(self):
        self.datas = []
        self.update_book()

    def reset(self):
        self.pseudo.set('')
        self.ville.set('')
        self.charactervar.set('')

    def update_book(self):
        self.select.delete(0,END)
        for n in self.datas:
            self.select.insert(END, n)

    def get_characters(self):
        return ('Mario', 'Donkey Kong', 'Link', 'Samus', 'Dark Samus', 'Yoshi', 'Kirby', 'Fox', 'Pikachu', 'Luigi', 'Ness', 'Captain Falcon', 'Jigglypuff', 'Peach', 'Daisy', 'Bowser', 'Ice Climbers', 'Sheik', 'Zelda', 'Dr. Mario', 'Pichu', 'Falco', 'Marth', 'Lucina', 'Young Link', 'Ganondorf', 'Mewtwo', 'Roy', 'Mr. Game & Watch', 'Meta Knight', 'Pit', 'Dark Pit', 'Zero Suit Samus', 'Wario', 'Snake', 'Ike', 'Pokémon Trainer', 'Diddy Kong', 'Lucas', 'Sonic', 'King Dedede', 'Olimar', 'Lucario', 'R.O.B', 'Toon Link', 'Wolf', 'Villager', 'Mega Man', 'Wii Fit Trainer', 'Rosalina & Luma', 'Little Mac', 'Greninja', 'Palutena', 'Pac-Man', 'Robin', 'Shulk', 'Bowser Jr.', 'Duck Hunt', 'Ryu', 'Ken', 'Cloud', 'Corrin', 'Bayonetta', 'Inkling', 'Ridley', 'Simon', 'Richter', 'King K. Rool', 'Isabelle', 'Incineroar', 'Piranha Plant', 'Joker', 'Hero', 'Banjo & Kazooie', 'Terry', 'Byleth', 'Min Min', 'Steve', 'Sephiroth', 'Pyra/Mythra', 'Kazuya', 'Sora', 'Mii Brawler', 'Mii Swordfighter', 'Mii Gunner', 'Random')


participants(root)
root.mainloop()