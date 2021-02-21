from turtle import Turtle, Screen

class GameSettings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen_color = 'grey'

        self.turtle_color = ['red', 'green', 'yellow', 'blue', 'maroon', 'purple']
        self.turtle_yposition = [-160, -94, -28, 40, 106, 172]


def create_turtle_bank(settings):
    turtles = []
    for i in range(6):
        tur = create_turtle()
        turtles.append(tur)
        set_turtle_color(tur, settings.turtle_color[i])
        set_turtle_home_position(tur, i, settings)
    return turtles

def create_turtle():
    tur = Turtle(shape='turtle')
    tur.resizemode('user')
    tur.shapesize(2, 2, 2)
    tur.penup()
    return tur

def set_turtle_color(tur, color):
    tur.color(color)

def set_turtle_home_position(tur, tur_id, settings):
    tur.goto(x=-380, y=settings.turtle_yposition[tur_id])

def create_new_screen(width, height, bgcolor):
    scr = Screen()
    scr.clear()
    scr.title('Turtle Race...!!')
    scr.setup(width=width, height=height)
    scr.colormode(255)
    scr.bgcolor(bgcolor)
    return scr