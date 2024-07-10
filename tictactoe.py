def printBoard():
    one   = 'X' if Xstate[0] else 'O' if Ostate[0] else 1
    two   = 'X' if Xstate[1] else 'O' if Ostate[1] else 2
    three = 'X' if Xstate[2] else 'O' if Ostate[2] else 3
    four  = 'X' if Xstate[3] else 'O' if Ostate[3] else 4
    five  = 'X' if Xstate[4] else 'O' if Ostate[4] else 5
    six   = 'X' if Xstate[5] else 'O' if Ostate[5] else 6
    seven = 'X' if Xstate[6] else 'O' if Ostate[6] else 7
    eight = 'X' if Xstate[7] else 'O' if Ostate[7] else 8
    nine  = 'X' if Xstate[8] else 'O' if Ostate[8] else 9

    print(f"{one} | {two} | {three}")
    print(f"--|---|--")
    print(f"{four} | {five} | {six}")
    print(f"--|---|--")
    print(f"{seven} | {eight} | {nine}")

def checkWin(Xstate, Ostate):
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for wins in win:
        if (Xstate[wins[0]] + Xstate[wins[1]] + Xstate[wins[2]] == 3):
            return 1
        if (Ostate[wins[0]] + Ostate[wins[1]] + Ostate[wins[2]] == 3):
            return 0
    return -1

Turn = 1
Ostate = [0,0,0,0,0,0,0,0,0]
Xstate = [0,0,0,0,0,0,0,0,0]
Xname = input("Please enter X's player name: ")
Oname = input("Please enter O's player name: ")

while True:
    printBoard()
    if Turn == 1:
        value = int(input(f"{Xname}'s chance, please enter a value: "))
        while Xstate[value - 1] == 1 or Ostate[value - 1] == 1:
            print(f"OOPS!! {value} is already occupied by {Oname if Ostate[value - 1] else Xname}")
            value = int(input(f"Please try a different value, {Xname}: "))
        Xstate[value - 1] = 1
    else:
        value = int(input(f"{Oname}'s chance, please enter a value: "))
        while Xstate[value - 1] == 1 or Ostate[value - 1] == 1:
            print(f"OOPS!! {value} is already occupied by {Xname if Xstate[value - 1] else Oname}")
            value = int(input(f"Please try a different value, {Oname}: "))
        Ostate[value - 1] = 1

    Turn = 1 - Turn
    win = checkWin(Xstate, Ostate)
    if win == 1:
        printBoard()
        print(f"Hurray! {Xname} won the game!")
        break
    elif win == 0:
        printBoard()
        print(f"Hurray! {Oname} won the game!")
        break
    elif all(x + o != 0 for x, o in zip(Xstate, Ostate)):
        printBoard()
        print("It's a draw!")
        break
