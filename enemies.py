#imports
import sys
import stdio
import stddraw
import color
from color import WHITE
from color import RED


stddraw.setXscale(0,10)
stddraw.setYscale(0,10)
stddraw.setPenColor(RED)

def main():
    createEnemies()
   # e = createEnemies()
    #stddraw.filledCircle
    #stddraw.show()



def createEnemies():
    enemies = []
    stddraw.setPenColor(RED)
    for y in range(3):
        for x in range(5):
            enemy = stddraw.filledCircle((x+1),10-(y+1), 0.45)
            enemies.append(enemy)
    stddraw.show()
   # return enemies


if __name__ == '__main__': main()