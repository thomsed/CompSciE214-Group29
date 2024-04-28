import stddraw
import picture as p

def RefreshBackground(): # function to refresh background
    pic_name ='Back ground.png' 
    backgroundImage_obj  = p.Picture(pic_name) # create picture object
    stddraw.picture(backgroundImage_obj) # draw picture object
   
def RefreshPlayer(x,y): # function to refresh player image
    pic_name ='Falcon.png' 
    playerImage_obj  = p.Picture(pic_name) # create picture object
    stddraw.picture(playerImage_obj,x,y) # draw picture object

def RefreshEnemy(x,y): # function to refresh enemy image
    enemyImage = 'Tie fighter.png'
    enemyImage_obj = p.Picture(enemyImage) # create picture object
    stddraw.picture(enemyImage_obj,x,y) # draw picture object

def RefreshBoss(x,y): # function to refresh boss image
    bossImage = 'Boss.png'
    boss_Image_obj = p.Picture(bossImage) # create picture object
    stddraw.picture(boss_Image_obj,x,y) # draw picture object

def RefreshBullet(x,y): # function to refresh player bullet
    bulletImage = "Bullet.png"
    bulletImage_obj = p.Picture(bulletImage) # create picture object
    stddraw.picture(bulletImage_obj,x,y) # draw picture object

def RefreshEBullet(x,y): # function to refresh enemy bullet
    EbulletImage = "EBullet.png"
    EbulletImage_obj = p.Picture(EbulletImage) # create picture object
    stddraw.picture(EbulletImage_obj,x,y) # draw picture object

def Explosion(x,y): # function to show explosion
     Image = 'Explosion.png'
     Image_obj = p.Picture(Image) # create picture object
     stddraw.picture(Image_obj,x,y) # draw picture object

def BigExplosion(x,y): # function to show big explosion
    Image = 'Big Explosion.png'
    Image_obj = p.Picture(Image) # create picture object
    stddraw.picture(Image_obj,x,y-0.3) # draw picture object with offset to align picture correctly

def Bunker(x,y,lives): # function to show bunker
    Image = 'bunker_' + str(lives) + '.png' #image name as per lives of bunker
    Image_obj = p.Picture(Image) # create picture object
    stddraw.picture(Image_obj,x,y) # draw picture object
    

