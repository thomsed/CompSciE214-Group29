#imports
import stddraw
import math
import Image

stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.hitTarget = False

    def bulletMove(self):
        self.x += 0.2*math.cos(math.radians(self.angle))
        self.y += 0.2*math.sin(math.radians(self.angle))
        Image.RefreshBullet(self.x,self.y)
        

class EBullet:
    def __init__(self,x,y,angle = 270):
        self.x = x
        self.y = y
        self.angle = angle
        self.hitPlayer = False

    def EbulletMove(self):
        self.x += 0.2*math.cos(math.radians(self.angle))
        self.y += 0.2*math.sin(math.radians(self.angle))
        Image.RefreshEBullet(self.x,self.y)
        
def main():
    stddraw.show()


if __name__ == '__main__':
    main()
