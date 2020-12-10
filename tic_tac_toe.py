def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print(" выберете, за кого будете играть(x или o):")

def check():
    win = 0
    if gameTable[0][0] == gameTable[0][1] == gameTable[0][2] != '-':
        who(1, gameTable[0][1])
        return True
    elif gameTable[1][0] == gameTable[1][1] == gameTable[1][2] != '-':
        who(1, gameTable[1][1])
        return True
    elif gameTable[2][0] == gameTable[2][1] == gameTable[2][2] != '-':
        who(1, gameTable[2][1])
        return True
    elif gameTable[0][0] == gameTable[1][0] == gameTable[2][0] != '-':
        who(1, gameTable[1][0])
        return True
    elif gameTable[0][1] == gameTable[1][1] == gameTable[2][1] != '-':
        who(1, gameTable[1][1])
        return True
    elif gameTable[0][2] == gameTable[1][2] == gameTable[2][2] != '-':
        who(1, gameTable[1][2])
        return True
    elif gameTable[0][0] == gameTable[1][1] == gameTable[2][2] != '-':
        who(1, gameTable[1][1])
        return True
    elif gameTable[0][2] == gameTable[1][1] == gameTable[2][0] != '-':
        who(1, gameTable[1][1])
        return True
    elif '-' not in gameTable[0] and '-' not in gameTable[1] and '-' not in gameTable[2]:
        who(2, '-')
        return True
    else:
        return False


def who(win, cords):
    if win == 1:
        if cords == p1:
            print('---=== ПОБЕДИЛ {} ===---'.format(p1))
        elif cords == p2:
            print('---=== ПОБЕДИЛ {} ===---'.format(p2))
    elif win == 2:
        print('\t---=== НИЧЬЯ! ===---')
    else:
        pass
def x_move():
    while True:
        x = input("Ходит {}\n Введите координаты через запятую! (x, y):\n".format(p1))
        tabx = x.split(',')
        try:
            tabx[0] = int(tabx[0])
            tabx[1] = int(tabx[1])
        except:
            print("--==Неверный формат координат==--")
            continue
        try:
            if gameTable[tabx[0]][tabx[1]] == '-':
                gameTable[tabx[0]][tabx[1]] = p1
                print(
                      '\t', '0', '\t ', '1', '  ', '2', '\n',
                      '0', gameTable[0], '\n',
                      '1', gameTable[1], '\n',
                      '2', gameTable[2])
                break
            else:
                print("--==Тут уже занято. Выберете другое место.==--")
        except:
            print("--==Неверный формат координат==--")
            continue


def y_move():
    while True:
        y = input("Ходит {}\n Введите координаты через запятую! (x, y):\n".format(p2))
        taby = y.split(',')
        try:
            taby[0] = int(taby[0])
            taby[1] = int(taby[1])
        except:
            print("--==Неверный формат координат==--")
            continue
        try:
            if gameTable[taby[0]][taby[1]] == '-':
                gameTable[taby[0]][taby[1]] = p2
                print(
                    '\t', '0', '\t ', '1', '  ', '2', '\n',
                    '0', gameTable[0], '\n',
                    '1', gameTable[1], '\n',
                    '2', gameTable[2])
                break
            else:
                print("--==Тут уже занято. Выберете другое место==--")
        except:
            print("--==Неверный формат координат==--")
            continue


def game():
    print(
          '\t', '0', '\t ', '1', '  ', '2', '\n',
          '0', gameTable[0], '\n',
          '1', gameTable[1], '\n',
          '2', gameTable[2])
    while True:
        x_move()
        if check():
            break
        y_move()
        if check():
            break

greet()
p1 = input('Ходить первым будет: ')
p2 = input('Ходить вторым будет: ')

gameTable = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
game()