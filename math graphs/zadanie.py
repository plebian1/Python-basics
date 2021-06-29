import tkinter
import tkinter.ttk as ttk
import sys
import requests
import requests.exceptions
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

def rysuj():
    wykres.cla()
    t = np.arange(float(poczx.get()), float(koniecx.get()), .01)
    x = Symbol('x')
    tekst = funkcjatext.get()
    tabtekst = tekst.split(';')
    symtab = []
    for i in range(len(tabtekst)):
        wart = tabtekst[i]
        symtab.append(parsing.sympy_parser.parse_expr(wart))


    for j in symtab:
        tab = []
        for i in t:
            tab.append(j.subs(x,i))
        wykres.plot(t, tab[:], label = str(j))

    wykres.set_ylabel(etykietaytext.get())
    wykres.set_xlabel(etykietaxtext.get())
    wykres.grid()
    wykres.legend()
    canvas.draw()
    toolbar.update()

class Okno(Frame):
    def __init__(self,master = None):
        window = tkinter.Tk()
        window.geometry("1000x600")

        Tytul = tkinter.Label(window, text="Kalkulator wykresów")
        Tytul.pack(side=tkinter.TOP)

        funkcjatextlabel = tkinter.Label(window, text="funkcja f(x):")
        funkcjatextlabel.place(x=700, y=80)

        funkcjatext = tkinter.Entry(window)  # Pole do wprowadzania danych
        funkcjatext.place(x=700, y=100)

        dodajBut = tkinter.Button(window, text="+", )
        dodajBut.place(x=700, y=150)

        minusBut = tkinter.Button(window, text="-", )
        minusBut.place(x=720, y=150)

        razyBut = tkinter.Button(window, text="*", )
        razyBut.place(x=740, y=150)

        dzielBut = tkinter.Button(window, text="/", )
        dzielBut.place(x=760, y=150)

        nawias1But = tkinter.Button(window, text="(", )
        nawias1But.place(x=700, y=200)

        nawias2But = tkinter.Button(window, text=")", )
        nawias2But.place(x=720, y=200)

        # Opisy wykresu

        tytullabel = tkinter.Label(window, text="Tytul rysynku:")
        tytullabel.place(x=20, y=20)

        tytulrys = tkinter.Entry(window)  # Pole do wprowadzania danych
        tytulrys.place(x=100, y=20, width=90)

        # OŚ X
        poczx = tkinter.Entry(window)  # Pole do wprowadzania danych
        poczx.place(x=100, y=40, width=30)

        koniecx = tkinter.Entry(window)  # Pole do wprowadzania danych
        koniecx.place(x=160, y=40, width=30)

        osx = tkinter.Label(window, text="OŚ X od:")
        osx.place(x=45, y=40)

        dox = tkinter.Label(window, text="Do:")
        dox.place(x=135, y=40)

        etykietax = tkinter.Label(window, text="etykieta:")
        etykietax.place(x=200, y=40)

        etykietaxtext = tkinter.Entry(window)
        etykietaxtext.place(x=250, y=40, width=50)

        # OŚ Y
        poczy = tkinter.Entry(window)  # Pole do wprowadzania danych
        poczy.place(x=100, y=60, width=30)

        koniecy = tkinter.Entry(window)  # Pole do wprowadzania danych
        koniecy.place(x=160, y=60, width=30)

        osy = tkinter.Label(window, text="OŚ Y od:")
        osy.place(x=45, y=60)

        doy = tkinter.Label(window, text="Do:")
        doy.place(x=135, y=60)

        etykietax = tkinter.Label(window, text="etykieta:")
        etykietax.place(x=200, y=60)

        etykietaytext = tkinter.Entry(window)
        etykietaytext.place(x=250, y=60, width=50)

        # rysowanie
        tabnazw = []
        rysujBut = tkinter.Button(window, text="rysuj", command=rysuj)
        rysujBut.place(x=720, y=300)

        fig = Figure(figsize=(5, 4), dpi=100)
        wykres = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
        # canvas.draw() #wywołanie rysowania
        canvas.get_tk_widget().place()  # toolbar

        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.NONE)  # wykres

        # koniec
        exitBut = tkinter.Button(window, text="Zakoncz Program", command=sys.exit)
        exitBut.place(x=700, y=500)


if __name__ == '__main__':
    a = Okno()
    a.mainloop()



