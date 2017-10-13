
class TicTacToe:
	def __init__(self):
		self.board = [
					['-','-','-'],
					['-','-','-'],
					['-','-','-']
				]

	def printBoard(self):
		print(self.board[0][0], " | ", self.board[0][1], " | ", self.board[0][2])
		print(self.board[1][0], " | ", self.board[1][1], " | ", self.board[1][2])
		print(self.board[2][0], " | ", self.board[2][1], " | ", self.board[2][2])

	def addMove(self, row, col, piece):
		if (self.board[row][col] == '-'):
			self.board[row][col] = piece
			return True
		else:
			return False


	def isBoardFull(self):
		for row in range(0, len(self.board)):
			for col in range(0,len(self.board[row])):
				if (self.board[row][col] == '-'):
					return False
		return True

	def changeMove(self, piece):
		if (piece == 'X'):
			return 'O'
		else:
			return 'X'

	def checkWinner(self):
		if (self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] 
			and (self.board[0][0] == 'X' or self.board[0][0] == 'O')):
			return True
		elif (self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] 
			and (self.board[1][0] == 'X' or self.board[1][0] == 'O')):
			return True
		elif (self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] 
			and (self.board[2][0] == 'X' or self.board[2][0] == 'O')):
			return True
		elif (self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] 
			and (self.board[0][0] == 'X' or self.board[0][0] == 'O')):
			return True
		elif (self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[2][1] 
			and (self.board[1][0] == 'X' or self.board[1][0] == 'O')):
			return True
		elif (self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] 
			and (self.board[2][0] == 'X' or self.board[2][0] == 'O')):
			return True
		elif (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] 
			and (self.board[0][0] == 'X' or self.board[0][0] == 'O')):
			return True
		elif (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] 
			and (self.board[0][2] == 'X' or self.board[0][2] == 'O')):
			return True
		else:
			return False

# create the tic tac toe object
game = TicTacToe()


print("Welcome to TicTacToe!!!")


game.printBoard()

token = 'X'

while(not game.isBoardFull()):
	print(token, "enter your move (row,col)")
	row = input()
	row = int(row) # convert str to int 
	
	col = input()
	col = int(col)

	while(game.addMove(row, col, token) == False):
		print("Invalid move. Player enter again")
		row = input()
		row = int(row)

		col = input()
		col = int(col)

	game.printBoard()

	if (game.checkWinner() == True):
		print(token, "won the game")
		break   # this quits the loop


	token = game.changeMove(token)

if (game.checkWinner() == False):
	print("There has been a tie.")
































