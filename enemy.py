#imports
import sys
import stdio
import stddraw
import color
from color import WHITE
from color import RED

#giving an additional .1 spacing on the border of the screen, but the working area is a 10x10 grid.
stddraw.setXscale(-0.6,10.6)
stddraw.setYscale(-0.6,10.6)
stddraw.setPenColor(RED)

#main thus far used to test the enemy, will be run from the enemy manager class
def main():
    print("hello")
# enemy object and its functions
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 0.45
        self.beenHit = False
        self.velocity = 0.05
        self.color = RED

    def move(self, direction):
        if direction == 1:
            self.x += self.velocity
        if direction == -1:
            self.x -= self.velocity
        stddraw.filledCircle(self.x, self.y, self.RADIUS)

   

    def moveDown(self):
        self.y -= 1

    def hit(self):
        stdio.write('hit')
        
if __name__ == '__main__': main()