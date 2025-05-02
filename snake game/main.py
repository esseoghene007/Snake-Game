import turtle 
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

user_snake = snake.Snake()
user_food = food.Food()
game_score = scoreboard.Scoreboard()



screen.listen()
screen.onkey(fun=user_snake.up, key="Up")
screen.onkey(fun=user_snake.down, key="Down")
screen.onkey(fun=user_snake.left, key="Left")
screen.onkey(fun=user_snake.right, key="Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    user_snake.move_snake()

    #detect collision with food.
    if user_snake.head.distance(user_food) < 15:
        user_food.refresh()
        user_snake.extend()
        game_score.increase_score()
    
    #detect collision with wall.
    if user_snake.head.xcor() > 290 or user_snake.head.xcor() < -290 or user_snake.head.ycor() < -290 or user_snake.head.ycor() > 290:
        game_score.reset()
        user_snake.reset()

    #detect collision with tail.
    for shapes in user_snake.main_snake[1:]:
        if user_snake.head.distance(shapes) < 10:
            game_score.reset()
            user_snake.reset()

            



  
   








screen.exitonclick()