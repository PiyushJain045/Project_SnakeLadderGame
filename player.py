from turtle import Turtle
from board_point import Board_Point
import pygame, time

pygame.init()
pygame.mixer.init()
snake_sound = pygame.mixer.Sound("Sound/Snake.wav")

board_obj = Board_Point()
class Player(Turtle):
    def __init__(self, S, C):
        super().__init__()
        self.shape(S)
        self.color(C)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=-225, y=-115)

    def move_f(self):
        self.pendown()
        self.forward(50)
        print(f"X:{self.xcor()}, Y:{self.ycor()}")
        self.penup()
        self.clear()

    def turn_up(self):
        self.setheading(90)

    def turn_down(self):
        self.setheading(270)

    def turn_left(self):
        self.setheading(180)

    def turn_right(self):
        self.setheading(0)

    def movement_on_board(self, dice_n):
        for _ in range(dice_n):
        # for _ in range(1):
            current_position = (int(self.xcor()), int(self.ycor()))

            if current_position in board_obj.end_game:
                if dice_n <= board_obj.end_game[current_position]:
                    pass
                elif current_position == board_obj.win_ordinate:
                    break
                else:
                    break
            if current_position in board_obj.right_terminal:
                self.left(90)
            if current_position in board_obj.left_terminal:
                self.right(90)
            self.move_f()

        if (int(self.xcor()), int(self.ycor())) in board_obj.ladder_snake:
            X = board_obj.ladder_snake[(int(self.xcor()), int(self.ycor()))][0]
            Y = board_obj.ladder_snake[(int(self.xcor()), int(self.ycor()))][1]
            turn = board_obj.ladder_snake[(int(self.xcor()), int(self.ycor()))][2]
            snake_sound.play()
            time.sleep(1)
            self.goto(X, Y)
            self.setheading(turn)
