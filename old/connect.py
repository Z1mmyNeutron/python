class Connect4:
    def __init__(self, rows, cols):
        print("Welcome to Connect 4!")

        board = []

        for r in range(rows):
            r = [0] * cols
            board.append(r)

        self.board = board
        self.rows = rows
        self.cols = cols

    #print the board
    def printBoard(self):
        print("-" * (self.cols + 2))
        for row in range(self.rows):
            print("|", end="")

            for col in range(self.cols):
                val = self.board[self.rows - row -1][col] #reverse the order rows are printed in...
                if val == 0:
                    print(" ", end="")
                elif val == 1:
                    print("Y", end="")
                elif val == -1:
                    print("X", end="")
            print("|")

        print("-" * (self.cols + 2))

    #places a chip, assuming it's possible. validation checked elsewhere...
    #player == {-1, 1} depending on the player...
    def placeChip(self, player, col):
        if col < 0 or col >= self.cols:
            return
        if player != 1 and player != -1:
            return

        row = self.rows - 1 #max index for row...
        val = self.board[row][col]

        if val != 0: #implies this column is already filled to the max...
            return
        
        while val == 0 and row > 0:
            row = row - 1
            val = self.board[row][col]

        if val != 0:
            row = row + 1

        self.board[row][col] = player

    #checks all horizontal, vertical, diagonal (+ -) groups of 4 to validate a win.
    def checkWin(self, player):
        return self.checkRows(player) or self.checkCols(player) or self.checkDiagonalUp(player) or self.checkDiagonalDown(player)

    def checkDiagonalDown(self, player):
        count = 0

        startRow = 0
        startCol = 0

        while startRow < self.rows:
            while startCol < self.cols:
                for i in range(4):
                    checkRow = startRow + i
                    checkCol = startCol - i

                    if checkRow >= self.rows or checkCol < 0 or self.board[checkRow][checkCol] != player:
                        count = 0
                        break

                    count = count + 1

                    if count >= 4:
                        return True

                startCol = startCol + 1
            startRow = startRow + 1

        return False

    def checkDiagonalUp(self, player):
        count = 0

        startRow = 0
        startCol = 0

        while startRow < self.rows:
            while startCol < self.cols:
                for i in range(4):
                    checkRow = startRow + i
                    checkCol = startCol + i

                    if checkRow >= self.rows or checkCol >= self.cols or self.board[checkRow][checkCol] != player:
                        count = 0
                        break

                    count = count + 1

                    if count >= 4:
                        return True

                startCol = startCol + 1
            startRow = startRow + 1

        return False

    #iterate through all rows, checking for any groupings of 4 of either {-1 or 1} depending on the player
    def checkRows(self, player):
        for row in range(self.rows):
            count = 0

            for col in range(self.cols):
                val = self.board[row][col]
                if val == player:
                    count = count +1
                else:
                    count = 0

                if count >= 4:
                    return True

            return False
                
        return False

    def checkCols(self, player):
        for col in range(self.cols):
            count = 0

            for row in range(self.rows):
                val = self.board[row][col]
                if val == player:
                    count = count +1
                else:
                    count = 0

                if count >= 4:
                    return True

            return False
                
        return False

    #top level of board entirely filled up implies a tie, if called after checkwin returns False
    def checkTie(self):
        for col in range(self.cols):
            if self.board[self.rows - 1][col] == 0:
                return False
        return True        

    def promptInput(self, player):
        column = -1

        while column < 0 or column >= self.cols:
            if player == 1:
                column = int(input(("Player 1, Select a Move: ")))
            elif player == -1:
                column = int(input(("Player 2, Select a Move: ")))
        return column

game = Connect4(6,7)

hasWinner = False
hasTie = False

playerTurn = 1

while not hasWinner and not hasTie:
    game.printBoard()

    column = game.promptInput(playerTurn)

    game.placeChip(playerTurn, column)

    hasWinner = game.checkWin(playerTurn)

    if not hasWinner:
        hasTie = game.checkTie()

    playerTurn = playerTurn * -1 #1, -1, 1, -1, 1, -1 ...

playerTurn = playerTurn * -1 #get the last player turn...
game.printBoard()

if hasWinner:
    print("The winner is Player ", playerTurn)
else:   #no winner implies tie
    print("You both suck and this game was a tie")