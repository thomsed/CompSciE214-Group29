#imports
import sys
import stdio
import stddraw
import color
import enemyManager
import player
import bullet

from color import WHITE
from color import GREEN
from color import BLUE
from color import RED


#Text formatting
TITLE_FONT = 28
SUBTITLE_FONT = 24
TEXT_FONT = 20
FONT_CHOICE = 'NotJamSciMono13'
FONT_COLOR = WHITE

def showTitleScreen():
    stddraw.setCanvasSize(618,418)
    stddraw.filledSquare(.5,.5,.5)
    stddraw.setPenColor(GREEN)
    stddraw.setFontFamily(FONT_CHOICE)
    stddraw.setFontSize(TITLE_FONT)
    stddraw.text(.5,.9,'COSMIC CONQUISTADORS')
    stddraw.setFontSize(SUBTITLE_FONT)
    stddraw.text(.5, .8, 'Instructions:')
    stddraw.setFontSize(TEXT_FONT)
    stddraw.text(.5, .7, '[A] move left, [S] stop move, [D] move right ')
    stddraw.text(.5, .6, '[Q] rotate left, [W] stop rotate, [E] rotate right')
    stddraw.text(.5, .5, '[Space] to shoot')
    stddraw.text(.5, .4, '[H] for help')
    stddraw.text(.5, .3, '[X] to quit')
    stddraw.setFontSize(SUBTITLE_FONT)
    stddraw.text(.5, .1, 'Press any key to start')
    stddraw.show()

def main():
    direction = 1
 #  showTitleScreen()
    enemyManager.createEnemies()
    player1 = player.Player(5,1)
    while True:
        stddraw.clear()
        stddraw.setPenColor(RED)
        player1.move()
        stddraw.setPenColor(BLUE)
        enemyManager.moveEnemies(direction)
        if enemyManager.checkBoundaries(): 
            enemyManager.moveDown()
            direction *= -1
        enemyManager.moveBullet()
        enemyManager.checkHit()
        enemyManager.checkLost()
        stddraw.show(10)

if __name__ == '__main__': 
    main()
