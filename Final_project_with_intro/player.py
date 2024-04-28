#imports
import stddraw
import sys
import math
import enemyManager
import Image
import Main
import stdaudio
import time
import enemy

from threading import Thread
from color import GRAY 

last_time = 0 # last time the player has shot a bullet
time_out = 0.5 # time before player can shoot again

stddraw.setXscale(-1, 11)
stddraw.setYscale(-1, 11)


def play_sound(): # function to play sound
    stdaudio.playFile('Shoot')  

def main(): # Joshua : Not sure if this function is needed, was only for testing player.
    player = Player(5,1)
    while True:
        Image.RefreshBackground
        player.move()
        stddraw.show(20)

class Player:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self.angle = 90

    def move(self):
        global  last_time # Tom try to replace the global variables

        Image.RefreshBackground() # refresh background
        shoot = False 
        current_time = time.time() # update the current time

        if stddraw.hasNextKeyTyped(): # check if there is input form user
            key = stddraw.nextKeyTyped() # input key stored in key
            if key == 'h': 
                Main.showTitleScreen(False) # show the help screen instead of the main title screen
                stddraw.setXscale(-1,11) # revert the scale back to the game screen scale
                stddraw.setYscale(-1,11) # 
            elif key == 'q': 
                sys.exit()    # quit game 

        #Live movement
        key1 = stddraw.getKeysPressed()
        if key1[stddraw.K_a] and not key1[stddraw.K_d] and self.x > 0.1: 
            self.x += -0.2 # Move player left while holding a key
        elif key1[stddraw.K_d] and not key1[stddraw.K_a] and self.x < 10:
            self.x += 0.2 # Move player right while holding d key
        
        if key1[stddraw.K_j] and not key1[stddraw.K_l] and self.angle < 135 :
            self.angle += 3 # rotate gun left while holding j key
        elif key1[stddraw.K_l] and not key1[stddraw.K_j] and self.angle > 45 :
            self.angle -= 3 # rotate gun right while holding l key
        
        if key1[stddraw.K_SPACE] and (current_time - last_time >= time_out) : # only be able to fire a bullet after time_out has passed
            shoot = True
            last_time = current_time # update last time

        
        if shoot:
            enemyManager.createBullet(self.x,self.y, self.angle) # Create bullet object at player coordinates
            thread = Thread(target=play_sound) # play sound of player shooting
            thread.start()
         
        Image.RefreshPlayer(self.x,self.y)
        
        #Create player gun
        radial_angle = (math.radians(self.angle))
        stddraw.setPenColor(stddraw.RED) 
        stddraw.setPenRadius(0.005)
        
        for i in range (4): # loop to draw 4 dots representing the gun
            stddraw.point(self.x+ i*0.3*math.cos(radial_angle),self.y+ i*0.3*math.sin(radial_angle))


    def checkPlayerHit(self):
        for EBullet in enemyManager.EbulletArr:
            if  abs(EBullet.x- self.x ) <= 0.4 and abs(EBullet.y-self.y) <= 0.4: # check if th enemy bullet is in the players hitbox
                Main.Lives += -1 # deduct a player life
                enemyManager.EbulletArr.remove(EBullet) # delete the enemy bullet that hit the player
                
                
                if Main.Lives <= 0: # Check if the player has no lives left
                    Image.BigExplosion(self.x,self.y) # big explosion to indicate player has died
                    enemy.game_over_anim('L') # Flashing game over animation
                    enemy.game_over('L') # Game over function
                else:
                    Image.Explosion(self.x,self.y) # small explosion to indicate player is hit
                    stddraw.show(40) # show the small explosion
        
if __name__ == "__main__":
    main()