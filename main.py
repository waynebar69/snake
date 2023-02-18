from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create the screen object
screen = Screen()
# Set the screen size in pixels
screen.setup(width=600, height=600)
# Change the screen background colour to black
screen.bgcolor("black")
# Create a title at the top of the screen
screen.title("My Snake Game")
# Turn off the screen tracer (We will now have to tell the screen when to refresh / update and display)
screen.tracer(0)
# Create 3 squares from turtles lined up on the horizontal axis

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Get the snake to start moving forward
game_is_on = True
while game_is_on:
    screen.update()
    # Give the screen a 0.1 seconds delay after each segment moves.
    # This slows down the screen to see what is happening
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

     #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()