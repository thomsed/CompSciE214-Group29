import stddraw
import picture as p
import Main
import enemy

def RefreshBackground():
    pic_name ='Back ground.png' 
    backgroundImage_obj  = p.Picture(pic_name)
    stddraw.picture(backgroundImage_obj)

    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.setFontFamily('NotJamSciMono13')
    stddraw.setFontSize(28)
    stddraw.text(0,10.7,'Lives: '+str(Main.Lives))

    


def RefreshPlayer(x,y):
    pic_name ='Falcon.png' 
    playerImage_obj  = p.Picture(pic_name)
    stddraw.picture(playerImage_obj,x,y)

def RefreshEnemy(x,y):
    enemyImage = 'Tie fighter.png'
    enemyImage_obj = p.Picture(enemyImage)
    stddraw.picture(enemyImage_obj,x,y)


def RefreshBullet(x,y):
    bulletImage = "Bullet.png"
    bulletImage_obj = p.Picture(bulletImage)
    stddraw.picture(bulletImage_obj,x,y)

def RefreshEBullet(x,y):
    EbulletImage = "EBullet.png"
    EbulletImage_obj = p.Picture(EbulletImage)
    stddraw.picture(EbulletImage_obj,x,y)

def Explosion(x,y):
     Image = 'Explosion.png'
     Image_obj = p.Picture(Image)
     stddraw.picture(Image_obj,x,y)

def BigExplosion(x,y):
    Image = 'Big Explosion.png'
    Image_obj = p.Picture(Image)
    stddraw.picture(Image_obj,x,y-0.3)
    

