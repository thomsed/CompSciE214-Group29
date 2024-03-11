import sys
import stdio
import stddraw

def createBall():
 stddraw.filledCircle(0.5,0.1,0.05)

def moveLeft():
  ballX = 0.5
  while ballX >= 0.05:
    stddraw.clear()
    stddraw.filledCircle(ballX,0.1,0.05)
    ballX += -0.001
    stddraw.show(10)
    


def moveRight():
  ballX = 0.05
  while ballX <= 0.95:
    stddraw.clear()
    stddraw.filledCircle(ballX,0.1,0.05)
    ballX += 0.001
    stddraw.show(10)
  stddraw.show()

def main():
  createBall()
  moveLeft()
  moveRight()
  

if __name__ == '__main__':
  main()


