import turtle

# Makes Turtles for the 
class myTurtle:
    def __init__(self, x, y, pspeed, pcolor, pshape, pwidth) -> None:
        self.x, self.y = x, y
        self.pspeed = pspeed
        self.pcolor = pcolor
        self.pshape = pshape
        self.pwidth = pwidth

    # Defining a turtle
    def define_turtle(self):
        pname = turtle.Turtle()
        pname.up()
        pname.color(self.pcolor)
        pname.speed(self.pspeed)
        pname.width(self.pwidth)
        pname.setposition(self.x, self.y)
        pname.shape(self.pshape)
        return pname

class Grid:
    # Turtles to control the row and column
    def __init__(self):
        self.rowTurtle = [myTurtle(-300, 100, 5, "white", "arrow", 5).define_turtle() for i in range(2)]
        self.columnTurtle = [myTurtle(-100, 300, 5, "yellow", "arrow", 5).define_turtle() for i in range(2)]

    # Set positions for the latter turtles
    def set_turtles(self):
        self.columnTurtle[1].setposition(100, 300)
        self.rowTurtle[1].setposition(-300, -100)

    # Draw Columns and Rows
    def draw_row_columns(self):
        for i in range(2):
            self.columnTurtle[i].down()
            self.columnTurtle[i].right(90)
            self.columnTurtle[i].forward(600)
            self.columnTurtle[i].hideturtle()

            self.rowTurtle[i].down()
            self.rowTurtle[i].forward(600)
            self.rowTurtle[i].hideturtle()

class DrawAction:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.count = 0
        self.fxn()
        self.det_turn()

    # Set x, y to get the proper square
    def fxn(self):
        if -298.0 < self.x < -117.0:
            self.x = -200
        elif -73.0 < self.x < 83.0:
            self.x = 0
        elif 115.0 < self.x < 272.0:
            self.x = 200

        if -276.0 < self.y < -119.0:
            self.y = -200
        elif -84.0 < self.y < 82.0:
            self.y = 0
        elif 109.0 < self.y < 293.0:
            self.y = 200
            
    # Determine the turn
    def det_turn(self):
       if self.count % 2 == 0:
           self.draw_circle()
       else:
           self.draw_cross()
       self.count += 1

    # Draw circle or cross
    def draw_circle(self):
        circleTurtle = myTurtle(self.x, self.y - 50, 10, "white", "arrow", pwidth = 7).define_turtle()
        circleTurtle.hideturtle()
        circleTurtle.down()
        circleTurtle.circle(65)
        circleTurtle.up()

    def draw_cross(self):
        crossTurtle = myTurtle(self.x, self.y - 50, 10, "white", "arrow", pwidth = 8).define_turtle()
        crossTurtle.hideturtle()
        crossTurtle.down()
        crossTurtle.left(45)
        crossTurtle.forward(100)
        crossTurtle.backward(160)
        crossTurtle.up()
        crossTurtle.setposition(self.x - 50, self.y + 70)
        crossTurtle.down()
        crossTurtle.right(90)
        crossTurtle.forward(160)
        crossTurtle.up()

class GameManager:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.onscreenclick(self.handle_click)

    def handle_click(self, x, y):
        DrawAction(x, y)
    

def main():
    turtle.title("Tic-tac-toe")  # Setting the title
    
    # Display window manipulation
    turtle.setup(600, 600)
    turtle.bgcolor("black")

    # Setting up the grid
    backGround = Grid()
    backGround.set_turtles()
    backGround.draw_row_columns()

    game_manager = GameManager()
    
    
    # To run the program till the end
    turtle.mainloop()


if __name__ == "__main__":
    main()



