# The following code creates the board
# Only 5 moves for X player and 4 for O player
#We're missing other features like checking if a player has already won
# as well  as checking if the player is entering a value that is within 
# the correct range. 
board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]
         ]
print(board[0])
print(board[1])
print(board[2])

# This is player X's first move
col = int(input("X player, select a column 1-3: "))
row = int(input("x player, select a row 1-3: "))

col -= 1
row -= 1

board[row][col] = "X"
print(board[0])
print(board[1])
print(board[2])

# This is player O's first move
col = int(input("O player, selct a column 1-3: "))
row = int(input("O player, select a row 1-3: "))

col -= 1
row -= 1

board[row][col] = "O"
print(board[0])
print(board[1])
print(board[2])

if board[row][col] == '-':
    board[row][col] = "O"
else:
    print("That spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])

# This is player X's second move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1

if board[row][col] == '-':
    board[row][col] = "X"
else:
    print("That spot was already taken")
print(board[0])
print(board[1])
print(board[2])

# This is player O's second move
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
col -= 1
row -= 1 

if board[row][col] == '-':
    board[row][col] = "O"
else:
    print("That spot was already taken.")
print(board[0])
print(board[1])
print(board[2])

# This is player X's thrid move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1

if board[row][col] == '-':
    board[row][col] = "X"
else:
    print("That spot was already taken.")
print(board[0])
print(board[1])
print(board[2])

# This is player O's third move
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select row 1-3: "))
col -= 1
row -= 1

if board[row][col] == '-':
    board[row][col] = "O"
else:
    print("That spot was already taken.")
print(board[0])
print(board[1])
print(board[2])

# This is player X's fourth move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1

if board[row][col] == '-':
    board[row][col] = "X"
else:
    print("That sport was already taken.")
print(board[0])
print(board[1])
print(board[2])

# This is player O's fouth move 
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
col -= 1
row -= 1

if board[row][col] == '-':
    board[row][col] = "O"
else:
    print("That spot was already taken.")
print(board[0])
print(board[1])
print(board[2])

# This is player X's fifth move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1

if board[row][col] == '-':
    board[row][col] = "X"
else:
    print("That spot was already taken.")
print(board[0])
print(board[1])
print(board[2])
