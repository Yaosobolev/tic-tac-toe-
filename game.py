class Game:
    def __init__(self, id):
        self.player = 0
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.player_turn = 0
        self.p1_played = False
        self.p2_played = False

    def get_player_turn(self):
        return self.player_turn
    
    def set_move(self, player, row, col):
        self.moves[player] = (row, col)
        if self.player_turn == 0:
            print("внутренний ход игрока :")
            self.player_turn = 1
        else:
            self.player_turn = 0

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, moves):
        """Handle a player's move."""
        print("вернитесь сюда")
        row, col = moves
        # Assuming `clicked_btn` and `send_play` are defined elsewhere in your code.
        # if (clicked_btn['text'] == ""):
        #     if (player == 1):
        #         player = 2
        #         clicked_btn['text'] = 'X'
        #         send_play(row, col)

    def connected(self):
        return self.ready

    def restart_game(self):
        """Сбросьте игру в исходное состояние."""
        self.player = 0
        self.ready = False
        self.moves = [None, None]
        self.player_turn = 0
        self.p1_played = False
        self.p2_played = False
        print("Игра перезапущена")