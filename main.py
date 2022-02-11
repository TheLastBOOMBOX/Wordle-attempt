# Use Curses
import curses
#creates screen
screen = curses.initscr()        
#initialises colour uses
curses.start_color()

#creates frequently used colour that are callable
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)


# Codes for the printing of a single cells,allong with editing it

class Cell:
    
    def __init__(self,row,column):
        self.row = row
        self.column = column
    
    def draw(self,colour,letter):
        self.letter = letter
        screen.addstr(self.row*3,self.column*6," ___",curses.color_pair(colour))
        screen.addstr((self.row*3)+1,self.column*6,f"¦ {self.letter} ¦",curses.color_pair(colour))
        screen.addstr((self.row*3)+2,self.column*6,"¦___¦",curses.color_pair(colour))

#Grid is the list holding all cells      
grid = [[Cell(row,column) for column in range(5) ] for row in range(6)]





class Graphics:
    def __init__(self,WOTD_List,Inputted_List,position):
        self.WOTD_List = WOTD_List
        self.Inputted_List = Inputted_List
        self.position = position
    def Checker(self):
        if self.WOTD_List[self.position] == self.Inputted_List[self.position]:
            colour = 1
        elif self._List[self.position] in self.Inputted_List:
            colour = 2
        else:
            colour = 3
    def Grid():
        screen.addstr(str([Cell(row,column) for column in range(5)] for row in range(5)))


      
          
Graphics.Grid()




screen = curses.initscr()
screen.addstr(str(len(grid[1])))
screen.refresh()

c=screen.getch()
grid[0][0].draw(4,chr(c))
screen.refresh()



   
#https://www.devdungeon.com/content/curses-programming-python