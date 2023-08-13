import pygame
import time

memory_key = 0

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))


def getKey (keyName):
    global memory_key
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'. format(keyName))
    if keyInput [myKey] == True and memory_key == False:
        ans = True
        ##return keyInput [myKey], memory_key
    else:
        ans = False
    memory_key = keyInput [myKey]
    return ans
    
    
def main():
    
    
    if getKey ('KP8') == True:
        print ('Norte')
    elif getKey ('KP6') == True:
        print ('Leste')
    elif getKey ('KP2') == True:
        print ('Sul')
    elif getKey ('KP4') == True:
        print ('Oeste')
    elif getKey ('KP9') == True:
        print ('Nordeste')
    elif getKey ('KP3') == True:
        print ('Sudeste')
    elif getKey ('KP7') == True:
        print ('Noroeste')
    elif getKey ('KP1') == True:
        print ('Sudoeste')
    elif getKey ('KP5') == True:
        print ('Parado')
    
    time.sleep(0.1)
    pygame.display.update()
    
if __name__ == '__main__':
    init()
    while True:
        main()
