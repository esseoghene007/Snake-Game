import turtle

X_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.main_snake = []
        self.create_snake()
        self.head = self.main_snake[0]
        self.tail = self.main_snake[-1]
        
    def create_snake(self):
        for shapes in range(0, 3):
            self.add_segment(X_POSITIONS[shapes])
        
    def add_segment(self, shapes):
        new_snake = turtle.Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(shapes)
        self.main_snake.append(new_snake)

    def reset(self):
        for seg in self.main_snake:
            seg.goto(1000, 1000)
        self.main_snake.clear()
        self.create_snake()
        self.head = self.main_snake[0]

    def extend(self):
        #add a new sedment to the snake
        self.add_segment(shapes=self.tail.position())


    def move_snake(self):
        for snake_num in range(len(self.main_snake) - 1, 0, -1):
            new_x = self.main_snake[snake_num - 1].xcor()
            new_y = self.main_snake[snake_num - 1].ycor()
            self.main_snake[snake_num].goto(x=new_x, y=new_y)
        
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)



