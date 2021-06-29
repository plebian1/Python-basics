import tkinter
import sys
from sympy import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np





def rysuj():
    """Funkcja modifkująca pole wykresu, pobiera wzory z pola na ekranie po czym tworzy na jego podstwie wykresy."""
    wykres.cla()
    logtab = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    t = np.arange(float(poczx.get()), float(koniecx.get()), .01)
    x = Symbol('x')
    tekst = funkcjatext.get()
    tabtekst = tekst.split(';')
    # Jeżeli dziedzina jest źle dobrana, program nie zadziała, dla nieskończoności działa kontrowersyjnie
    if tekst != '':
        symtab = []
        for i in range(len(tabtekst)):
            wart = tabtekst[i]
            symtab.append(parsing.sympy_parser.parse_expr(wart))


        k = 0
        for j in symtab:
            if k>4 or logtab[k] == 0:
                tab = []
                for i in t:
                    tab.append(j.subs(x,i))
                wykres.plot(t, tab[:], label = str(k+1) + '. '+ str(j))
                wykres.legend()

            k+=1

    wykres.set_ylabel(etykietaytext.get())
    wykres.set_xlabel(etykietaxtext.get())
    wykres.grid()
    wykres.set_title(tytulrys.get())

    wykres.set_xlim([float(poczx.get()), float(koniecx.get())])
    wykres.set_ylim([float(poczy.get()), float(koniecy.get())])

    canvas.draw()
    toolbar.update()
    return

def klawtekst(tekst):
    """Funkcja do wstawiania tekstu do pola tekstu funkcji przez przyciski na ekranie"""
    a = funkcjatext.get()
    dlug = len(a)
    funkcjatext.insert(dlug,tekst)
    return

def wyczysc():
    """Funkcja czyszcząca pole tekstu funkcji"""
    a = funkcjatext.get()
    dlug = len(a)
    funkcjatext.delete(0,dlug)
    return

#Ogólnie to znowu raczej kiepsko z obiektowością tego, no ale większość rzeczy działa bez zarzutu
if __name__ == '__main__':
    """ W main są rozmieszczane wszystkie pola tekstowe, opisy, przyciski, pole do rysowania wykresu itd.
    Podłączone są także funkcjonalności do przycisków i zainicjaliozwe jest pole wykresu."""
    window = tkinter.Tk()
    window.geometry("850x600")

    Tytul = tkinter.Label(window, text="Kalkulator wykresów")
    Tytul.pack(side=tkinter.TOP)

    funkcjatextlabel = tkinter.Label(window, text="funkcja f(x):")
    funkcjatextlabel.place(x=700, y=80)

    funkcjatext = tkinter.Entry(window)  # Pole do wprowadzania funkcji
    funkcjatext.place(x=700, y=100)



    #Przyciski
    dodajBut = tkinter.Button(window, text="+", command =lambda:klawtekst("+"))
    dodajBut.place(x=700, y=130)

    minusBut = tkinter.Button(window, text="-", command =lambda:klawtekst("-") )
    minusBut.place(x=720, y=130)

    razyBut = tkinter.Button(window, text="*", command =lambda:klawtekst("*"))
    razyBut.place(x=740, y=130)

    dzielBut = tkinter.Button(window, text="/", command =lambda:klawtekst("/"))
    dzielBut.place(x=760, y=130)

    nawias1But = tkinter.Button(window, text="(", command =lambda:klawtekst("("))
    nawias1But.place(x=700, y=160)

    nawias2But = tkinter.Button(window, text=")", command =lambda:klawtekst(")"))
    nawias2But.place(x=720, y=160)

    sinbut = tkinter.Button(window, text="sin", command=lambda: klawtekst("sin()"))
    sinbut.place(x=700, y=190)

    cosbut = tkinter.Button(window, text="cos", command=lambda: klawtekst("cos()"))
    cosbut.place(x=730, y=190)

    wyczyscBut = tkinter.Button(window, text="wyczysc ", command=lambda:wyczysc())
    wyczyscBut.place(x=700, y=220)

    # Opisy wykresu

    tytullabel = tkinter.Label(window, text="Tytul rysynku:")
    tytullabel.place(x=20, y=20)

    tytulrys = tkinter.Entry(window)  # Pole do wprowadzania danych
    tytulrys.place(x=100, y=20, width=90)

    #check boxy, niestety zakodowany jakby to ująć statycznie, więc działa tylko do 5 wykresów dalej by trzeba było dorobić

    var1 = tkinter.IntVar()
    check1 = tkinter.Checkbutton(window, text="wykres 1", variable=var1, onvalue = 0, offvalue = 1)
    check1.place(x=500,y=200)

    var2 = tkinter.IntVar()
    check2 = tkinter.Checkbutton(window, text="wykres 2", variable=var2, onvalue = 0, offvalue = 1)
    check2.place(x=500, y=220)

    var3 = tkinter.IntVar()
    check3 = tkinter.Checkbutton(window, text="wykres 3", variable=var3, onvalue=0, offvalue = 1)
    check3.place(x=500, y=240)

    var4 = tkinter.IntVar()
    check4 = tkinter.Checkbutton(window, text="wykres 4", variable=var4, onvalue=0, offvalue = 1)
    check4.place(x=500, y=260)

    var5 = tkinter.IntVar()
    check5 = tkinter.Checkbutton(window, text="wykres 5", variable=var5, onvalue=0, offvalue = 1)
    check5.place(x=500, y=280)



    # OŚ X
    poczx = tkinter.Entry(window)  # Pole do wprowadzania danych
    poczx.place(x=100, y=40, width=30)
    poczx.insert(0,-5)

    koniecx = tkinter.Entry(window)  # Pole do wprowadzania danych
    koniecx.place(x=160, y=40, width=30)
    koniecx.insert(0,5)

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
    poczy.insert(0,-5)

    koniecy = tkinter.Entry(window)  # Pole do wprowadzania danych
    koniecy.place(x=160, y=60, width=30)
    koniecy.insert(0,5)

    osy = tkinter.Label(window, text="OŚ Y od:")
    osy.place(x=45, y=60)

    doy = tkinter.Label(window, text="Do:")
    doy.place(x=135, y=60)

    etykietax = tkinter.Label(window, text="etykieta:")
    etykietax.place(x=200, y=60)

    etykietaytext = tkinter.Entry(window)
    etykietaytext.place(x=250, y=60, width=50)

    # rysowanie
    rysujBut = tkinter.Button(window, text="rysuj", command=rysuj)
    rysujBut.place(x=650, y=100)

    fig = Figure(figsize=(5, 4), dpi=100)
    wykres = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.get_tk_widget().place()  # toolbar

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.NONE)  # wykres
    rysuj()

    #koniec
    exitBut = tkinter.Button(window, text="Zakoncz Program", command=sys.exit)
    exitBut.place(x=700, y=300)

    window.mainloop()
