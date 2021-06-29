def draw(size, board1):
    # print("printing board")
    iter = 0
    for r in range(size):
        for c in range(size):
            print("|", end=''),
            print(board1[iter], end=''),
            iter += 1
        print("|", end='')
        print()


def checkwin(board2):
    # podzielone dla czytelności
    if board2[0] == board2[1] == board2[2] or board2[3] == board2[4] == board2[5] or board2[6] == board2[7] == board2[
        8]:  # poziom
        return True
    elif board2[0] == board2[3] == board2[6] or board2[1] == board2[4] == board2[7] or board2[2] == board2[5] == board2[
        8]:  # pion
        return True
    elif board2[0] == board2[4] == board2[8] or board2[2] == board2[4] == board2[6]:  # ukos
        return True
    else:
        return False


def computer_Move(board, xo2, isalt, isfirst):
    iter = 0
    count = 0
    eval = [None] * 9
    board3 = [None] * 9
    # moveS = 'X'
    for r in range(9):
        board3[r] = board[r]
    if xo2:
        moveS = 'X'
    else:
        moveS = 'O'
    for i in board3:
        if isinstance(board3[iter], int):
            count += 1
            board3[iter] = moveS
            win = checkwin(board3)
            # print(win)
            if not win:
                eval[iter] = computer_Move(board3, not xo2, not isalt, False)
            elif win and isalt:
                return -1
            elif win and isfirst:
                return iter
            elif win:
                return 1
            board3[iter] = iter + 1
        iter += 1
    # print(count)
    # print(eval)
    if count == 0:  # cała plansza zapełniona i remis
        return 0
    else:
        # wybranie odpowiednich wartości
        min = 2
        max = -2
        licznik2 = 0
        for i in eval:
            if isinstance(i, int):
                if i < min:
                    min = i
                    # minl = licznik2
                if i > max:
                    max = i
                    maxl = licznik2
            licznik2 += 1
        # zwrócenie odpowiedniego ruchu
        if isfirst:
            return maxl
        if isalt:
            return min
        else:
            return max


if __name__ == "__main__":

    # Ogólna inicjalizacja
    board = []
    size = 3
    licznik = 1
    for r in range(size*size):
        board.append(r+1)
        #licznik += 1
    gameStop = False
    xo = True  # true - ruch x, false - ruch o

    print("Czy chcesz zaczynac gre? Tak - 1, Nie - 2")
    dec = int(input())
    if dec == 1:
        comp = False
    else:
        comp = True
    draw(size, board)

    # Petla główna
    while (not gameStop):
        if (not comp):
            print("Podaj numer pola:", end='')
            move = int(input())
            comp = True
        else:
            move = computer_Move(board, xo, False, True) + 1
            print("computer:", end='')
            print(move)
            comp = False
        if (xo):
            board[move - 1] = 'X'
        else:
            board[move - 1] = 'O'
        xo = not xo
        draw(size, board)
        gameStop = checkwin(board)
        gameStop = True
        for i in range(size*size):
            if isinstance(board[i], int):
                gameStop = False

    print("Koniec gry", end='')
