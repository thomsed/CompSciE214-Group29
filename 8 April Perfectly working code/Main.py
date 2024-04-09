#imports
import stddraw
import enemyManager
import player
import Image
import enemy



from color import WHITE
from color import GREEN
from color import BLACK


#Text formatting
TITLE_FONT = 24
SUBTITLE_FONT = 20
TEXT_FONT = 16
FONT_CHOICE = 'INVASION2000'
FONT_COLOR = WHITE

Lives = 3




def showTitleScreen(title):
    
    
    stddraw.setXscale(0,1) #H:
    stddraw.setYscale(0,1) #H:
    stddraw.setPenColor(BLACK)
    stddraw.clear(BLACK)
    stddraw.filledSquare(.5,.5,.5)
    stddraw.setPenColor(GREEN)
    stddraw.setFontFamily(FONT_CHOICE)
    stddraw.setFontSize(TITLE_FONT)
    if title == True: #H
        stddraw.text(.5,.9,'COSMIC CONQUISTADORS')
    else: #H
        stddraw.text(.5,.9,'HELP') #H
    stddraw.setFontSize(SUBTITLE_FONT)
    stddraw.text(.5, .8, 'Instructions:')
    stddraw.setFontSize(TEXT_FONT)
    stddraw.text(.5, .7, '[A] move left, [S] stop move, [D] move right ')
    stddraw.text(.5, .6, '[J] rotate left, [K] stop rotate, [L] rotate right') #H:I just changed this to correlate with the actual key
    stddraw.text(.5, .5, '[Space] to shoot')
    stddraw.text(.5, .4, '[H] for help')
    stddraw.text(.5, .3, '[Q] to quit')
    stddraw.setFontSize(SUBTITLE_FONT)
    if title == True: #H
        stddraw.text(.5, .1, 'Press [S] to start') #H: made it s
    else: #H
        stddraw.text(.5, .1, 'Press [S] to continue') #H
    while True: #H:
        if stddraw.hasNextKeyTyped():
            k = stddraw.nextKeyTyped()
            if k == 's':
                title = False
                break
        stddraw.show(0) #H:


    

def main():
    direction = 1
    if enemy.level == 1:
     showTitleScreen(True)
    stddraw.setXscale(-1,11) #H:
    stddraw.setYscale(-1,11) #H:
    enemyManager.createEnemies(3,5)
    player1 = player.Player(5,1)

   
    while True:
        Image.RefreshBackground()     
        player1.move()        
        enemyManager.moveEnemies(direction) 

        enemyManager.EnemyFire()
        enemyManager.moveEbullet()

        if enemyManager.checkBoundaries(): 
            enemyManager.moveDown()
            direction *= -1
        enemyManager.moveBullet()
        enemy.display_score()
        enemyManager.checkHit()
        enemy.display_score()
    
        enemyManager.is_BulletOut()

        player1.checkPlayerHit()
        enemyManager.checkLost()
        stddraw.show(10)

if __name__ == '__main__': 
    main()
