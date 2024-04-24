#imports
import stddraw
import enemyManager
import player
import Image
import enemy
import sys

Lives = 3 # Player lives

def showTitleScreen(title): # function to show title or help screen
    # Avoid error when setting canvas size more than once
    try:
         stddraw.setCanvasSize(700,750)
    except: Exception    

    stddraw.setXscale(0,1) 
    stddraw.setYscale(0,1) 

    #Pepare canvas and format text
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontFamily('INVASION2000')
    
    # Check if the title scrren or help screen should be displayed
    stddraw.setFontSize(24)
    if title == True: 
        stddraw.text(.5,.9,'COSMIC CONQUISTADORS')
        stddraw.setFontSize(20)
        stddraw.text(.5, .1, 'Press [S] to start')
    else: #H
        stddraw.text(.5,.9,'HELP') 
        stddraw.setFontSize(20)
        stddraw.text(.5, .1, 'Press [S] to continue')

    stddraw.text(.5, .8, 'Instructions:')
    stddraw.setFontSize(16)
    stddraw.text(.5, .7, '[A] move left, [D] move right ')
    stddraw.text(.5, .6, '[J] rotate left, [L] rotate right') 
    stddraw.text(.5, .5, '[Space] to shoot')
    stddraw.text(.5, .4, '[H] for help')
    stddraw.text(.5, .3, '[Q] to quit')

    # Show the screen untill the user inputs 's' to start/continue or 'q' to quit the game     
    while True: 
        if stddraw.hasNextKeyTyped():
            k = stddraw.nextKeyTyped()
            if k == 's':
                title = False
                break
            if k == 'q':
                sys.exit()
        stddraw.show(0) 

def main():
    
    player1 = player.Player(5,1) # create player object

    #Initialise level normaly if not boss level
    if enemy.level != 5 : 
         
        direction = 1
        if enemy.level == 1:
           showTitleScreen(True)
           stddraw.setXscale(-1,11) 
           stddraw.setYscale(-1,11) 

         
        enemyManager.createEnemies(enemy.level)
        Image.RefreshBackground()
        Image.RefreshPlayer(5,1)
        enemy.display_score()
        enemyManager.move_enemy_into_start_pos(enemyManager.enemyArr) # move enemies into position(Animation)

                  
    if enemy.level == 5 :  
            boss_obj = enemy.Boss(5,13)
            #Move boss into position(Animation)
            for i in range(100):
                Image.RefreshBackground()
                boss_obj.y += -0.05
                Image.RefreshPlayer(boss_obj.x,boss_obj.y)
                Image.RefreshPlayer(5,1)
                enemy.display_score()
                stddraw.show(10)  
            stddraw.show(500)

            enemyManager.Number_Of_Enemies+=1
    
    #Main game loop
    while True:
        Image.RefreshBackground()    
        player1.move()        
        
        #Code to run for normal levels
        if enemy.level != 5:  
            enemyManager.moveEnemies(direction) 
            enemyManager.EnemyFire()
          
            # When an enemy reaches a boundary change the direction of all the enemies and move all enemies down one unit
            if enemyManager.checkBoundaries(): 
                enemyManager.moveDown()
                direction *= -1
           
          
            enemy.display_score()
            enemyManager.checkHit()
            enemy.level_over()
          
        # code to run if boss level
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
