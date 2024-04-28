import stddraw
import Image
import math

class Bunker():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 10
        self.radius = 0.5 

    def hit(self): #function to decrement the lives of a bunker when hit
        if self.lives > 0:
            self.lives -= 1

def draw_bunkers(bunkers_list):# function to draw the bunkers
    for i in range(len(bunkers_list)):
        if bunkers_list[i].lives > 0:
            Image.Bunker(bunkers_list[i].x, bunkers_list[i].y)

def check_hit(ebullet_list, player_list, bunkers_list): #function to check when a bunker is hit by a bullet
    for bunker in bunkers_list: #for loop that goes through list of bunkers
        bunk_x = bunker.x
        bunk_y = bunker.y
        bunk_r = bunker.radius
        bunk_lives = bunker.lives
        for bullet in ebullet_list[:]: #for loop to go through the enemy bullets
            ebull_x = bullet.x
            ebull_y = bullet.y
            distance = math.sqrt((ebull_x - bunk_x)**2 + (ebull_y - bunk_y)**2)
            if distance <= bunk_r and bunk_lives > 0:
                ebullet_list.remove(bullet)
                bunker.hit()

        for bullet in player_list[:]: #function to go through the player bullets
            play_x = bullet.x
            play_y = bullet.y
            distance = math.sqrt((play_x - bunk_x)**2 + (play_y - bunk_y)**2)
            if distance <= bunk_r and bunk_lives > 0:
                player_list.remove(bullet)
                bunker.hit()

