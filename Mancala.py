class Mancala_Board:
    def __init__(self, mancala=None):
        if mancala is not None:
            self.mancala = mancala[:]
        else:
            self.mancala = [0] * 14
            for i in range(0, 6):
                self.mancala[i] = 4
            for i in range(7, 13):
                self.mancala[i] = 4

    def player_move(self, i):
        j = i
        repeat_turn = False
        add = self.mancala[j]
        self.mancala[j] = 0 
        while add > 0:
            j += 1
            j %= 14
            if (j == 6 and i >= 7) or (j == 13 and i < 6):
                continue
            self.mancala[j] += 1
            add -= 1
        if (j == 6 and i < 6) or (j == 13 and i >= 7):
            repeat_turn = True

        if (i < 6 and 0 <= j < 6 and self.mancala[j] == 1) or (i >= 7 and 7 <= j < 13 and self.mancala[j] == 1):
            opposite_index = 12 - j
            if self.mancala[opposite_index] > 0:
                mancala_index = 6 if i < 6 else 13
                self.mancala[mancala_index] += self.mancala[j] + self.mancala[opposite_index]
                self.mancala[j] = self.mancala[opposite_index] = 0

        while (i < 6 and 0 <= j < 6 and self.mancala[j] > 1) or (i >= 7 and 7 <= j < 13 and self.mancala[j] > 1):
            add = self.mancala[j]
            self.mancala[j] = 0
            while add > 0:
                j += 1
                j %= 14
                if (j == 6 and i >= 7) or (j == 13 and i < 6):
                    continue
                self.mancala[j] += 1
                add -= 1
            if (j == 6 and i < 6) or (j == 13 and i >= 7):
                repeat_turn = True
                break
            repeat_turn = False

        return repeat_turn

    def isEnd(self):
        if sum(self.mancala[0:6]) == 0 or sum(self.mancala[7:13]) == 0:
            self.mancala[6] += sum(self.mancala[0:6])
            self.mancala[13] += sum(self.mancala[7:13])
            for i in range(14):
                if i != 6 and i != 13:
                    self.mancala[i] = 0
            return True
        return False

    def print_mancala(self):
        for i in range(12, 6, -1):
            print('  ', self.mancala[i], '   ', end='')
        print()
        print(self.mancala[13], '                                           ', self.mancala[6])
        for i in range(0, 6):
            print('  ', self.mancala[i], '   ', end='')
        print()

    def husVal(self):
        if self.isEnd():
            if self.mancala[13] > self.mancala[6]:
                return 100
            elif self.mancala[13] == self.mancala[6]:
                return 0
            else:
                return -100
        return self.mancala[13] - self.mancala[6]

        
def alphabeta(mancala, depth, alpha, beta , MinorMax):
    if depth == 0 or mancala.isEnd():
        return mancala.husVal(),-1
    if MinorMax:
        v = -1000000
        player_move = -1
        for i in range(7,13,1):
            if mancala.mancala[i]==0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ =  alphabeta(a, depth-1, alpha, beta, minormax)
            if v < newv:
                player_move = i
                v = newv
            alpha = max(alpha, v)
            if alpha >= beta :
                break
        return v, player_move
    else:
        v = 1000000
        player_move = -1
        for i in range(0, 6, 1):
            if mancala.mancala[i] == 0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ = alphabeta(a, depth - 1, alpha, beta, not  minormax)
            if v > newv:
                player_move = i
                v = newv
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, player_move

def player_player():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("PLAYER 1 TURN >>> "))
            if h < 7 or h > 12 or j.mancala[h] == 0:
                print("You can't play at this position. Choose another position")
                continue

            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            h = int(input("PLAYER 2 TURN >>> "))
            if h > 5 or j.mancala[h] == 0:
                print("You can't play at this position. Choose another position")
                continue

            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break

    if j.mancala[0] < j.mancala[13]:
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
    print('GAME ENDED')
    j.print_mancala()

def player_aibot():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("YOUR TURN >>> "))
            if h > 5 or j.mancala[h] == 0:
                print("You can't Play at this position. Choose another position")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT TURN >>> ", end = "")
            _,k = alphabeta(j, 10, -100000, 100000, True)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
    if j.mancala[0] < j.mancala[13]:
        print("AI-BOT WINS")
    else:
        print("YOU WIN")
    print('GAME ENDED')
    j.print_mancala()

print("\n:::: MANCALA BOARD GAME ::::")
print("!!! Welcome to Mancala Gameplay !!!")
while True:
    print("\nChoose your Gameplay Type")
    print("(1) Player-1 vs Player-2")
    print("(2) Player vs AI-Bot")
    type = int(input(">>> "))
    if type == 1:
        player_player()
        break
    elif type == 2:
        player_aibot()
        break
    else:
        print("Wrong Gameplay Type. Enter Again")
        continue
