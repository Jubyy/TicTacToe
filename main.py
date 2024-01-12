congrats=r'''   ____   U  ___ u  _   _     ____     ____        _       _____    _   _    _         _       _____             U  ___ u  _   _    ____     _    
U /"___|   \/"_ \/ | \ |"| U /"___|uU |  _"\ u U  /"\  u  |_ " _|U |"|u| |  |"|    U  /"\  u  |_ " _|     ___     \/"_ \/ | \ |"|  / __"| uU|"|u  
\| | u     | | | |<|  \| |>\| |  _ / \| |_) |/  \/ _ \/     | |   \| |\| |U | | u   \/ _ \/     | |      |_"_|    | | | |<|  \| |><\___ \/ \| |/  
 | |/__.-,_| |_| |U| |\  |u | |_| |   |  _ <    / ___ \    /| |\   | |_| | \| |/__  / ___ \    /| |\      | | .-,_| |_| |U| |\  |u u___) |  |_|   
  \____|\_)-\___/  |_| \_|   \____|   |_| \_\  /_/   \_\  u |_|U  <<\___/   |_____|/_/   \_\  u |_|U    U/| |\u\_)-\___/  |_| \_|  |____/>> (_)   
 _// \\      \\    ||   \\,-._)(|_    //   \\_  \\    >>  _// \\_(__) )(    //  \\  \\    >>  _// \\_.-,_|___|_,-.  \\    ||   \\,-.)(  (__)|||_  
(__)(__)    (__)   (_")  (_/(__)__)  (__)  (__)(__)  (__)(__) (__)   (__)  (_")("_)(__)  (__)(__) (__)\_)-' '-(_/  (__)   (_")  (_/(__)    (__)_) '''
def make_board(values):
    print('1 | 2 | 3 \n----------\n4 | 5 | 6 \t \n----------\n7 | 8 | 9\n\n ')
    board=''
    separator_vertical=0
    for i in values:
        separator_horizontal=0
        for j in i:
            if j==-1:
                board+=' '
            elif j==0:
                board+='O'
            else:
                board+='X'
            if separator_horizontal<2:
                board+=" | "
            separator_horizontal+=1
        if separator_vertical<2:
            board+='\n----------\n'
        separator_vertical+=1
    print(board)



def make_turn(whose_turn,values):
    symbol = 'X' if whose_turn == 'X' else 'O'
    print(f"That's {symbol} turn. Pick a number between 1 to 9: ")

    while True:
        try:
            choice = int(input())
            if 1 <= choice <= 9:
                row, col = divmod(choice - 1, 3)
                if values[row][col] == -1:
                    values[row][col] = 1 if whose_turn == 'X' else 0
                    return 'O' if whose_turn == 'X' else 'X'
                else:
                    print("Cell already taken. Pick another number.")
            else:
                print("Please enter a number between 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")




def check_winner(values):
    winner_X=[]
    winner_O=[]
    columns=[[] for _ in range(3)]
    diagonals=[[] for _ in range(2)]
    for index,row in enumerate(values):
        winner_X.append(all(ele == 1 for ele in row))
        winner_O.append(all(ele == 0 for ele in row))
        for jindex,value in enumerate(row):
            columns[jindex].append(value)

    for column in columns:
        winner_X.append(all(ele == 1 for ele in column))
        winner_O.append(all(ele == 0 for ele in column))

    for i in range(3):
        diagonals[0].append(values[i][i])
    for i in range(3):
        diagonals[1].append(values[i][2 - i])

    for diagonal in diagonals:
        winner_X.append(all(ele == 1 for ele in diagonal))
        winner_O.append(all(ele == 0 for ele in diagonal))
    if True in winner_X:
        return 'X'
    elif True in winner_O:
        return 'O'



def game():
    game=True
    values = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    whose_turn = 'X'
    while game:
        make_board(values)
        whose_turn=make_turn(whose_turn,values)
        who_win=check_winner(values)
        if who_win=='X':
            game=False
        elif who_win=='O':
            game=False
    print(f" {congrats} \nThe player with symbol {who_win} just won!")



game()
