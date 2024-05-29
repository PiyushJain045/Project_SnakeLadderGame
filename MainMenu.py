from tkinter import *
import pygame

# Colors and constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"  # Adding white color for foreground text
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = "✓"
timer = None

# Initialize Pygame
pygame.init()
pygame.mixer.init()
menu_sound = pygame.mixer.Sound("Sound/MainMenu.wav")
menu_sound.play()

# Create main window
window = Tk()
window.title("Snake and Ladder")
window.minsize(width=900, height=700)

# Create a Canvas widget and set the background image
canvas = Canvas(window, width=900, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load background image
MM_img = PhotoImage(file="Image/MM2.png")
canvas.create_image(0, 0, image=MM_img, anchor="nw")

# Add label for main menu
my_label = Label(window, text="Main Menu", fg=GREEN, font=(FONT_NAME, 50, "bold"))
canvas.create_window(450, 50, window=my_label)

# Add label for choosing players
label = Label(window, text="Choose the number of Players", fg="Black", font=(FONT_NAME, 20), bg=YELLOW)
canvas.create_window(450, 150, window=label)

# Function for radio button
def radio_used():
    print(radio_state.get())

# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(window, text="2 Players", value=2, variable=radio_state, command=radio_used, fg="RED", font=(FONT_NAME, 15), bg=YELLOW)
radiobutton2 = Radiobutton(window, text="3 players", value=3, variable=radio_state, command=radio_used, fg="RED", font=(FONT_NAME, 15), bg=YELLOW)
radiobutton3 = Radiobutton(window, text="4 players", value=4, variable=radio_state, command=radio_used, fg="RED", font=(FONT_NAME, 15), bg=YELLOW)
radiobutton4 = Radiobutton(window, text="Computer", value=0, variable=radio_state, command=radio_used, fg="RED", font=(FONT_NAME, 17), bg=YELLOW)

# Add radio buttons to the canvas
canvas.create_window(450, 200, window=radiobutton1)
canvas.create_window(450, 250, window=radiobutton2)
canvas.create_window(450, 300, window=radiobutton3)
canvas.create_window(450, 350, window=radiobutton4)

# Function for button action
def action():
    print("Do something")
    menu_sound.stop()
    window.destroy()

# Add button to the canvas
button = Button(window, text="Let's Play!", command=action, fg=WHITE, font=(FONT_NAME, 20), bg=RED)
canvas.create_window(450, 420, window=button)

# Class to get user choice
class user_choice:
    def __init__(self):
        self.n = radio_state.get()

    def total_players(self):
        return self.n

# Run the main loop
window.mainloop()
