#imports
import enemy
import bullet
import stddraw
import time
import random
import Image

global direction # unglobalise Tom (or else)

stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)

enemyArr = []             # array to store enemy objects
bulletArr = []            # array to  store player bullet objects
EbulletArr = []           # array to store enemy bullet objects
Last_time = 0             # last time enmy fired
Pause = 0.8               # time before another bullet is fired
Number_Of_Enemies = 0    
Enemies_Destroyed = 0

def move_enemy_into_start_pos(enemyArr): # function to move the enemies into their positions.(Animation)

    # The whole loop moves every enemy down 5 units from the position they where initialised at
    for i in range(100):
        Image.RefreshBackground()
        for enemy1 in enemyArr:
              enemy1.y += -0.05
              Image.RefreshEnemy(enemy1.x,enemy1.y)
              Image.RefreshPlayer(5,1)
              enemy.display_score()
        stddraw.show(10)  
          
def is_BulletOut(): # function to remove any bullets that are out of bounds
    # Check player bullet
    for bullet in bulletArr:
        if bullet.y >= 9.8 :
            bulletArr.remove(bullet)
    #Check enemy bullet
    for Ebullet in EbulletArr:
        if Ebullet.y <= 0.2 :
            EbulletArr.remove(Ebullet)

def clear_lists(): # function to clear enemies and bullets when the game is lost
    enemyArr.clear()
    bulletArr.clear()
    EbulletArr.clear()

def createEnemies(level): # Function to create enemies

    global Number_Of_Enemies # Tom, anada one
    
    # Create enemy objects according to the level
    if level == 1:
        for y in range(2):#2 rows of enemies
            for x in range(6):#6 columns of enemies
                enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                enemyArr.append(enemy_obj)
                Number_Of_Enemies += 1

    elif level == 2:
        for y in range(3):#3 rows of enemies
            for x in range(6):#6 columns of enemies
                enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                enemyArr.append(enemy_obj)
                Number_Of_Enemies+=1

    elif level == 3:
        for y in range(3):#3 rows of enemies
           for x in range (10):#10 columns of enemies
                if x not in [4,5] : # no enemies in 5th and 6th columns
                  enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                  enemyArr.append(enemy_obj)
                  Number_Of_Enemies+=1  
    
    elif level == 4:
        for y in range (3):#3 rows of enemies
            for x in range (9):#9 columns of enemies
                if x not in [1,4,7] and y not in [1]: # no enemies in the 2nd 5th and 8th columns , and 2nd row
                   enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                   enemyArr.append(enemy_obj)
                   Number_Of_Enemies+=1  

def checkBoundaries(): # Check if any enemy has reached the boundaries    
    for enemy in enemyArr:
        if enemy.x <= -0.56 or enemy.x >= 10.56:
            return True
    return False

def checkLost(): # Check if lost due to enemy position 
    for enemy1 in enemyArr:
        if enemy1.y <= 1:
            enemy.game_over_anim('L')
            enemy.game_over('L')
            
def moveEnemies(direction):# Move all enemies left/right
    for enemy in enemyArr:
        enemy.move(direction)

def moveDown(): # move all enemies down
    for enemy in enemyArr:
        enemy.moveDown()

def createBullet(x,y,angle): # create bullet object
    bullet_obj = bullet.Bullet(x,y,angle)
    bulletArr.append(bullet_obj)

def createEBullet(x,y,angle = 270): # create enemy bullet with default angle 270 degrees
    Ebullet_obj = bullet.EBullet(x,y,angle)
    EbulletArr.append(Ebullet_obj)

def checkHit(): # check if an enemy is hit
    global Enemies_Destroyed # YO Tom removing these global variables is going to be tricky

    for bullet in bulletArr:
        for enemy in enemyArr:
            #for a circle of radius 0.45, a 0.31x0.31 square roughly approximates its area, check hitbox
            if  abs(bullet.x-enemy.x) <= 0.31 and abs(bullet.y-enemy.y) <= 0.31:
                Enemies_Destroyed +=1
                enemy.hit()
                #Explosion when enemy is hit
                Image.Explosion(enemy.x,enemy.y)
                stddraw.show(40)
                #remove enmy and bullet
                enemyArr.remove(enemy)
                bulletArr.remove(bullet)

def EnemyFire(): # function to make an enemy fire
    global Last_time # the fight is lost Tom

    current_time = time.time() # update current time
    if current_time - Last_time >= Pause : # check if an enemy is allowed to fire
        
        # Pick a random enemy to fire a bullet if there are still enemies left, otherwise increase the score
        if len(enemyArr) !=0 :
          enemy1 = enemyArr[random.randrange(len(enemyArr))]
          createEBullet(enemy1.x,enemy1.y)
          Last_time = current_time # update last time
        else:
            enemy.inc_score()
                           
def moveBullet(): # function to move all player bullets
    for bullet in bulletArr:
        bullet.bulletMove()

def moveEbullet(): # function to move all enemy bullets
    for ebullet in EbulletArr:
        ebullet.EbulletMove()

def main(): # Dont know if this is necessary.Maybe necessary to test all functions
    stddraw.show()
    
if __name__ == '__main__':
    main()