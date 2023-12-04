class GameBoard():
    def __init__(self):
        global grid
        grid = [[" "," "," "],
                [" "," "," "],
                [" "," "," "]]

    def printCurrentBoard(self):
        #Show the grid to the user.
        for r, row in enumerate(grid):
            if r == 0:
                print("\n")
                print("|".join(row))
            else:
                print("-----")   
                print("|".join(row))

    def placeX(self, i, j):
        i = i - 1
        j = j - 1
        row = grid[i]
        if row[j] == " ":
            row[j] = "X"
            return True
        return False

    def placeO(self, i, j):
        i = i - 1
        j = j - 1
        row = grid[i]
        if row[j] == " ":
            row[j] = "O"
            return True
        return False

    def getInput(self, player, game_piece):
        while True:
            try:              
                row, column = list(map(int, input('{}\'s Turn! Where should {} go? '.format(player, game_piece)).split()))
            except ValueError:
                print("You typed an invalid value. Try again.")
            else:
                res = all(1 <= i <= 3 for i in (row, column))
                if res:
                    return row, column
                else:
                    print("The integer value must be between 1 and 3. Try again.")


    def decideWinner(self, i, j):
        # (1,1)
        if grid[i-1][0] == grid[i-1][1] == grid[i-1][2] != " ":
            return True

        elif grid[0][j-1] == grid[1][j-1] == grid[2][j-1] != " ":
            return True

        elif grid[0][0] == grid[1][1] == grid[2][2] != " ":
            return True

        elif grid[2][0] == grid[1][1] == grid[0][2] != " ":
            return True
        
        return False


    def boardFull(self):
        if all(" " not in row for row in grid):
            return True
        return False


class ScoreBoard(dict): 
    def printScoreBoard(self):
        playername = self.keys()
        string_length=15
        print("Name".ljust(string_length-4," "),"| Wins | Losses | Draws")
        print("---------".ljust(string_length-4,"-"),"|------|--------|------")
        for player in playername:
            print(self[player]['Name'],"|   ".rjust(string_length-len(self[player]['Name']), " "), 
                  self[player]['Wins'], "|     ", self[player]['Losses'], "|   ", self[player]['Draws'])
    
    def addWin(self, playername):
        if playername not in self:
            self.update({playername: {'Name': playername, 'Wins': 0, 'Losses': 0, 'Draws': 0}})         
        self[playername]['Wins'] += 1

    def addLoss(self, playername):
        if playername not in self:
            self.update({playername: {'Name': playername, 'Wins': 0, 'Losses': 0, 'Draws': 0}})
        self[playername]['Losses'] += 1

    def addDraw(self, playername):
        if playername not in self:
            self.update({playername: {'Name': playername, 'Wins': 0, 'Losses': 0, 'Draws': 0}})
        self[playername]['Draws'] += 1





def main():
    print("\nWe are playing tic tac toe!\n"\
          "To play the game, enter two numbers to indicate where to place each game piece.\n"\
          "Enter numbers from 1 to 3.\n" \
          "1 1 is the top left corner. 3 3 is the bottom right corner.")
    
    score = ScoreBoard()
    userChoice = "y"
    while userChoice.lower() == "y":
        board = GameBoard()
        playerX = input("Who is playing as X? ")
        playerO = input("Who is playing as O? ") 
        board.printCurrentBoard()
        #Set the default number of turns.
        numberOfTurns = 1
        isWon= False
        isTie = False
        #Run until someone wins or it ties.
        while isWon == False and isTie == False:
            #Catch any errors with the input.
            player = ["_", playerX, playerO,  playerX, playerO,  playerX, playerO,  playerX, playerO, playerX][numberOfTurns]
            while True:
                #Get input and check who is the player is.
                #Edit the grid with the values given corresponding with the player. 
                if player == playerX:  
                    game_piece = "X"                                      
                    row, column = board.getInput(player, game_piece)
                    print()
                    if board.placeX(row, column):                    
                        break
                else: 
                    game_piece = "O"
                    row, column = board.getInput(player, game_piece)
                    print()
                    if board.placeO(row, column):                    
                        break
                print("That tile is already occupied!")
                board.printCurrentBoard()                      
            #Determine if the programs needs to terminate.
            isWon = board.decideWinner(row, column)
            #Check the status of the game.
            
            if isWon:
                print("Player " + player + " wins!") 
                score.addWin(player)
                if player == playerX:
                    score.addLoss(playerO)
                else:
                    score.addLoss(playerX)
            if not isWon and board.boardFull():
                isTie = True
                print("It is a tie!")
                score.addDraw(playerX)
                score.addDraw(playerO)
                
            #Draw the edited grid.
            board.printCurrentBoard() 
            numberOfTurns += 1

        print("\nGame over!\n")
        score.printScoreBoard()
        userChoice = input("Play again? (Y/N): ")
        while userChoice.lower() != "y" and userChoice.lower() != "n":
            print("Please type \"y\"  or \"n\". Try again.")
            userChoice = input("Play again? (Y/N): ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()
