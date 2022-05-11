import random, sys, os, time, modules.colorama as colorama, math
from modules.colorama import (Fore, Back)
from copy import deepcopy



board = []

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
# (end)

def to_int(val, err="enter a valid option", return_val_if_err=True):
    while True:
        try:
            return int(val)
        except ValueError:
            print(err)
            if return_val_if_err:
                return val
def int_input(to_print, err="enter a valid option", return_if_err=False):
    while True:
        inp = input(to_print)
        try:
            return int(inp)
        except ValueError:
            print(err)
            if return_if_err:
                return inp


players = []

def check_slapped(slapper_id, slapped_id):
    slapper = players[slapper_id]
    slapped = players[slapped_id]
    print(slapper.is_slapping and slapped.is_ducking)
    if slapper.is_slapping and not slapped.is_ducking and slapped.is_slapped and slapped.pos > 1:
        board[slapped.id_] = ["—",]*len(board[slapped.id_])
        players[slapped_id].pos -= 2
        board[slapped.id_][slapped.pos] = slapped.character

cur_player = 0


def check_win(player):
    return board[player][-1] != "—"
def move_player(player, interval):
    players[player].pos += interval

def minimax(player, depth, alpha, beta):
    #implement the base case here
    if check_win(player):
        return (-10, None, None)
    for obj in players:
        if obj.id_ == player:
            continue
        else:
            if check_win(obj.id_):
                return (10, None, None)
    if depth == 0:
        return (0, None, None)
    
    
    
    if player == "O":
        best = -100000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "—":
                    place_player("O", row, col)
                    move_value = minimax("X", depth - 1, alpha, beta)[0]
                    alpha = max(alpha, move_value)
                    if move_value > best:
                        best = move_value
                        [optimal_row, optimal_col] = [row, col]
                    place_player("—", row, col)
                    if alpha >= beta:
                        break
        return (best, optimal_row, optimal_col)
    else:
        worst = 100000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "—":
                    place_player("X", row, col)
                    move_value = minimax("O", depth - 1, alpha, beta)[0]
                    beta = min(beta, move_value)
                    if move_value < worst:
                        worst = move_value
                        [optimal_row, optimal_col] = [row, col]
                    place_player("—", row, col)
                    if beta <= alpha:
                        break
        return (worst, optimal_row, optimal_col)


class Player:
    def __init__(self, *t, **kwargs):
        for dictionary in t:
            for key in dictionary:
                if type(key) == 'dict':
                    for attr in key:
                        setattr(self, attr, key[attr])
                else:
                    setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
        essentials = ['name', 'character', 'pos', 'is_slapping', 'is_ducking', 'is_going']
        for i in essentials:
            if not i in self.__dict__:
                print(f"missing value \'{i}\' in \'Object\'")
                # raise MissingValueError(f"missing value \'{i}\' in \'Object\'")

class User(Player):
    def __init__(self, *t, **kwargs):
        super().__init__(*t, **kwargs)
    def Move(self, depth, alpha, beta):
        action = input("""Choose an option:
(1) Duck
(2) Slap
(3) Go

> """)
        if action == "1":
            self.is_ducking = True
        elif action == "2":
            self.is_slapping = True
            input_value = "\n\nChoose an option:"
            option_count = 1
            for x in players:
                if not (x is self):
                    input_value += "\n("+str(option_count)+") "+x.name+" ["+x.character+"]"
                    option_count += 1
            input_value += "\n\n> "
            attack = int_input(input_value)
            
        elif action == "3":
            self.pos += 1
        
        board[self.id_] = ["—",]*len(board[self.id_])
        board[self.id_][self.pos] = self.character
        self.ppos = self.pos

class BigBrain(Player):
    def __init__(self, *t, **kwargs):
        super().__init__(*t, **kwargs)
    def Move(self, depth, alpha, beta):
        action = str(random.randint(1, 3))
        if action == "1":
            self.is_ducking = True
        elif action == "2":
            attack = random.randint(0, len(players) - 1)
            while attack == self.id_:
                attack = random.randint(0, len(players) - 1)
            
            self.is_slapping = True
            players[attack].is_slapped = True
        elif action == "3":
            self.pos += 1
        
        # self.pos += 1
        
        board[self.id_] = ["—",]*len(board[self.id_])
        board[self.id_][self.pos] = self.character
        self.ppos = self.pos
        print('moved')

obj_ = User({
    'name': 'Player',
    'character': 'P',
    'pos': 0,
    'ppos': 0,
    'slapped_id': False,
    'is_slapping': False,
    'is_slapped': False,
    'is_ducking': False,
    'is_going': False,
    'id_': len(players)
})
players.append(obj_)
obj_ = BigBrain({
    'name': 'Bot 1',
    'character': 'B',
    'pos': 0,
    'ppos': 0,
    'slapped_id': False,
    'is_slapping': False,
    'is_slapped': False,
    'is_ducking': False,
    'is_going': False,
    'id_': len(players)
})
players.append(obj_)
obj_ = BigBrain({
    'name': 'Bot A',
    'character': 'b',
    'pos': 0,
    'ppos': 0,
    'slapped_id': False,
    'is_slapping': False,
    'is_slapped': False,
    'is_ducking': False,
    'is_going': False,
    'id_': len(players)
})
players.append(obj_)

# +["▕ ▘"]
board = [['—']*10 for i in range(len(players))]
for x in players:
    s = x.__dict__
    board[s['id_']][s['pos']] = s['character']


def move(player):
    clear_screen()
    print('Duck, Slap, Go!'"\n\n"+'-'*50+"\n")
    
    
    print("\n".join(["  ".join([x for x in y]) for y in board])+"\n\n")
    
    message = ""
    
    for p in players:
        p.Move(2, -math.pow(2, 32), math.pow(2, 32))
    for i in range(len(players)):
        for j in range(len(players)):
            if i == j:
                continue
            
            this = players[i]
            that = players[j]
            
            is_slapped = check_slapped(i, j)
            
            if is_slapped:
                players[j].pos -= 2
                message += f"{i} just slapped {j}\n"
    for i in range(len(players)):
        players[i].is_ducking = players[i].is_slapping = players[i].is_slapped = players[i].slapped_id = False
    print(message)
    if message != "":
        time.sleep(3)
    return print('End of turn'), time.sleep(0.5), move(player)


move(cur_player)