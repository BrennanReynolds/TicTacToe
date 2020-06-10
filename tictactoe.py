import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe!")

PLAYERXO = bool
x_turn = True
start_condition = False
win_condition = False
info_text = tk.StringVar()
info_text.set("Let's play some Tic Tac Toe!")


def startX():
    global PLAYERXO, start_condition
    start_condition=True
    PLAYERXO = 1
    print(PLAYERXO)
    info_text.set("your turn!")

def startO():
    global PLAYERXO, start_condition
    start_condition=True
    PLAYERXO = 0
    print(PLAYERXO)
    info_text.set("My Turn!")
    computer_move()

def playerxo_to_text(player_bool):
    if(player_bool):
        return "X"
    else:
        return "O"

def restartButton():
    global start_condition, win_condition
    print("Here we go again!")
    start_condition = False
    win_condition = False
    for button in gridButtons:
        button.clear()
    info_text.set("Here we go again!")


def winchecker(which_player):
    win_counter = [0,0,0,0,0,0,0,0]
    for button in gridButtons:
        if (button.text.get() == playerxo_to_text(which_player)):
            for row in range(2,5):
                if button.row == row:
                    win_counter[row-2]+=1
            for column in range(0,3):
                if button.column == column:
                    win_counter[column+3]+=1
            if button.row-2 == button.column:
                if button.row-2 == 1:
                    win_counter[7]+=1
                win_counter[6]+=1
            if ((button.row-2 == 2) and (button.column==0)) or ((button.row-2 == 0) and (button.column==2)):
                win_counter[7]+=1

    print(win_counter)
    for potential_win in range(0,len(win_counter)):
        if win_counter[potential_win] == 3:
            print("Win at "+str(potential_win))
            info_text.set("Nice Job!!")
            return True
    return False

def computer_move():
    global x_turn, win_condition
    comp_letter = playerxo_to_text(not PLAYERXO)
    for button in gridButtons:
        if button.text.get() == "":
            button.text.set(comp_letter)
            x_turn = not x_turn
            if winchecker(not PLAYERXO):
                info_text.set("Ha! Got You!")
                win_condition = True
            break

xbutton = tk.Button(text="Play as X", command=startX)
xbutton.grid(row=0,column=0)
obutton = tk.Button(text="Play as O",command=startO)
obutton.grid(row=0,column=1)
restartbutton = tk.Button(text="Restart", command=restartButton)
restartbutton.grid(row=0,column=2)
infolabel = tk.Label(textvariable = info_text)
infolabel.grid(row=1, column = 0, columnspan = 3)

class XOButton:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.text = tk.StringVar()
        self.text.set("")
        self.button = tk.Button(height=0, width=3, command=self.buttonAction, font=("Arial", 100), textvariable=self.text)
        self.button.grid(row=row, column=column)


    def buttonAction(self):
        global win_condition
        if start_condition == True and win_condition == False:
            print("pressed button at "+str(self.row)+", "+str(self.column)+"!!")
            self.text.set(playerxo_to_text(PLAYERXO))
            if not winchecker(PLAYERXO):
                computer_move()
            else:
                win_condition = True

        else:
            if win_condition == True and start_condition == True:
                info_text.set("Restart the game to play again!")
            if win_condition == False and start_condition == False:
                info_text.set("You have to pick a letter to start!")

    def clear(self):
        self.text.set("")

gridButtons = []

for y in range(2,5):
    for x in range(0,3):
        gridButtons.append(XOButton(y,x))


root.mainloop()
