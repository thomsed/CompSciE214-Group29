#imports
import enemy
import bullet
import stddraw
import time
import random
import Image

global direction

stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)

enemyArr = []
bulletArr = []
EbulletArr = []
Last_time = 0
Pause = 0.8
Number_Of_Enemies = 0
Enemies_Destroyed = 0

def move_enemy_into_start_pos(enemyArr):
    for i in range(100):
        Image.RefreshBackground()
        for enemy1 in enemyArr:
              enemy1.y += -0.05
              Image.RefreshEnemy(enemy1.x,enemy1.y)
              Image.RefreshPlayer(5,1)
              enemy.display_score()
        stddraw.show(10)  
          
def is_BulletOut():
    for bullet in bulletArr:
        if bullet.y >= 9.8 :
            bulletArr.remove(bullet)
    for Ebullet in EbulletArr:
        if Ebullet.y <= 0.2 :
            EbulletArr.remove(Ebullet)

def clear_lists(): #H: function to clear enemies and bullets when the game is lost
    enemyArr.clear()
    bulletArr.clear()
    EbulletArr.clear()

def createEnemies(level): # Change this to create and then move the enemies down into their positions

    global Number_Of_Enemies
    if level == 1:
        for y in range(2):#2
            for x in range(2):#6
                enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                enemyArr.append(enemy_obj)
                Number_Of_Enemies += 1
    elif level == 2:
        for y in range(2):#3
            for x in range(2):#6
                enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                enemyArr.append(enemy_obj)
                Number_Of_Enemies+=1
    elif level == 3:
        for y in range(2):#3
           for x in range (2):#10
                if x not in [4,5] :
                  enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                  enemyArr.append(enemy_obj)
                  Number_Of_Enemies+=1  
    
    elif level == 4:
        for y in range (3):#3
            for x in range (9):#9
                if x not in [1,4,7] and y not in [1]:
                   enemy_obj = enemy.Enemy(x/1.2, 15 - (y/1.2)-0.5)  
                   enemyArr.append(enemy_obj)
                   Number_Of_Enemies+=1  

def checkBoundaries():
    # Check if any enemy has reached the boundaries
    for enemy in enemyArr:
        if enemy.x <= -0.56 or enemy.x >= 10.56:
            return True
    return False

def checkLost():
    
    for enemy1 in enemyArr:
        if enemy1.y <= 1:
            enemy.game_over_anim('L')
            enemy.game_over('L')
            
def moveEnemies(direction):
    for enemy in enemyArr:
        enemy.move(direction)

def moveDown():
    for enemy in enemyArr:
        enemy.moveDown()

def createBullet(x,y,angle):
    bullet_obj = bullet.Bullet(x,y,angle)
    bulletArr.append(bullet_obj)

def createEBullet(x,y,angle = 270):
    Ebullet_obj = bullet.EBullet(x,y,angle)
    EbulletArr.append(Ebullet_obj)

def checkHit():
    global Enemies_Destroyed
    for bullet in bulletArr:
        for enemy in enemyArr:
            #for a circle of radius 0.45, a 0.31x0.31 square roughly approximates its area,
            #making a hitbox far easier to calculate
            if  abs(bullet.x-enemy.x) <= 0.31 and abs(bullet.y-enemy.y) <= 0.31:
                Enemies_Destroyed +=1
                enemy.hit()
                #Explosion when enemy is hit
                Image.Explosion(enemy.x,enemy.y)
                stddraw.show(40)
                enemyArr.remove(enemy)
                bulletArr.remove(bullet)

def EnemyFire():
    global Last_time
    current_time = time.time()
    if current_time - Last_time >= Pause : 

        if len(enemyArr) !=0 :
          enemy1 = enemyArr[random.randrange(len(enemyArr))]
          createEBullet(enemy1.x,enemy1.y)
          Last_time = current_time
        else:
            enemy.inc_score()
                           
def moveBullet():
    for bullet in bulletArr:
        bullet.bulletMove()

def moveEbullet():
    for ebullet in EbulletArr:
        ebullet.EbulletMove()

def main():
    stddraw.show()
    
if __name__ == '__main__':
    main()