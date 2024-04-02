import sys
import stdio
import stddraw
import color
import math
stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.hitTarget = False

    def bulletMove(self):
        self.x += 0.1*math.cos(math.radians(self.angle))
        self.y += 0.1*math.sin(math.radians(self.angle))
        stddraw.setPenRadius(0.01)
        stddraw.point(self.x,self.y)
        
def main():
    bullet1 = Bullet(5,1, 45)
    while True:
        stddraw.clear()
        bullet1.bulletMove()
        stddraw.show(20)


if __name__ == '__main__':
    main()
