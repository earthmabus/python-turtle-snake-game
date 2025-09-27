from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

SLEEP_TIME_IN_MS_INITIAL = 250
SLEEP_TIME_IN_MS = 250
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

# create the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Michael's Snake Game")
screen.tracer(0)

def quit_game():
    print("You pressed 'q' to quit the game")
    screen.bye()

snake = Snake()
food = Food()
scoreboard = ScoreBoard(int(SCREEN_WIDTH / 2) - 50, int(SCREEN_HEIGHT / 2))

screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=quit_game, key="q")
screen.listen()

def did_snake_hit_wall():
    if snake.segments[0].xcor() > int(SCREEN_WIDTH / 2) - 20: return True
    if snake.segments[0].xcor() < -1 * (int(SCREEN_WIDTH / 2)) + 20: return True
    if snake.segments[0].ycor() > int(SCREEN_HEIGHT / 2) - 20: return True
    if snake.segments[0].ycor() < -1 * (int(SCREEN_HEIGHT / 2)) + 20: return True
    return False

scoreboard.refresh()
def update_screen():
    # move the snake in the same direction
    snake.continue_moving()
    screen.update()

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.current_score_increase()

        # make the snake move faster every 3 bites
        global SLEEP_TIME_IN_MS
        if scoreboard.score % 3 == 0:
            SLEEP_TIME_IN_MS = int(SLEEP_TIME_IN_MS / 2)

    # detect collision with wall
    if did_snake_hit_wall():
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

        # reset the speed to slow
        SLEEP_TIME_IN_MS = SLEEP_TIME_IN_MS_INITIAL

    # detect collision with tail
    if snake.collide_with_tail():
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # wake up and move the snake again in SLEEP_TIME_IN_MS
    screen.ontimer(update_screen, SLEEP_TIME_IN_MS)

# wake the snake up for actions in SLEEP_TIME_IN_MS
screen.ontimer(update_screen, SLEEP_TIME_IN_MS)

screen.exitonclick()
