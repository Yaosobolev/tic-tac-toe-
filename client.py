import pickle
import time
from tkinter import *
import socket
import os
from socket import *


"""
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
"""
wind = Tk()
wind.geometry("400x400")
greeting = Label(text="Добро пожаловать!", font=('Helvetica', '15'))
waiting_lb = Label(text="Ожидание другого игрока!...", font=('Helvetica', '15'))
player_turn_lb = Label(text="Ход противника", font=('Helvetica', '15'))
your_turn_lb = Label(text="Твой ход", font=('Helvetica', '15'))

host = '127.0.0.1'
port = 7228
s = socket(AF_INET, SOCK_STREAM)

_cells = {}
buttons = []
moves = []

def switch_turn(player_turn):

    if player_turn == 0:
        if player == 0:
            player_turn_lb.grid_forget()
            your_turn_lb.grid(row=6, column=6)
        if player == 1:
            your_turn_lb.grid_forget()
            player_turn_lb.grid(row=6, column=6)

    else :
        if player == 0:
            your_turn_lb.grid_forget()
            player_turn_lb.grid(row=6, column=6)
        if player == 1:
            player_turn_lb.grid_forget()
            your_turn_lb.grid(row=6, column=6)


def send_play(row, col):
    s.send(str.encode("\n".join([str(row), str(col)])))

def play(event) :
    global moves
    global  player_turn
    
    clicked_btn = event.widget
    row, col = _cells[clicked_btn]

    if (clicked_btn['text'] == "" and clicked_btn["state"] == NORMAL):
        print("ana player :" , player)
        #print(" player turn :", player_turn)
        print("player_turn",game.player_turn)
        if ((player == 0) and (game.player_turn == 0)):
            clicked_btn['text'] = 'O'

        elif((player == 1) and (game.player_turn == 1)):
            clicked_btn['text'] = 'X'

        s.send(str.encode("\n".join([str(row), str(col)])))

    wind.update()
def winner(the_winner):

    result_lb = Label( font=('Aerial 17 bold italic'))
    result_lb.grid (row=3, column=3, sticky="ne")
    if the_winner == 'O':
        result_lb["text"]=("the winner is player O" )
    elif the_winner == 'X':
        result_lb["text"]=("the winner is player X" )
    else :
        result_lb["text"] = "Tie game"

# def restart_game_request():
#     # Это пример функции, которая отправляет запрос на перезапуск игры на сервер
#     # Замените "RESTART_CODE" на код или сообщение, которое ваш сервер понимает как запрос на перезапуск
#     s.send(str.encode("RESTART_GAME"))

# # Добавление кнопки перезапуска игры в интерфейс
# restart_button = Button(master=wind, text="Перезапустить игру", bg="blue", fg="white", command=restart_game_request)
# restart_button.grid(row=5, column=3, padx=10, pady=5, sticky="nsew")
        

def check():
    btn_1 = list(filter(lambda x: _cells[x] == (1, 1), _cells))[0]
    btn_2 = list(filter(lambda x: _cells[x] == (1, 2), _cells))[0]
    btn_3 = list(filter(lambda x: _cells[x] == (1, 3), _cells))[0]
    btn_4 = list(filter(lambda x: _cells[x] == (2, 1), _cells))[0]
    btn_5 = list(filter(lambda x: _cells[x] == (2, 2), _cells))[0]
    btn_6 = list(filter(lambda x: _cells[x] == (2, 3), _cells))[0]
    btn_7 = list(filter(lambda x: _cells[x] == (3, 1), _cells))[0]
    btn_8 = list(filter(lambda x: _cells[x] == (3, 2), _cells))[0]
    btn_9 = list(filter(lambda x: _cells[x] == (3, 3), _cells))[0]

    if (btn_1["text"] != '')\
            and((btn_1["text"] == btn_2["text"] == btn_3["text"] ) \
            or (btn_1["text"] == btn_4["text"]  == btn_7["text"])\
            or (btn_1["text"] == btn_5["text"]  == btn_9["text"])) :
        winner(btn_1["text"])
    elif (btn_4["text"] != '') and (btn_4["text"] == btn_5["text"] == btn_6["text"]) :
        winner(btn_4["text"])
    elif (btn_7["text"] != '') and (btn_7["text"] == btn_8["text"] == btn_9["text"]) :
        winner(btn_7["text"])
    #if (btn_1["text"] == btn_4["text"]  == btn_7["text"]) :
    #    return btn_1
    elif (btn_2["text"] != '') and (btn_2["text"] == btn_5["text"]  == btn_8["text"]) :
        winner(btn_2["text"])
        print("her here 2 5 8")
    elif (btn_3["text"] != '') \
            and ((btn_3["text"] == btn_6["text"]  == btn_9["text"])\
            or (btn_3["text"] == btn_5["text"]  == btn_7["text"]) ):
        winner(btn_3["text"])
    elif (btn_1["text"] != "" and btn_2["text"] != "" and btn_3["text"] != "" \
          and btn_4["text"] != ""and btn_5["text"] != "" and btn_6["text"] != ""\
          and btn_7["text"] != ""and btn_8["text"] != "" and btn_9["text"] != ""):

        winner("tiegame")



def create_board_grid( game, player):
    lb1 = Label(wind, text="Client :bla bla", font=('Helvetica', '15'))
    p = player
    p = str(int(p)+1)
    wind.title("You are player :"+ p)
    #greeting.destroy()
    if not (game.connected()) :
        #print("In disconnected")

        #button_frame.grid_forget()
        waiting_lb.grid(row=4, column=2, sticky="ne")
    else:
        waiting_lb.grid_remove()
        greeting.grid_remove()
        button_frame.grid(row =3, column= 2)
        lb1 = Label(wind, text="Client :bla bla", font=('Helvetica', '15'))
        #print("_cells :" , _cells)
        """"""
        for btn in _cells:
            row, col = _cells[btn]
            btn.grid(
                row=row,
                column=col,
                padx=5,
                pady=5,
                sticky="nsew"
            )
        
            if ((player == '1') and (game.player_turn == 0)) or ((player == '0') and (game.player_turn == 1)):
                btn["state"] = DISABLED
                switch_turn(game.player_turn)
            if ((player == '0') and (game.player_turn == 0)) or ((player == '1') and (game.player_turn == 1)):
                btn["state"] = NORMAL
                switch_turn(game.player_turn)



            btn.bind("<ButtonPress-1>", play)

        player0_move = game.get_player_move(0)
        player1_move = game.get_player_move(1)

        if player0_move:
            key_btn = list(filter(lambda x: _cells[x] == player0_move, _cells))[0]
            key_btn.config(text="O", bg="green")
        if player1_move:
            key_btn = list(filter(lambda x: _cells[x] == player1_move, _cells))[0]
            key_btn.config(text="X", bg="yellow")

        if player1_move or player0_move:
            check()
    wind.update()



def main():
    run = True
    print('ожидание ответа на соединение')
    global player
    global game
    try:
        s.connect((host, port))
    except s.error as e:
        print(str(e))
    res = s.recv(10)
    player = res.decode()
    while run:

        try:
            #game = n.send("get")
            s.send(str.encode("get"))
            #print("send game :")
            data = s.recv(10 * 60)
            #print("data :", data)
            game =pickle.loads(data)

            #print("recived * 10 :", game)
            btn.grid_forget()
            greeting.grid(row=4, column=2, sticky="se")
        
        except:
            run = False
            print("Не удалось получить игру")
            """
            for w in wind.winfo_children():
                w.grid_forget()
            btn.grid(row=3,
                     column=3,
                     padx=18,
                     pady=5,
                     sticky="nsew")
            """
            break

        create_board_grid(game, player)

btn = Button(
    master=wind,
    text="Подключиться к серверу!",
    width=15,
    height=5,
    bg="purple",
    fg="yellow",
    command=main
)
btn.grid(row=3,
             column=3,
             padx=18,
             pady=5,
             sticky="nsew")
button_frame = Frame(wind)
button_frame.grid(row=1, column=2)
for row in range(1, 4):

   for col in range(1, 4):
       button = Button(
           master=button_frame,
           text="",
           font=('Helvetica', '15'),  # (size=36, weight="bold"),#,
           bg="cornsilk2",
           fg="black",
           width=3,
           height=1  # ,
           # highlightbackground="lightblue",
       )
       _cells[button] = (row, col)



wind.mainloop()




