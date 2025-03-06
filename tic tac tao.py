#program tonmake a tic tac toe
board=["-","-","-","-","-","-","-","-","-"]
pos=""
game_still_going=True
winner=None
curr_pla="x"
def play_game():
    display_board()
    while game_still_going:
        hundle_turn(curr_pla)
        check_if_game_over()
        flip_player()
    if winner=="x" or winner=="o":
        print(winner,"won")
    elif winner==None:
        print("tie")
def display_board():
    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])

def hundle_turn(player):
    print(player,"'s turn")
    pos=input("enter a position from the board")
    valid=False
    while not valid:
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos=input("enter a position from the board")
        pos=int(pos)-1
        if board[pos]=="-":
            valid=True
        elif board[pos]!="-":
            print("the space is occupied,try another position")
            
    board[pos]=player
    display_board()
def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():
    global winner
    row_winner=check_row()
    columns_winner=check_columns()
    diagonals_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif columns_winner:
        winner=columns_winner
    elif diagonals_winner:
        winner=diagonals_winner 
    else:
        winner==None
    return
def check_row():
    global game_still_going
    row_1=(board[0]==board[1]==board[2]!="-")
    row_2=(board[3]==board[4]==board[5]!="-")
    row_3=(board[6]==board[7]==board[8]!="-")
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_columns():
    global game_still_going
    columns_1=(board[0]==board[3]==board[6]!="-")
    columns_2=(board[1]==board[4]==board[7]!="-")
    columns_3=(board[2]==board[5]==board[8]!="-")
    if columns_1 or columns_2 or columns_3:
        game_still_going=False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return
def check_diagonals():
    global game_still_going
    diagionals_1=(board[0]==board[4]==board[8]!="-")
    diagionals_2=(board[2]==board[4]==board[6]!="-")
    if diagionals_1 or diagionals_2:
        game_still_going=False
    if diagionals_1:
        return board[0]
    elif diagionals_2:
        return board[2]
    return
def check_if_tie():
    global game_still_going
    global board
    if "-" not in board:
        game_still_going=False
    return
def flip_player():
    global turn
    global curr_pla
    if curr_pla=="x":
        curr_pla="o"
    elif curr_pla=="o":
        curr_pla="x"
    return



play_game()



        
