#imports
import stddraw
import sys
import math
import enemyManager
import Image
import Main
import stdaudio
import time
import enemy

from threading import Thread
from color import GRAY 

last_time = 0
timeout = 0.5

stddraw.setXscale(-1, 11)
stddraw.setYscale(-1, 11)

moveRight = False
moveLeft = False
rotateLeft = False
rotateRight = False
shoot = False

def play_sound():
    stdaudio.playFile('Shoot')  #.wav file from https://www.classicgaming.cc/classics/space-invaders/sounds

def main():
    player = Player(5,1)
    while True:
        Image.RefreshBackground
        player.move()
        stddraw.show(20)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 90

    def move(self):
        global moveRight, moveLeft, rotateLeft, rotateRight, shoot , last_time
        Image.RefreshBackground()
        shoot = False
        current_time = time.time()

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
            elif key == ' ' and (current_time - last_time >= timeout):
                shoot = True
                last_time = current_time
            elif key == 'h': #H
                Main.showTitleScreen(False) #H
                stddraw.setXscale(-1,11) #H
                stddraw.setYscale(-1,11) #H
            elif key == 'q': #H
                sys.exit() #H    

        if moveRight and self.x < 10:
            self.x += 0.15

        if moveLeft and self.x > 0:
            self.x -= 0.15

        if rotateRight and self.angle >= 45 :
            self.angle -= 2

        if rotateLeft and self.angle <= 135 :
            self.angle += 2
        if shoot:
            enemyManager.createBullet(self.x,self.y, self.angle)
            thread = Thread(target=play_sound) #H Code from : https://stackoverflow.com/questions/52769618/how-can-i-play-a-sound-while-other-lines-of-code-execute-simultaneously
            thread.start()
         
        Image.RefreshPlayer(self.x,self.y)
        
        radialAngle = (math.radians(self.angle))
        stddraw.setPenColor(GRAY)
        stddraw.setPenRadius(0.07)
        stddraw.line(self.x, self.y, (0.5*math.cos(radialAngle)+self.x), (0.5*math.sin(radialAngle)+self.y))

    def checkPlayerHit(self):
        for EBullet in enemyManager.EbulletArr:
            if  abs(EBullet.x- self.x ) <= 0.4 and abs(EBullet.y-self.y) <= 0.4:
                Main.Lives += -1
                enemyManager.EbulletArr.remove(EBullet)
                
                if Main.Lives <= -1:
                    Image.BigExplosion(self.x,self.y)
                    stddraw.show(200)
                    enemy.game_over()
                else:
                    Image.Explosion(self.x,self.y)
                    stddraw.show(40)
        

if __name__ == "__main__":
    main()