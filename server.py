import socket
from socket import *
from _thread import *
import pickle
from game import Game


server = '127.0.0.1'
port = 7228

s = socket(AF_INET, SOCK_STREAM)

try:
    s.bind((server, port))
except s.error as e:
    str(e)

s.listen(5)
print("Ожидание соединения, сервер запущен")

games = {}
ThreadCount = 0


def threaded_client(conn, p, gameId):
    global ThreadCount
    conn.send(str.encode(str(p)))
    print("Игрок : ", p)

    reply = ""
    while True:
        try:

            data = conn.recv(10).decode()
            if(('\n') in data):
                row, col = [int(i) for i in data.split('\n')]
            if (data != "get"):
                print("от игррока :", p)
            if gameId in games:
                game = games[gameId]

                if not data:
                    print("Нет данных, тогда перерыв здесь : ", data)
                    break
                else:
                    if data == "reset":
                        game.resetWent()

                    elif (data != "get") :
                        game.set_move(p, row, col)
                
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Потеряно соединение с игроком", p)
    try:
        del games[gameId]
        print("Закрытие игры", gameId)
    except:
        pass
    ThreadCount -= 1
    print("Кол-во потоков",ThreadCount)
    conn.close()

while True:
    conn, address = s.accept()
    print('Подключен к: ' + address[0] + ':' +str(address[1]))

    ThreadCount += 1
    p = 0
    gameId = (ThreadCount - 1)//2
    if ThreadCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Создание новой игры...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))