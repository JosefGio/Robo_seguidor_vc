import pygame
def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey (keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    
    myKey = getattr(pygame, 'K_{}'. format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()
    return ans
    
def main():
    if getKey ('KP8'):
        print ('Norte')
        #MOTOR 1
       # p0.value(1)
       # p1.value(0)
        #MOTOR 2
       # p2.value(0)
       #  p3.value(1)
        #MOTOR 3
       #  p4.value(1)
       # p5.value(0)
        #MOTOR 4
       # p6.value(0)
       # p7.value(1)
    if getKey ('KP2'):
        print ('Sul')
         #MOTOR 1
       # p0.value(0)
       # p1.value(1)
        #MOTOR 2
       # p2.value(1)
       # p3.value(0)
        #MOTOR 3
       # p4.value(0)
       # p5.value(1)
        #MOTOR 4
       # p6.value(1)
       # p7.value(0)
    if getKey ('KP6'):
        print ('Leste')
        #MOTOR 1
       # p0.value(1)
       # p1.value(0)
        #MOTOR 2
       # p2.value(1)
       # p3.value(0)
        #MOTOR 3
      #  p4.value(0)
       # p5.value(1)
        #MOTOR 4
      #  p6.value(0)
      # p7.value(1)
    if getKey ('KP4'):
        print ('Oeste')
    
if __name__ == '__main__':
    init()
    while True:
        main()