from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
food = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.title('Score')

score = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.write_score()
    if snake.head.distance(food) < 15:
        food.new_pos()
        snake.extend()
        scoreboard.score += 1

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.head.color('red')
        screen.update()
        time.sleep(1)
        scoreboard.reset_score()
        snake.reset_snake()
        screen.update()
        time.sleep(1)

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake.head.color('red')
            segment.color('red')
            screen.update()
            time.sleep(1)
            scoreboard.reset_score()
            snake.reset_snake()
            screen.update()
            time.sleep(1)




screen.exitonclick()