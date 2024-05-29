from turtle import Turtle
import random
import time
import pygame

pygame.init()
pygame.mixer.init()
dice_sound = pygame.mixer.Sound("Sound/dicesound.wav")

class BgColor(Turtle):
    def __init__(self, in_color, X, Y):
        super().__init__()
        self.hideturtle()
        self.fillcolor(in_color)
        self.penup()
        self.goto(X, Y)

    def ColorBackground(self, f1, r1, f2, r2, i):
        self.pendown()
        self.begin_fill()
        for _ in range(i):
            self.forward(f1)
            self.right(r1)
            self.forward(f2)
            self.right(r2)
        self.end_fill()

dice_bg = BgColor('yellow', -40, -165)
dice_bg.ColorBackground(100, 90, 0, 0, 4)

class Dice(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('red')
        self.penup()
        self.goto(x=-8, y=-247)
        self.write("0", font=("Courier", 40, "normal"))
        self.dice_number = 0

    def roll_dice(self, scr):
        dice_sound.play()
        for i in range(15):
            time.sleep(0.1)
            scr.tracer(0)
            self.clear()
            self.dice_number = random.randint(1, 6)
            self.write(f"{self.dice_number}", font=("Courier", 40, "normal"))
            scr.tracer(1)
        return self.dice_number
