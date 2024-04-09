#imports
import enemy
import bullet
import stddraw
import random
import Image

global direction

stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)

enemyArr = []
bulletArr = []
EbulletArr = []

def is_BulletOut():
    for bullet in bulletArr:
        if bullet.y >= 11 :
            bulletArr.remove(bullet)
    for Ebullet in EbulletArr:
        if Ebullet.y <= -1 :
            EbulletArr.remove(Ebullet)

def clear_lists(): #H: function to clear enemies and bullets when the game is lost
    enemyArr.clear()
    bulletArr.clear()
    EbulletArr.clear()


def createEnemies(row,col):
        for y in range(row):
            for x in range(col):
                enemy_obj = enemy.Enemy(x, 10 - y)  # Adjust y-coordinate to fit the grid
                enemyArr.append(enemy_obj)

def checkBoundaries():
    # Check if any enemy has reached the boundaries
    for enemy in enemyArr:
        if enemy.x <= -0.56 or enemy.x >= 10.56:
            return True
    return False

def checkLost():
    for enemy1 in enemyArr:
        if enemy1.y <= 1:
            enemy.game_over()

def moveEnemies(direction):
    for enemy in enemyArr:
        enemy.move(direction)

def moveDown():
    for enemy in enemyArr:
        enemy.moveDown()

def createBullet(x,y,angle):
    bullet_obj = bullet.Bullet(x,y,angle)
    bulletArr.append(bullet_obj)

def createEBullet(x,y):
    Ebullet_obj = bullet.EBullet(x,y)
    EbulletArr.append(Ebullet_obj)

def checkHit():
    for bullet in bulletArr:
        for enemy in enemyArr:
            #for a circle of radius 0.45, a 0.31x0.31 square roughly approximates its area,
            #making a hitbox far easier to calculate
            if  abs(bullet.x-enemy.x) <= 0.31 and abs(bullet.y-enemy.y) <= 0.31:
                enemy.hit()
                #Explosion when enemy is hit
                Image.Explosion(enemy.x,enemy.y)
                stddraw.show(40)
                

                enemyArr.remove(enemy)
                bulletArr.remove(bullet)

def EnemyFire():
    for enemy in enemyArr:
        if random.randrange(0,1000) >= 990:
            createEBullet(enemy.x,enemy.y)
                       
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