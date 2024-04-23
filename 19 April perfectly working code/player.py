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
            
            if key == 'h': 
                Main.showTitleScreen(False) 
                stddraw.setXscale(-1,11) 
                stddraw.setYscale(-1,11) 
            elif key == 'q': 
                sys.exit()     

        #Change to live input Moving Shooting rotating
        key1 = stddraw.getKeysPressed()
        if key1[stddraw.K_a] and not key1[stddraw.K_d] and self.x > 0.1:
            self.x += -0.2
        elif key1[stddraw.K_d] and not key1[stddraw.K_a] and self.x < 10:
            self.x += 0.2
        
        if key1[stddraw.K_j] and not key1[stddraw.K_l] and self.angle < 135 :
            self.angle += 3
        elif key1[stddraw.K_l] and not key1[stddraw.K_j] and self.angle > 45 :
            self.angle -= 3
        
        if key1[stddraw.K_SPACE] and (current_time - last_time >= timeout) :
            shoot = True
            last_time = current_time

        
        if shoot:
            enemyManager.createBullet(self.x,self.y, self.angle)
            thread = Thread(target=play_sound) #H Code from : https://stackoverflow.com/questions/52769618/how-can-i-play-a-sound-while-other-lines-of-code-execute-simultaneously
            thread.start()
         
        Image.RefreshPlayer(self.x,self.y)
        
        radialAngle = (math.radians(self.angle))
        stddraw.setPenColor(GRAY)
        stddraw.setPenRadius(0.07)
        stddraw.line(self.x, self.y, (0.5*math.cos(radialAngle)+self.x), (0.5*math.sin(radialAngle)+self.y))

        moveLeft = False
        moveRight = False

    def checkPlayerHit(self):
        for EBullet in enemyManager.EbulletArr:
            if  abs(EBullet.x- self.x ) <= 0.4 and abs(EBullet.y-self.y) <= 0.4:
                Main.Lives += -1
                enemyManager.EbulletArr.remove(EBullet)
                
                if Main.Lives <= 0:
                    Image.BigExplosion(self.x,self.y)
                    enemy.game_over_anim('L')
                    enemy.game_over('L')
                else:
                    Image.Explosion(self.x,self.y)
                    stddraw.show(40)
        
if __name__ == "__main__":
    main()