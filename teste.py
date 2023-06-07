from control import KeyPressModule as kp


kp.init()

def main():
    print (kp.getKey('s'))

if __name__ == '__main__':
    init()
    while True:
        main()