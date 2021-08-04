from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.pencolor('white')
        self.penup()
        self.sety(y=270)
        self.write_score()

    def write_score(self):
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score}', align='center', font=('Arial', 10, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.write_score()


