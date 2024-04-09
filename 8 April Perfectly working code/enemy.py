#imports
import stddraw
import Image
import stdaudio
import enemyManager
import Main
from threading import Thread

#giving an additional .1 spacing on the border of the screen, but the working area is a 10x10 grid.
stddraw.setXscale(-1,11)
stddraw.setYscale(-1,11)

score = [0,0,0] #H
high_score = [0,0,0]
level = 1
velocity = 0.04

def play_sound(): #H
    stdaudio.playFile('invaderkilled') #H: .wav file from https://www.classicgaming.cc/classics/space-invaders/sounds

def game_over(): #H
    global score, high_score, level
    stddraw.setXscale(-1,11)
    stddraw.setYscale(-1,11)
    stdaudio.playFile('explosion') #H: .wav file from https://classicgaming.cc/classics/space-invaders/sounds
    stddraw.show(100)
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontSize(60)
    stddraw.text(5,8,'GAME OVER')
    strscore = ''
    for i in range(3):
        strscore += str(score[i])
    stddraw.setFontSize(40)
    stddraw.text(5,4.5,'SCORE ' + strscore)
    stddraw.setFontSize(30)
    stddraw.text(5,1,'PRESS [C] TO CONTINUE')

    score_num = score[0] * 100 + score[1] * 10 + score[2]
    highscore_num = high_score[0] * 100 + high_score[1] * 10 + high_score[2]
    if score_num > highscore_num:
        high_score = score[:]
        stddraw.text(5,2.5,'NEW HIGH SCORE!!!')

    score = [0,0,0]
    level = 1
    stddraw.setPenColor(stddraw.BLACK)
    enemyManager.clear_lists()
    Main.Lives = 3
    done = False
    while done == False:
        if stddraw.hasNextKeyTyped():
            k = stddraw.nextKeyTyped()
            if k == 'c':
                break
        stddraw.show(0)
    Main.main()  

def inc_score(): #H
    global level
    if score[2] < 9:
        score[2] += 1
    elif score[2] == 9 and score[1] < 9:
        score[2] = 0
        score[1] += 1
    elif score[2] == 9 and score[1] == 9:
        score[2] == 0
        score[1] == 0
        score[0] += 1
    level_score = score[0] * 100 + score[1] * 10 + score[2]
    if level_score % 15 == 0:
        level += 1
        enemyManager.clear_lists()
        Main.main()

def display_score(): #H
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontFamily('NotJamSciMono13')
    stddraw.setFontSize(40)
    strscore = ''
    for i in range(3):
        strscore += str(score[i])
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.text(1,-0.5,'SCORE: ' + strscore)
    stddraw.setFontSize(35)
    stddraw.text(5,10.7,'LEVEL ' + str(level))
    stddraw.setFontSize(40)
    stddraw.setPenColor(stddraw.BLUE)
    strhighscore = ''
    for i in range(3):
        strhighscore += str(high_score[i])
    stddraw.text(8,-0.5,'HIGH SCORE: ' + strhighscore)  

#main thus far used to test the enemy, will be run from the enemy manager class
def main():
    stddraw.show()
# enemy object and its functions
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 0.45
        self.beenHit = False
        self.velocity = velocity * level

    def move(self, direction):
        if direction == 1:
            self.x += self.velocity
        if direction == -1:
            self.x -= self.velocity
        
        Image.RefreshEnemy(self.x,self.y)

    def moveDown(self):
        self.y -= 1

    def hit(self):
        thread = Thread(target=play_sound) #H Code from : https://stackoverflow.com/questions/52769618/how-can-i-play-a-sound-while-other-lines-of-code-execute-simultaneously
        thread.start() #H
        inc_score() #

           
if __name__ == '__main__': main()