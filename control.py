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
    if getKey ('w'):
       # print ('Pra cima')
        #MOTOR 1
        p0.value(1)
        p1.value(0)
        #MOTOR 2
        p2.value(0)
        p3.value(1)
        #MOTOR 3
        p4.value(1)
        p5.value(0)
        #MOTOR 4
        p6.value(0)
        p7.value(1)
    if getKey ('s'):
       # print ('Pra baixo')
         #MOTOR 1
        p0.value(0)
        p1.value(1)
        #MOTOR 2
        p2.value(1)
        p3.value(0)
        #MOTOR 3
        p4.value(0)
        p5.value(1)
        #MOTOR 4
        p6.value(1)
        p7.value(0)
    if getKey ('d'):
       # print ('Para direita')
        #MOTOR 1
        p0.value(1)
        p1.value(0)
        #MOTOR 2
        p2.value(1)
        p3.value(0)
        #MOTOR 3
        p4.value(0)
        p5.value(1)
        #MOTOR 4
        p6.value(0)
        p7.value(1)
    if getKey ('a'):
       # print ('Para a esquerda')
    
if __name__ == '__main__':
    init()
    while True:
        main()