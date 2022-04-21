#!/usr/bin/env python3

import pylab as plt
import tkinter as tk

from pylab import linspace, pi, plot,sin,cos, show,grid,legend
from os.path import basename, splitext
from tkinter import *

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Generátor funkce cosinus"

    def __init__(self):
        super().__init__(className=self.name)
        self.var_entryE = tk.IntVar()
        self.var_entryS = tk.IntVar()
        self.var_entryF = tk.IntVar()
        self.var_entryA = tk.IntVar()
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.lbl1 = tk.Label(self, text="Cosinus", font=7)
        self.lbl1.pack()

        self.lblF = tk.Label(self, text=u"Frekvence:")
        self.lblF.pack(anchor=N)

        self.entryF  = tk.Entry(self, textvariable = self.var_entryF, width = 15, justify=CENTER, borderwidth=5)
        self.entryF.pack()

        self.lblA = tk.Label(self, text=u"Amplituda:")
        self.lblA.pack(anchor=N)

        self.entryA  = tk.Entry(self, textvariable = self.var_entryA, width = 15, justify=CENTER, borderwidth=5)
        self.entryA.pack()

        self.btn3 = tk.Button(self, text="Načíst libovolný graf", command=self.graf, borderwidth= 3)
        self.btn3.pack()       

        self.btn2 = tk.Button(self, text="Načíst ze souboru", command=self.grafsoubor, borderwidth= 3)
        self.btn2.pack()

        self.btn = tk.Button(self, text="Konec", command=self.quit, borderwidth= 3)
        self.btn.pack()

    def graf(self):
        
        self.frekvence = self.var_entryF.get()
        self.amplituda = self.var_entryA.get()
        
        t = plt.linspace(1, 10/self.frekvence, self.frekvence*10000)
        x = self.amplituda * (plt.cos(2*pi*self.frekvence*t ))

        plt.plot(t,x)
        plt.title("Cosinus")
        plt.xlabel("t[s]")
        plt.ylabel("u[V]")
        plt.grid()
        plt.show()
    
        
    def grafsoubor(self):
        f = open("soubor-win.txt", "r")
        x = []
        y = []
        while 1:
            radek = f.readline()
            if radek =="":
                break
            cisla = radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        f.close()
        plt.figure()
        plt.plot(x,y)
        plt.grid(True)
        plt.show()
          
def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()
