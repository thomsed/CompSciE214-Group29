#imports
import enemy
import bullet
import math
import sys
import stdio
import stddraw
import color
from color import WHITE
from color import RED
stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)
stddraw.setPenColor(RED)

import enemy
import stdio
import stddraw
import color
global direction

enemyArr = []
bulletArr = []
def createEnemies():
        for y in range(3):
            for x in range(5):
                enemy_obj = enemy.Enemy(x, 10 - y)  # Adjust y-coordinate to fit the grid
                enemyArr.append(enemy_obj)
def checkBoundaries():
    # Check if any enemy has reached the boundaries
    for enemy in enemyArr:
        if enemy.x <= 0 or enemy.x >= 10:
            return True
    return False

def checkLost():
    for enemy in enemyArr:
        if enemy.y <= 1:
            break


def moveEnemies(direction):
    for enemy in enemyArr:
        enemy.move(direction)

def moveDown():
    for enemy in enemyArr:
        enemy.moveDown()

def createBullet(x,y,angle):
    bullet_obj = bullet.Bullet(x,y,angle)
    bulletArr.append(bullet_obj)

def checkHit():
    for bullet in bulletArr:
        for enemy in enemyArr:
            #for a circle of radius 0.45, a 0.31x0.31 square roughly approximates its area,
            #making a hitbox far easier to calculate
            if  abs(bullet.x-enemy.x) <= 0.31 and abs(bullet.y-enemy.y) <= 0.31:
                enemy.hit()
                enemyArr.remove(enemy)
                bulletArr.remove(bullet)
                
def moveBullet():
    for bullet in bulletArr:
            bullet.bulletMove()


def main():
    
    stddraw.setPenColor(color.RED)
    createEnemies()
    createBullet(1,1,44)
    createBullet(1,1,44)
    createBullet(10,8,90)
    while True:
        stddraw.clear()
        moveEnemies(1)
        for bullet in bulletArr:
            bullet.bulletMove()
            checkHit()
        stddraw.show(20)
    


if __name__ == '__main__':
    main()