game_Map = {'0-0': '0','0-1': '1','0-2': '2','0-3': '3',
            '1-0': '1','1-1': '-','1-2': '-','1-3': '-',
            '2-0': '2','2-1': '-','2-2': '-','2-3': '-',
            '3-0': '3','3-1': '-','3-2': '-','3-3': '-'}
currentTurn = 0

def clearGameMap():
    global game_Map
    global currentTurn
    game_Map = {'0-0': '0', '0-1': '1', '0-2': '2', '0-3': '3',
                '1-0': '1', '1-1': '-', '1-2': '-', '1-3': '-',
                '2-0': '2', '2-1': '-', '2-2': '-', '2-3': '-',
                '3-0': '3', '3-1': '-', '3-2': '-', '3-3': '-'}
    currentTurn = 0
    print("НАЧАЛО ИГРЫ КРЕСТИКИ-НОЛИКИ!")
    showGameField()

def stepTurn():
    global currentTurn
    currentTurn += 1

def showGameField():
    gameField = ""
    for x in range(0, 4):

        if (x > 0):
            print(gameField)
            gameField = ""
        for y in range(0, 4):
            key = "{xx}-{yy}".format(xx=x, yy=y)
            gameField = gameField + game_Map[key]
    #        print("VALUE OF ", key, " IS ", game_Map[key])
    print(gameField)

def makeKey(x,y):
    return "{xx}-{yy}".format(xx=x, yy=y)

def makeTurn(x, y, symbol):
    if (game_Map[makeKey(x, y)] == "-"):
        game_Map[makeKey(x, y)] = symbol
        showGameField()
        return True
    else:
        print("В данном месте уже сделан ход, походите в другое место")
        return False

def checkVictory():
    if ((game_Map["1-1"] == game_Map["1-2"]) and (game_Map["1-1"] == game_Map["1-3"] and (game_Map["1-1"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["2-1"] == game_Map["2-2"]) and (game_Map["2-1"] == game_Map["2-3"] and (game_Map["2-1"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["3-1"] == game_Map["3-2"]) and (game_Map["3-1"] == game_Map["3-3"] and (game_Map["3-1"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["1-1"] == game_Map["2-1"]) and (game_Map["1-1"] == game_Map["3-1"] and (game_Map["1-1"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["1-2"] == game_Map["2-2"]) and (game_Map["1-2"] == game_Map["3-2"] and (game_Map["1-2"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["1-3"] == game_Map["2-3"]) and (game_Map["1-3"] == game_Map["3-3"] and (game_Map["1-3"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["1-1"] == game_Map["2-2"]) and (game_Map["1-1"] == game_Map["3-3"] and (game_Map["1-1"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    elif ((game_Map["1-3"] == game_Map["2-2"]) and (game_Map["1-3"] == game_Map["3-1"] and (game_Map["1-3"] != "-"))):
        print("ПОБЕДИЛ ИГРОК ", getTurnSide())
        return True
    else:
        return False

def startGame():
    clearGameMap()
    while (True):
        stopGame = False
        print("ХОДИТ ИГРОК ", getTurnSide())
        x = input("Введите номер ряда (1-3) ")
        y = input("Введите номер столбца (1-3) ")

        if ((x not in range(1, 3) or (y not in range(1, 3)))):
            print("Некорректный ввод данных для хода")
            continue

        if makeTurn(int(x), int(y), getTurnSide()):

            if (checkVictory()):
                while (True):
                    answer = input("Играть еще раз? Y - ДА, N - НЕТ ")
                    if (answer in ["y", "Y"]):
                        clearGameMap()
                        break
                    elif (answer in ["n", "N"]):
                        print("СПАСИБО ЗА ИГРУ!")
                        stopGame = True
                        break
                    else:
                        print("Неверный ввод ответа.")
                        continue
            else:
                stepTurn()
                continue

            if (stopGame):
                break

def getTurnSide():
    global currentTurn
    if (currentTurn % 2 == 0):
        return "X"
    else:
        return "0"

startGame()