def greeting():
    print("===================")
    print("  Добро пожаловать ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("===================")
    print("   Правила игры:"   )
    print("Для выбора ячейки введите ")
    print("координаты ячейки в формате: x y ")
    print("где,")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show_field():
    print()
    print("      0   1   2   ")
    print()
    for i, row in enumerate(field):
        row_str = f"  {i}   {' | '.join(row)}   "
        print(row_str)
        if i < 2:
            print("     ------------ ")
    print()


def ask_player():
    while True:
        cords = input("      Сделайте ход: ").split()
        if len(cords) != 2:
            print(" Требуется 2 координаты! ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" Клетка уже занята! ")
            continue
        return x, y


def check_winner():
    win_line = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_line:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print()
            print("Выиграл крестик!!! Поздравляем!")
            return True
        if symbols == ["0", "0", "0"]:
            print()
            print("Выиграл нолик!!! Поздравляем! ")
            return True
    return False


def start():
    greeting()
    count = 0
    while True:
        count += 1
        show_field()
        if count % 2 == 1:
            print(" Ход крестика!")
        else:
            print(" Ход нолика!")
        x, y = ask_player()
        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"
        if check_winner():
            break
        if count == 9:
            print()
            print(" Игра окончена. Ничья!")
            break

field = [[" "] * 3 for i in range(3)]

start()