board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}
player = 1  # to initialise 1st player
tot_moves = 0  # to count total moves
finish = 0

def check():
    # player 1
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Player 1 won')
        return 1
    if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Player 1 won')
        return 1
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Player 1 won')
        return 1

    if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Player 1 won')
        return 1
    if board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X':
        print('Player 1 won')
        return 1

    if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Player 1 won')
        return 1
    if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Player 1 won')
        return 1
    if board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
        print('Player 1 won')
        return 1

    # Player 2
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('Player 2 won')
        return 1
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Player 2 won')
        return 1
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Player 2 won')
        return 1

    if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Player 2 won')
        return 1
    if board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O':
        print('Player 2 won')
        return 1

    if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Player 2 won')
        return 1
    if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Player 2 won')
        return 1
    if board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
        print('Player 2 won')
        return 1
    return 0  # if check fails


print("1|2|3")
print("-+-+-")
print("4|5|6")
print("-+-+-")
print("7|8|9")
print("* *  * * *")

while True:
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

    finish = check()
    if tot_moves == 9 or finish == 1:
        break
    while True:                            #input from players
        if player == 1:                    #choose player
            p1_input = input('Player 1')
            if p1_input in board and board[p1_input] == ' ':
                board[p1_input] = 'X'
                player = 2
                break
            else:
                print("Please try again")
                continue
        else:
            p2_input = input('Player 2')
            if p2_input in board and board[p2_input] == ' ':
                board[p2_input] = 'O'
                player = 1
                break
            else:
                print("Please try again")
                continue
    tot_moves += 1
    print("* * * * * * *")








