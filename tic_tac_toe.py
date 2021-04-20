print("Welcome, let's play Tic-tac-Toe \n For playing, select the required number and the mark will be displayed. ")
player_one = input('Player 1 write your name.')
player_two = input('Player 2 now you do it.')
l = ['X', 'O']

one_sign = input('{}Select your symbol- X or O by typing the symbol'.format(player_one))
x = True
while x:
    if one_sign not in l:
        print("Try again", end="")
        one_sign = input()
        pass
    else:
        x = False
l.remove(one_sign)
two_sign = l[0]
left_no = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 1
winning_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
win = True
player_one_turn = []
player_two_turn = []
for i in range(10):
    if i in left_no:
        if i % 3 != 0:
            print(i, '\t', end='')

        else:
            print(i)

    for i in winning_list:
        won = 0
        for j in i:
            if j in player_one_turn:
                won += 1
                if won == 3:
                    print('Won by player 1')

            if j in player_two_turn:
                won += 1
                if won == 3:
                    print('Won by player 2')

                break

while win:
    for turn in range(1, 10, 1):
        if not left_no:
            print('Draw')
            win = False
            quit()
        elif turn % 2 != 0:
            played_num = int(input(f'{player_one} select the number'))
            player_one_turn.append(played_num)
            player_one_turn.sort()
            left_no.remove(played_num)
            for i in winning_list:
                win_one = 0
                win_two = 0
                for j in i:
                    if j in player_one_turn:
                        win_one += 1
                        if win_one == 3:
                            print(f'{player_one} has won')
                            win = False
                            quit()
                            break
                    if j in player_two_turn:
                        win_two += 1
                        if win_two == 3:
                            print(f'{player_two} has won')
                            quit()
                            break
            for i in range(10):
                if i in left_no:
                    if i % 3 != 0:
                        print(i, '\t', end='')

                    else:
                        print(i)
                elif i in player_one_turn:
                    if i % 3 != 0:
                        print(f'{one_sign}', '\t', end='')

                    else:
                        print(f'{one_sign}')
                elif i in player_two_turn:
                    if i % 3 != 0:
                        print(f'{two_sign}', '\t', end='')

                    else:
                        print(f'{two_sign}')

        else:
            played_num = int(input(f'{player_two} select the number'))
            player_two_turn.append(played_num)
            player_two_turn.sort()
            left_no.remove(played_num)
            for i in winning_list:
                win_one = 0
                win_two = 0
                for j in i:
                    if j in player_one_turn:
                        win_one += 1
                    elif win_one == 3:
                        print(f'{player_one} has won')
                        win = False
                        quit()
                        break
                    if j in player_two_turn:
                        win_two += 1
                        if win_two == 3:
                            print(f'{player_two} has won')
                            win = False
                            quit()
                            break
            for i in range(10):
                if i in left_no:
                    if i % 3 != 0:
                        print(i, '\t', end='')

                    else:
                        print(i)
                elif i in player_two_turn:
                    if i % 3 != 0:
                        print(f'{two_sign}', '\t', end='')

                    else:
                        print(f'{two_sign}')
                elif i in player_one_turn:
                    if i % 3 != 0:
                        print(f'{one_sign}', '\t', end='')

                    else:
                        print(f'{one_sign}')
print('Draw')

for i in winning_list:
    win_one = 0
    win_two = 0
    for j in i:
        if j in player_one_turn:
            win_one += 1
            if win_one == 3:
                print(f'{player_one} has won')
                break
        if j in player_two_turn:
            win_two += 1
            if win_two == 3:
                print(f'{player_two} has won')
                break
