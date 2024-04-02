#imports
import sys
import stdio
import stddraw
import color
import math
import enemyManager
from color import WHITE
from color import RED
from color import BLUE
from color import BLACK


stddraw.setXscale(-1, 11)
stddraw.setYscale(-1, 11)

moveRight = False
moveLeft = False
rotateLeft = False
rotateRight = False
shoot = False

def main():
    player = Player(5,1)
    while True:
        stddraw.clear()
        player.move()
        stddraw.show(20)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 90

    def move(self):
        global moveRight, moveLeft, rotateLeft, rotateRight, shoot
        stddraw.clear()
        shoot = False
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'd':
                moveRight = True
                moveLeft = False
            elif key == 'a':  
                moveRight = False
                moveLeft = True
            elif key == 's':
                moveRight = False
                moveLeft = False
            elif key == 'j':
                rotateRight = False
                rotateLeft = True
            elif key == 'l':
                rotateRight = True
                rotateLeft = False
            elif key == 'k':
                rotateRight = False
                rotateLeft = False
            elif key == ' ':
                shoot = True
        if moveRight and self.x < 10:
            self.x += 0.1

        if moveLeft and self.x > 0:
            self.x -= 0.1

        if rotateRight and self.angle >= 45 :
            self.angle -= 2

        if rotateLeft and self.angle <= 135 :
            self.angle += 2
        if shoot:
            enemyManager.createBullet(self.x,self.y, self.angle)
        

        stddraw.setPenColor(BLUE)
        stddraw.setPenRadius()
        stddraw.filledCircle(self.x, self.y, 0.5)  # Draw the circle at updated position
        radialAngle = (math.radians(self.angle))
        stddraw.setPenColor(BLACK)
        stddraw.setPenRadius(0.07)
        stddraw.line(self.x, self.y, (0.5*math.cos(radialAngle)+self.x), (0.5*math.sin(radialAngle)+self.y))

if __name__ == "__main__":
    main()