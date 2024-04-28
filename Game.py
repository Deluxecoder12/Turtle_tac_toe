import turtle

# Defines how the turtles are made
class myTurtle:
    def __init__(self, x, y, pspeed, pcolor, pshape, pwidth, visible=True) -> None:
        self.x, self.y = x, y
        self.pspeed = pspeed
        self.pcolor = pcolor
        self.pshape = pshape
        self.pwidth = pwidth
        self.visible = visible

    # Defining a turtle
    def define_turtle(self):
        pname = turtle.Turtle(visible=self.visible)
        pname.up()
        pname.color(self.pcolor)
        pname.speed(self.pspeed)
        pname.width(self.pwidth)
        pname.setposition(self.x, self.y)
        pname.shape(self.pshape)
        return pname

# For the Grid
class Grid:
    # Turtles to control the row and column
    def __init__(self):
        self.columnTurtle = [myTurtle(-100, 300, 5, "yellow", "arrow", 5).define_turtle() for i in range(2)]
        self.rowTurtle = [myTurtle(-300, 100, 5, "red", "arrow", 5).define_turtle() for i in range(2)]
        self.set_turtles()
        self.draw_row_columns()

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

# For drawing the user input
class DrawAction:
    def __init__(self, x, y, count) -> None:
        self.x = x
        self.y = y
        self.count = count
        self.det_turn()
            
    # Determine the turn
    def det_turn(self):
        if self.count % 2:
            self.draw_cross()
        else:
            self.draw_circle()
        self.count += 1

    # Draw circle or cross
    def draw_circle(self):
        circleTurtle = myTurtle(self.x, self.y - 70, 10, "white", "arrow", pwidth = 7).define_turtle()
        circleTurtle.hideturtle()
        circleTurtle.down()
        circleTurtle.circle(70)
        circleTurtle.up()

    def draw_cross(self):
        crossTurtle = myTurtle(self.x, self.y, 10, "white", "arrow", pwidth = 8).define_turtle()
        crossTurtle.hideturtle()
        crossTurtle.down()
        crossTurtle.left(45)
        crossTurtle.forward(90)
        crossTurtle.backward(180)
        crossTurtle.up()
        crossTurtle.left(45)
        crossTurtle.forward(130)
        crossTurtle.down()
        crossTurtle.right(135)
        crossTurtle.forward(180)
        crossTurtle.up()

# Handles the flow of the game
class GameManager:
    def __init__(self):
        self.reset_game()

    # Set up game
    def reset_game(self):
        # Window setup
        self.window = turtle.Screen()
        self.window.clear()
        self.window.bgcolor("black")
        self.window.title("Tic-tac-toe")
        
        self.count = 0
        self.input_matrix = [[0] * 3 for _ in range(3)]
        self.draw_lock = False
        
        # Setting up the grid
        backGround = Grid()

        self.window.onscreenclick(self.handle_click)
        self.display = myTurtle(0, 0, 10, "yellow", "arrow", 5, False).define_turtle()
        self.display.penup()
        self.display.hideturtle()

    # Set x, y to get the proper square and the matrix position
    def fxn(self, coord):
        if -350.0 <= coord < -100.0:
            return -200, 0
        elif -100.0 <= coord < 100.0:
            return 0, 1
        elif 100.0 <= coord < 350.0:
            return 200, 2
        return coord

    # Handles user input
    def handle_click(self, x, y):
        if not self.draw_lock:
            self.draw_lock = True
            x, list_x = self.fxn(x)
            y, list_y = self.fxn(y)
            if self.input_matrix[list_x][list_y] == 0:
                self.count += 1
                self.input_matrix[list_x][list_y] = (self.count % 2) + 1
                DrawAction(x, y, self.count)
                
                winner, winner_symbol = self.check_win()  # Capture both return values
                if winner:
                    message = f"Winner is {'O' if winner_symbol == 1 else 'X'}"
                    self.game_over(message)
                elif self.count == 9:
                    self.game_over("No winner")

            self.draw_lock = False

    # Checks for wins and loses
    def check_win(self):
        if self.count > 3:
            for i in range(3):
                if self.input_matrix[i][0] == self.input_matrix[i][1] == self.input_matrix[i][2] != 0:
                    return True, self.input_matrix[i][0]
                if self.input_matrix[0][i] == self.input_matrix[1][i] == self.input_matrix[2][i] != 0:
                    return True, self.input_matrix[0][i]

            # Check diagonals
            if self.input_matrix[0][0] == self.input_matrix[1][1] == self.input_matrix[2][2] != 0:
                return True, self.input_matrix[0][0]
            if self.input_matrix[0][2] == self.input_matrix[1][1] == self.input_matrix[2][0] != 0:
                return True, self.input_matrix[0][2]
        return False, None
    
    # Game Over Prompt
    def game_over(self, message):
        self.display.goto(0, 0)
        self.display.write(message, align="center", font=("Arial", 16, "normal"))
        self.display.goto(0, -30)
        self.display.write("Click to restart or right-click to exit", align="center", font=("Arial", 16, "normal"))
        # Use lambda to ignore x, y
        self.window.onscreenclick(lambda x, y: self.reset_game())  # Left-click to restart
        self.window.onscreenclick(lambda x, y: self.window.bye(), 3)  # Right-click to exit
    
def main():
    game_manager = GameManager()
    
    # To run the program till the end
    turtle.mainloop()

if __name__ == "__main__":
    main()



