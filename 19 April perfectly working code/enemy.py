#imports
import stddraw
import enemy
import stdio
import Image
import stdaudio
import enemyManager
import Main
import time
import random
import math
from threading import Thread

#giving an additional .1 spacing on the border of the screen, but the working area is a 10x10 grid.
stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)
Last_time = 0
last_time = 0
time_out = 0.3
Pause = 2
next_move=[5,8]

score = [0,0,0] #H
high_score = [0,0,0]
level = 1
velocity = 0.04

def play_sound(): #H
    stdaudio.playFile('invaderkilled') #H: .wav file from https://www.classicgaming.cc/classics/space-invaders/sounds

def game_over(W_or_L): #H
    global score, high_score, level
    stddraw.setXscale(-1,11)
    stddraw.setYscale(-1,11)
    
    if W_or_L == 'L':
        stdaudio.playFile('explosion') #H: .wav file from https://classicgaming.cc/classics/space-invaders/sounds
        stddraw.show(100)
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontSize(100)
        stddraw.text(5,8,'GAME OVER')
        stddraw.setPenColor(stddraw.GREEN)
    else:
        stdaudio.playFile('explosion') #H: .wav file from https://classicgaming.cc/classics/space-invaders/sounds
        stddraw.show(100)
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.setFontSize(100)
        stddraw.text(5,8,'GAME WON !')
        stddraw.setPenColor(stddraw.GREEN)

    strscore = ''
    for i in range(3):
        strscore += str(score[i])
    stddraw.setFontSize(40)
    stddraw.text(5,4.5,'SCORE ' + strscore)
    stddraw.setFontSize(30)
    stddraw.text(5,1,'PRESS [C] TO CONTINUE')

    score_num = score[0] * 100 + score[1] * 10 + score[2]
    highscore_num = high_score[0] * 100 + high_score[1] * 10 + high_score[2]
    if score_num > highscore_num:
        high_score = score[:]
        stddraw.text(5,2.5,'NEW HIGH SCORE!!!')

    #reset values
    score = [0,0,0]
    level = 1
   # stddraw.setPenColor(stddraw.BLACK)
    enemyManager.clear_lists()
    Main.Lives = 3
    enemyManager.Enemies_Destroyed = 0 
    enemyManager.Number_Of_Enemies = 0

    done = False
    while done == False:
        if stddraw.hasNextKeyTyped():
            k = stddraw.nextKeyTyped()
            if k == 'c':
                break
        stddraw.show(0)
    Main.main()  

def game_over_anim(win_or_lose):

    if win_or_lose == 'W':
        for i in range(4):
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledRectangle(-1,10,12,2)
            stddraw.filledRectangle(-1,-2,12,2)

            stddraw.show(100)

            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledRectangle(-1,10,12,2)
            stddraw.filledRectangle(-1,-2,12,2)

            stddraw.show(100)

            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledRectangle(-1,10,12,2)
            stddraw.filledRectangle(-1,-2,12,2)

            stddraw.show(100)
    else:
        for i in range(4):
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledRectangle(-1,10,12,2)
            stddraw.filledRectangle(-1,-2,12,2)

            stddraw.show(100)

            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledRectangle(-1,10,12,2)
            stddraw.filledRectangle(-1,-2,12,2)

            stddraw.show(100)

            stddraw.setPenColor(stddraw.RED)
            stddraw.filledRectangle(-1,10,12,2)
            stddraw.filledRectangle(-1,-2,12,2)

            stddraw.show(100)

def inc_score(): #H
    global level
    if score[2] < 9:
        score[2] += 1
    elif score[2] == 9 and score[1] < 9:
        score[2] = 0
        score[1] += 1
    elif score[2] == 9 and score[1] == 9:
        score[2] == 0
        score[1] == 0
        score[0] += 1

    if enemyManager.Number_Of_Enemies == enemyManager.Enemies_Destroyed:                                    #Change 15 to a variable that holds the numbr of enemies in the level
        level += 1
        enemyManager.Enemies_Destroyed = 0
        enemyManager.Number_Of_Enemies = 0
        enemyManager.clear_lists()
        Main.main()

def display_score(): #H

    stddraw.setPenColor(stddraw.DARK_BLUE)
    stddraw.filledRectangle(-1,10,12,2)
    stddraw.filledRectangle(-1,-2,12,2)

    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontFamily('INVASION2000')
    stddraw.setFontSize(30)
    strscore = ''
    for i in range(3):
        strscore += str(score[i])
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.text(1,-0.5,'SCORE: ' + strscore)
    stddraw.setFontSize(35)
    stddraw.text(5,10.5,'LEVEL ' + str(level))
    stddraw.setFontSize(30)
    stddraw.setPenColor(stddraw.YELLOW)
    strhighscore = ''
    for i in range(3):
        strhighscore += str(high_score[i])
    stddraw.text(8,-0.5,'HIGH SCORE: ' + strhighscore)  

    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.setFontFamily('INVASION2000')
    stddraw.setFontSize(28)
    stddraw.text(0.5,10.5,'Lives: '+str(Main.Lives))

#main thus far used to test the enemy, will be run from the enemy manager class
def main():
    stddraw.show()
# enemy object and its functions
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 0.45
        self.beenHit = False
        self.velocity = velocity * level* 0.6

    def move(self, direction):
        if direction == 1:
            self.x += self.velocity
        if direction == -1:
            self.x -= self.velocity
        
        Image.RefreshEnemy(self.x,self.y)

    def moveDown(self):
        self.y -= 1

    def hit(self):
        thread = Thread(target=play_sound) #H Code from : https://stackoverflow.com/questions/52769618/how-can-i-play-a-sound-while-other-lines-of-code-execute-simultaneously
        thread.start() #H
        if level !=5: #Lubbe change back
          inc_score() #

class Boss:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Health = 6
        self.radius = 1
        self.velocity = 0.1
    
    def Move(self):
        global last_time ,next_move
        
        EnemyMoves = [[0,9.3],[5,9.3],[10,9.3],[0,7],[5,7],[10,7]]
        current_time = time.time()

        if (current_time - last_time >= time_out):

            while ((self.x - 0.1 < next_move[0] < self.x + 0.1) and (self.y - 0.1 < next_move[1] < self.y + 0.1)):
                 next_move = EnemyMoves[random.randrange(6)]
            last_time = current_time
            stdio.writeln(str(self.x)+' '+str(self.y))
            
        
        abs_distance = math.sqrt((next_move[0]-self.x)**2+(next_move[1]-self.y)**2)
        angle = math.atan2(next_move[1]-self.y , next_move[0]-self.x) # in radians
        

        self.x = self.x + abs_distance * math.cos(angle)*0.05
        self.y = self.y + abs_distance * math.sin(angle)*0.05

        Image.RefreshPlayer(self.x,self.y)
    
    def Fire(self):
        global Last_time
        current_time = time.time()
        if current_time - Last_time >= Pause :
            Last_time = current_time
            for i in range(210,345,15):
                enemyManager.createEBullet(self.x,self.y-0.2,i)

    def checkHit(self):
        for bullet in enemyManager.bulletArr:
             if  abs(bullet.x- self.x ) <= 0.4 and abs(bullet.y-self.y) <= 0.4:
                self.Health -=1
                enemyManager.bulletArr.remove(bullet)
                 
                if self.Health <=0:
                    #Win game
                    Image.BigExplosion(self.x,self.y)
                    enemy.game_over_anim('W')
                    enemy.game_over('W')   
                else:
                    Image.Explosion(self.x,self.y)


    def showHealth(self) :
         #show the boss health
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontFamily('INVASION2000')
        stddraw.setFontSize(20)
        stddraw.text(8.8,10.5,'Boss Health :'+str(self.Health))           
        

if __name__ == '__main__': main()