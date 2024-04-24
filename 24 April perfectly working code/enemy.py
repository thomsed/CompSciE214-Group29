#imports
import stddraw
import enemy
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

last_time_fired = 0 # last time the boss fired
last_time_moved = 0 # last time the boss moved
time_out_move = 0.3 # time the boss has to wait before moving again
time_out_fire = 2 # time the boss has to wait before firing again
next_move=[5,8] # boss next move initialized to starting position

score = [0,0,0] # score array 
high_score = [0,0,0] # highscore array
level = 1 
velocity = 0.04

def play_sound(): #function to play sound
    stdaudio.playFile('invaderkilled') 

def game_over(W_or_L): # function is run when game is over

    global score, high_score, level # Joshua : Tom do your magic
    
    # game over when lost
    if W_or_L == 'L':
        stdaudio.playFile('explosion') 
        stddraw.show(100)
        #draw the game over screen
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontSize(100)
        stddraw.text(5,8,'GAME OVER')
        
    else:
        #game over when won
        stdaudio.playFile('explosion') 
        stddraw.show(100)

        # draw the game won screen
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.setFontSize(100)
        stddraw.text(5,8,'GAME WON !')

    # display score    
    strscore = ''
    for i in range(3):
        strscore += str(score[i])
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontSize(40)
    stddraw.text(5,4.5,'SCORE ' + strscore)
    # display continue instructions
    stddraw.setFontSize(30)
    stddraw.text(5,1,'PRESS [C] TO CONTINUE')

    # build score integer
    score_num = score[0] * 100 + score[1] * 10 + score[2]
    #build highscore integer
    highscore_num = high_score[0] * 100 + high_score[1] * 10 + high_score[2]
    if score_num > highscore_num: # Test if new highscore
        high_score = score[:]
        stddraw.text(5,2.5,'NEW HIGH SCORE!!!')

    #reset values
    score = [0,0,0]
    level = 1
    enemyManager.clear_lists()
    Main.Lives = 3
    enemyManager.Enemies_Destroyed = 0 
    enemyManager.Number_Of_Enemies = 0

    # Show the screen untill users inputs 'c'.Then run the main function
    done = False
    while done == False:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'c':
                break
        stddraw.show(0)
    Main.main()  

def level_over(): # function to check if a level is completed 
    global level # Joshua:  Tom Please replace the global variable

    # check if level is finished
    if enemyManager.Number_Of_Enemies == enemyManager.Enemies_Destroyed: #Check if all the enemies are destroyed
        level += 1
        enemyManager.Enemies_Destroyed = 0 #reset variable
        enemyManager.Number_Of_Enemies = 0 # reset variable
        enemyManager.clear_lists() 
        Main.main()

def game_over_anim(win_or_lose): # function to display an animation when the game is over

    if win_or_lose == 'W':
        # Green animation when game is won
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
        # Red animation when game is lost
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

def inc_score(): # function to increase score
    
    #increase score
    if score[2] < 9:
        score[2] += 1
    elif score[2] == 9 and score[1] < 9:
        score[2] = 0
        score[1] += 1
    elif score[2] == 9 and score[1] == 9:
        score[2] == 0
        score[1] == 0
        score[0] += 1

def display_score(): # function to display score, level , player lives and highscore
    # Draw blue bars at the top  and bottom of the screen
    stddraw.setPenColor(stddraw.DARK_BLUE)
    stddraw.filledRectangle(-1,10,12,2)
    stddraw.filledRectangle(-1,-2,12,2)

    # display score 
    strscore = ''
    for i in range(3): # build score string from score array
        strscore += str(score[i])
    stddraw.setFontSize(30)
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.text(1,-0.5,'SCORE: ' + strscore)

    #display level
    stddraw.setFontSize(35)
    stddraw.text(5,10.5,'LEVEL ' + str(level))

    #display highscore
    stddraw.setFontSize(30)
    strhighscore = ''
    for i in range(3): # loop to build highscore string
        strhighscore += str(high_score[i])
    stddraw.text(8,-0.5,'HIGH SCORE: ' + strhighscore)  

    #display player lives
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.setFontFamily('INVASION2000')
    stddraw.setFontSize(28)
    stddraw.text(0.5,10.5,'Lives: '+str(Main.Lives))

#main thus far used to test the enemy, will be run from the enemy manager class
def main():
    stddraw.show()

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 0.45 # enemy hitbox
        self.beenHit = False
        self.velocity = velocity * level* 0.6 # Increase the all the enemy speeds as the level increases

    def move(self, direction): # function to move enemies
        #Check direction to see whether the enemies should move left or right
        if direction == 1: # 
            self.x += self.velocity 
        if direction == -1:
            self.x -= self.velocity
        
        Image.RefreshEnemy(self.x,self.y)

    def moveDown(self):# function to move enemies down a level
        self.y -= 1

    def hit(self):
        # play target destroyed sound
        thread = Thread(target=play_sound) 
        thread.start() 
        # increase score when enemy is hit
        inc_score() 

class Boss:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Health = 6
        self.radius = 1
        self.velocity = 0.1
    
    def Move(self):
        global last_time_moved ,next_move # Joshua : Tom try to replace thes global variables please
        
        EnemyMoves = [[0,9.3],[5,9.3],[10,9.3],[0,7],[5,7],[10,7]] # Array of the boss's possible moves
        current_time = time.time() # update current time

        if (current_time - last_time_moved >= time_out_move): # check the time to see if the boss can move to a new position

            while ((self.x - 0.1 < next_move[0] < self.x + 0.1) and (self.y - 0.1 < next_move[1] < self.y + 0.1)): # Check that the next move is not the last move it made
                 next_move = EnemyMoves[random.randrange(6)]
            last_time_moved = current_time # updaate the time the boss last moved
            
        
        abs_distance = math.sqrt((next_move[0]-self.x)**2+(next_move[1]-self.y)**2) # Distance from the boss's current position to its next move position
        angle = math.atan2(next_move[1]-self.y , next_move[0]-self.x) #  angle in radians, from boss's current position to its next move position
        
        # update the boss's position(Proportional to the current distance between the boss's current position and the next move)
        self.x = self.x + abs_distance * math.cos(angle)*0.05 
        self.y = self.y + abs_distance * math.sin(angle)*0.05

        Image.RefreshPlayer(self.x,self.y)
    
    def Fire(self):
        global last_time_fired # Joshua : Tom try to replace these please
        current_time = time.time() # update the current time
        if current_time - last_time_fired >= time_out_fire : # check the time to see if the boss can fire again 
            #create ten bullets fired in a half circle from the boss
            for i in range(210,345,15): 
                enemyManager.createEBullet(self.x,self.y-0.2,i) # create enemy bullet object

            last_time_fired = current_time # update last time boss fired

    def checkHit(self): # function to check if boss has been hit by a bullet
        for bullet in enemyManager.bulletArr:
             if  abs(bullet.x- self.x ) <= 0.4 and abs(bullet.y-self.y) <= 0.4: # check if the player bullet is in the enemy hitbox
                self.Health -=1 # decrease boss's health
                enemyManager.bulletArr.remove(bullet) # delete the bullet object that hit the boss
                 
                if self.Health <=0: # check if boss has been defeated
                    #Win game
                    Image.BigExplosion(self.x,self.y)
                    enemy.game_over_anim('W') # game winning animation
                    enemy.game_over('W')  # game over function : win
                else:
                    Image.Explosion(self.x,self.y) # show an explosion to indicate the boss has been hit


    def showHealth(self) : # function to show the boss's health
         #show the boss health
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontFamily('INVASION2000')
        stddraw.setFontSize(20)
        stddraw.text(8.8,10.5,'Boss Health :'+str(self.Health))           
        

if __name__ == '__main__': main()