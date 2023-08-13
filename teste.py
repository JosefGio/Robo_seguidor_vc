import control as kp


kp.init()

def main():
    print (kp.getKey('s'))

if __name__ == '__main__':
    kp.init()
    while True:
        main()
