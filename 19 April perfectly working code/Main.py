#imports
import stddraw
import enemyManager
import player
import Image
import enemy
import sys



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
    try:
         stddraw.setCanvasSize(700,750)
    except: Exception    

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
    stddraw.text(.5, .7, '[A] move left, [D] move right ')
    stddraw.text(.5, .6, '[J] rotate left, [L] rotate right') #H:I just changed this to correlate with the actual key
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
            if k == 'q':
                sys.exit()
        stddraw.show(0) #H:

def main():
    
    player1 = player.Player(5,1)

    if enemy.level != 5 : 

         direction = 1
         if enemy.level == 1:
           showTitleScreen(True)
           stddraw.setXscale(-1,11) #H:
           stddraw.setYscale(-1,11) #H:

         if enemy.level != 5: #change back to 5
                enemyManager.createEnemies(enemy.level)
                Image.RefreshBackground()
                Image.RefreshPlayer(5,1)
                enemy.display_score()
                enemyManager.move_enemy_into_start_pos(enemyManager.enemyArr)

                  
    if enemy.level == 5 :  
            boss_obj = enemy.Boss(5,13)
            #Move boss into pos
            for i in range(100):
                Image.RefreshBackground()
                boss_obj.y += -0.05
                Image.RefreshPlayer(boss_obj.x,boss_obj.y)
                Image.RefreshPlayer(5,1)
                enemy.display_score()
                stddraw.show(10)  
            stddraw.show(500)

            enemyManager.Number_Of_Enemies+=1

    while True:
        Image.RefreshBackground()    
        player1.move()        
      
        
        if enemy.level != 5:  
           enemyManager.moveEnemies(direction) 
           enemyManager.EnemyFire()
          

           if enemyManager.checkBoundaries(): 
            enemyManager.moveDown()
            direction *= -1
           
          
           enemy.display_score()
           enemyManager.checkHit()
          
       
        if enemy.level == 5:
            boss_obj.Move()
            boss_obj.Fire()
            boss_obj.checkHit()
            enemy.display_score()
            boss_obj.showHealth()

        enemyManager.is_BulletOut()
        enemyManager.moveEbullet()
        enemyManager.moveBullet()
        player1.checkPlayerHit()
        enemyManager.checkLost()
        stddraw.show(10)

if __name__ == '__main__': 
    main()
