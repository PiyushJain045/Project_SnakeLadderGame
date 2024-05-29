# ----------------Main Menu---------------------#
import time

from MainMenu import user_choice

obj = user_choice()
n_players = obj.total_players()
print(n_players)

# ----------------------------------------------------------------#
from turtle import Screen
from turtle import Turtle
from player import Player

# --------------------------Define Turtle Screen------------------#
screen = Screen()
screen.setup(width=900, height=700)
screen.bgpic("Image/wooden.png")
screen.title("Snake and Ladder")
screen.addshape("Image/snakeboard2.gif")
screen.tracer(0)
# ---------------------form Dice bg color------------------#
from dice import Dice, BgColor

# ---------------------Set the snake and ladder board--------------------#
board = Turtle()
board.penup()
board.shape("Image/snakeboard2.gif")
board.goto(x=0, y=100)
# -----------------------Player token and related data-------------------------------#

all_players = []
if n_players != 0:
    player_attributes = [('turtle', 'red'),
                         ('turtle', 'blue'),
                         ('turtle', 'green'),
                         ('turtle', 'yellow')]

    for i in range(0, n_players):
        player = Player(player_attributes[i][0], player_attributes[i][1])
        all_players.append(player)

    all_message = [
        ["red", "Red's", (-360, 120)],
        ["blue", "Blue's", (280, 120)],
        ["green", "green", (-370, -100)],
        ["yellow", "yellow", (280, -100)]
    ]

if n_players == 0:
    player_attributes = [('turtle', 'red'),
                         ('circle', 'blue')
                         ]

    for i in range(0, 2):
        player = Player(player_attributes[i][0], player_attributes[i][1])
        all_players.append(player)

    all_message = [
        ["red", "Red's", (-360, 120)],
        ["blue", "Bot's", (280, 120)]
    ]

# ------------------mechanism to get co-ordinates using player0------------#
print(f"X:{all_players[0].xcor()}, Y:{all_players[0].ycor()}")
screen.listen()
screen.onkey(all_players[0].move_f, "0")
screen.onkey(all_players[0].turn_up, "Up")
screen.onkey(all_players[0].turn_down, "Down")
screen.onkey(all_players[0].turn_right, "Right")
screen.onkey(all_players[0].turn_left, "Left")

# -------------initial 'Roll the dice' message--------------#
rtd_message_bg = BgColor('yellow', -220, 125)
rtd_message_bg.ColorBackground(450, 90, 40, 90, 2)
roll_the_dice_message = Turtle()
roll_the_dice_message.hideturtle()
roll_the_dice_message.penup()
roll_the_dice_message.color('red')
roll_the_dice_message.goto(-200, 90)
roll_the_dice_message.write(f"Press R to Roll the Dice!", font=("Courier", 20, "bold"))


# --------'which player's Turn' message background color------------------#
def bg_color(C, X, Y, f1, r1, f2, r2, i):
    turn_message_background = BgColor(C, X, Y)
    turn_message_background.ColorBackground(f1, r1, f2, r2, i)


bg_color('white', -375, 200, 105, 90, 0, 0, 4)
bg_color('white', 276, 200, 105, 90, 0, 0, 4)
bg_color('white', -375, -20, 105, 90, 0, 0, 4)
bg_color('white', 276, -20, 105, 90, 0, 0, 4)

####-----------------------GAME MECHANISM------------------------####.
DICE = Dice()

# ------------------------'which player's Turn' message--------------#
turn_message = Turtle()
turn_message.hideturtle()
turn_message.penup()

screen.tracer(1)
value = 0

screen.tracer(0)
# turn_message.clear()
turn_message.color(all_message[value][0])
turn_message.goto(all_message[value][2][0], all_message[value][2][1])
turn_message.write(f"{all_message[value][1]}\nTurn", font=("Courier", 20, "bold"))
screen.tracer(1)


def handle_player():
    roll_the_dice_message.clear()
    rtd_message_bg.clear()

    global value, all_players, all_message

    screen.tracer(0)
    turn_message.color(all_message[value][0])
    turn_message.goto(all_message[value][2][0], all_message[value][2][1])
    turn_message.write(f"{all_message[value][1]}\nTurn", font=("Courier", 20, "bold"))
    screen.tracer(1)

    # ------------------Moves the token-------------------------------------#
    moves = DICE.roll_dice(screen)
    all_players[value].movement_on_board(moves)

    if n_players != 0:
        value += 1
        if value > n_players - 1:
            value = 0
    elif n_players == 0:
        value += 1
        if value > 1:
            value = 0

    screen.tracer(0)
    turn_message.clear()
    turn_message.color(all_message[value][0])
    turn_message.goto(all_message[value][2][0], all_message[value][2][1])
    turn_message.write(f"{all_message[value][1]}\nTurn", font=("Courier", 20, "bold"))
    screen.tracer(1)

    if n_players == 0:
        if value == 1:
            time.sleep(1)
            handle_player()


screen.onkey(handle_player, "r")
print("I won")
screen.exitonclick()
