import pygame
import pygame_menu
import time
import random
import sys
from os import path

#To jest od zmieniania "trudności"
def set_speed(value,cos):
    if value[1] == 1:
        tabtrue[1] = False
    else:
        tabtrue[1] = True


def set_box(value,cos):

    if value[1] == 1:
        tabtrue[0]= False
    else:
        tabtrue[0] = True


#Funckaj do wyświetlania wiadomości na ekranie
def message(msg, color):
    surface.fill(white)
    mesg = pygame.font.SysFont(None, 50).render(msg, True, color)
    surface.blit(mesg, [int(width / 4), int(height / 2) - 60])


def start_the_game(lives,highscore,menu):
    a = menu.get_input_data()
    for key, value in a.items():
        nazwa = value
    # pozycja startowa
    xpoz = int(width / 2)
    ypoz = int(height / 2)

    # snake, już po napisaniu programu myślę to to by lepiej wyglądało jako obiekt klasy
    snakesize = 20
    body = []
    length = 1
    head = pygame.Rect(xpoz, ypoz, snakesize, snakesize)

    # Udawany wektor prędkości, startuje nie ruszając się
    xmove = 0
    ymove = 0

    # tempo gry, regulowane timerem
    clock = pygame.time.Clock()
    tempo = tempstart

    # startowa pozycja jedzenia
    foodx = round(random.randrange(0, width - snakesize) / snakesize) * snakesize
    foody = round(random.randrange(0, height - snakesize) / snakesize) * snakesize
    food = pygame.Rect(foodx, foody, snakesize, snakesize)


    if lives > 0 :
        game_over = False
    else:
        game_over = True
    utrata = False
    while not game_over:
        if utrata:
            surface.fill(white)
            wiadomosc = "Straciłeś życie, masz jeszcze: " + str(lives)
            message(wiadomosc, blue)
            wynik = pygame.font.SysFont(None, 30).render("Wynik: " + str(length - 1), True, green)
            surface.blit(wynik, [0, 0])
            pygame.display.update()
            time.sleep(2)
            #Poprawianie najlepszego wyniku
            if length - 1 > highscore:
                highscore = length - 1
            start_the_game(lives,highscore,menu)
            game_over = True


        if lives > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if xmove != snakesize or length == 1 or xmove == 0:
                            xmove = -snakesize
                            ymove = 0
                    elif event.key == pygame.K_RIGHT:
                        if xmove != -snakesize or length == 1 or xmove == 0:
                            xmove = snakesize
                            ymove = 0
                    elif event.key == pygame.K_UP:
                        if ymove != snakesize or length == 1 or ymove == 0:
                            xmove = 0
                            ymove = -snakesize
                    elif event.key == pygame.K_DOWN:
                        if ymove != -snakesize or length == 1 or ymove == 0:
                            xmove = 0
                            ymove = snakesize

            head.x += xmove
            head.y += ymove
            # Sprawdzanie kolizji ze ścianą
            if tabtrue[0]:
                if head.x >= width or head.x < 0 or head.y >= height or head.y < 0:
                    lives += -1
                    utrata = True
            # Wychodzenie po drugiej stronie
            else:
                if head.x >= width:
                    head.x += -width
                elif head.x < 0:
                    head.x += width
                elif head.y >= height:
                    head.y += -height
                elif head.y < 0:
                    head.y += height

            # dodajemy głowę do miejsc do narysowania
            tabsnake = []
            tabsnake.append(head.x)
            tabsnake.append(head.y)
            body.append(tabsnake)
            # usuwamy ostatni element, żeby nie był już rysowany
            if len(body) > length:
                del body[0]

            # Sprawdzamy czy głowa nie styka się z resztą ciała (:-1, bo ostatnia jest sama głowa)
            for i in body[:-1]:
                if i == tabsnake:
                    lives += -1
                    utrata = True

            # jedzenie

            if head.x == food.x and head.y == food.y:
                eat.play()
                foodx = round(random.randrange(0, width - snakesize) / snakesize) * snakesize
                foody = round(random.randrange(0, height - snakesize) / snakesize) * snakesize
                length += 1
                if tabtrue[1]:
                    tempo += 1
            food = pygame.Rect(foodx, foody, snakesize, snakesize)

            # rysowanie
            surface.fill(white)
            # jedzenie
            pygame.draw.rect(surface, red, food)
            for i in body:
                pygame.draw.rect(surface, black, [i[0], i[1], snakesize, snakesize])
            # wyświetlanie wyniku
            wynik = pygame.font.SysFont(None, 30).render("Wynik: " + str(length -1), True, green)
            surface.blit(wynik, [0, 0])
            #wyświetlanie żyć
            zycia = pygame.font.SysFont(None, 30).render("Życia: " + str(lives), True, green)
            surface.blit(zycia, [0, 20])

            pygame.display.update()
            clock.tick(tempo)
        # tutaj ląduję po przegraniu
        else:
            lose.play()
            message("GAME OVER", red)
            pygame.display.update()
            time.sleep(4)
            highestscore = "Twój najlepszy wynik to : " + str(highscore)
            message(highestscore , red)
            pygame.display.update()
            time.sleep(2)
            game_over = True


            highscoretab.append([nazwa,highscore])
            f = open("wyniki.txt", "w+")
            for listitem in highscoretab:
                    f.writelines('%s' % listitem[0] + ', %s\n' % listitem[1])
            f.close


def zasady():
    petla = True
    while petla:
        surface.fill(orange)
        tekst = pygame.font.SysFont(None, 30).render(("Poruszanie strzałkami "), True, black)
        surface.blit(tekst, [10, 20])
        tekst = pygame.font.SysFont(None, 30).render(("Zjadanie czerwonych kwadratów powiększa węża "), True, black)
        surface.blit(tekst, [10, 45])
        tekst = pygame.font.SysFont(None, 30).render(("Escape kończy grę i cofa do menu"), True, black)
        surface.blit(tekst, [10, 70])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    petla = False
        pygame.display.update()
    pass



def config():
    menu2 = pygame_menu.Menu(height, width, 'Snake', theme=pygame_menu.themes.THEME_ORANGE, onclose= pygame_menu.events.BACK)
    menu2.add_selector('Zmiana szybkości po jedzeniu:', [('Tak', 1), ('Nie', 2)], onchange=set_speed)
    menu2.add_selector('Ściany zabijają:', [('Tak', 1), ('Nie', 2)], onchange=set_box)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                petla = False
    menu2.mainloop(surface)


def wyniki():
    petla = True

    #sortowanie wyników
    for i in highscoretab:
        for j in range(len(highscoretab)-1):
            if int(highscoretab[j][1]) < int(highscoretab[j+1][1]):
                tempint = int(highscoretab[j][1])
                tempnazw = highscoretab[j][0]
                highscoretab[j][1] = int(highscoretab[j+1][1])
                highscoretab[j][0] = highscoretab[j+1][0]
                highscoretab[j + 1][1] = tempint
                highscoretab[j + 1][0] = tempnazw

    oklaski.play()
    while petla:
        surface.fill(orange)
        k = 0
        for i in highscoretab:
            wynik = pygame.font.SysFont(None, 30).render("Wynik " + i[0] +" to:" +str(i[1]), True, green)
            surface.blit(wynik, [int(width/3), 25*k])
            k+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    petla = False
        pygame.display.update()





def autor():
    petla = True
    while petla:
        surface.fill(orange)
        wynik = pygame.font.SysFont(None, 30).render(("Autor: Jędrzej Piątek"), True, black)
        surface.blit(wynik, [10, 20])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    petla = False
        pygame.display.update()


def main_menu(lives):
    # High score
    highscore = 0
    menu = pygame_menu.Menu(height, width, 'Snake', theme=pygame_menu.themes.THEME_ORANGE, onclose= pygame_menu.events.EXIT)
    menu.add_text_input('Nazwa gracza:', default='Gall Anonim')
    menu.add_button('Start gry', lambda: start_the_game(lives,highscore,menu))
    menu.add_button('Zasady gry', zasady)
    menu.add_button('Konfiguracja', lambda: config())
    menu.add_button('Najlepsze wyniki', wyniki)
    menu.add_button('O autorze', autor)
    menu.add_button('Zakończ program', pygame_menu.events.EXIT)
    menu.mainloop(surface)


if __name__ == '__main__':

    sound_dir = path.dirname(__file__)
    sound_dir = sound_dir +'/sounds'
    #kolory
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    orange = (255,165,0)

    pygame.init()
    pygame.mixer.init()

    #dźwięki
    a = sound_dir +'/applause4.wav'
    oklaski = pygame.mixer.Sound(a)
    oklaski.set_volume(0.25)

    # źródło następnych dwóch https://opengameart.org/content/snake-sprites-sound
    b = sound_dir + '/eat.ogg'
    eat = pygame.mixer.Sound(b)
    eat.set_volume(0.1)
    
    a = sound_dir + '/lose.ogg'
    lose = pygame.mixer.Sound(a)
    lose.set_volume(0.1)

    # rozdzielczość ekranu
    width = 800
    height = 600
    surface = pygame.display.set_mode((width, height))
    # zmienna odpowiedzialna za to czy są ściany czy ich nie ma
    box = True
    # ilość żyć
    lives = 3
    # tempo startowe, zmiana tempa po zjedzeniu
    tempstart = 10
    tempchange = True
    #trochę szkoda gadać, ale przez to że nie robię tego poprawnie obiektowo to zmienne odpowiedzialne za konfigurację, musze przechowywać w tablicy
    tabtrue = [box,tempchange]
    #tablica wyników
    highscoretab = []
    #Dodanie wyników zapisanych w pliku
    f = open("wyniki.txt", "r")
    filecontents = f.readlines()
    for line in filecontents:
        a = line.split(',')
        b = a[1].split('\n')
        highscoretab.append([a[0],b[0]])

    main_menu(lives)
