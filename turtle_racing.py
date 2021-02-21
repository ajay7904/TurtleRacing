import game_functions
import random

settings = game_functions.GameSettings()
game_status = 'idle'

def listen_keyboard():
    screen.listen()
    screen.onkey(start_racing, 's')
    screen.onkey(ready_race, 'r')
    screen.onkey(exit_race, 'x')
    screen.exitonclick()


def start_racing():
    global game_status
    if game_status == 'ready':
        game_status = 'started'
        print("Racing started...")
        while game_status == 'started':
            for turtle in turtle_bank:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)
                if turtle.xcor() > 320:
                    turtle.shapesize(4, 4, 4)
                    print(f"The {turtle.pencolor()} turtle is the winner..!!")
                    print("Press 'r' to restart or 'x' to exit game")
                    game_status = 'idle'
                    break

def ready_race():
    global game_status
    global screen
    global turtle_bank
    if game_status == 'idle':
        screen = game_functions.create_new_screen(width=settings.screen_width, height=settings.screen_height,
                                              bgcolor=settings.screen_color)
        turtle_bank = game_functions.create_turtle_bank(settings)
        game_status = 'ready'
        print("Press 's' to start or 'x' to exit game")
        listen_keyboard()

def exit_race():
    print("exiting game...bye")
    screen.bye()


screen = game_functions.create_new_screen(width=settings.screen_width, height=settings.screen_height, bgcolor=settings.screen_color)
turtle_bank = game_functions.create_turtle_bank(settings)
game_status = 'ready'
print("Press 's' to start or 'x' to exit game")
listen_keyboard()