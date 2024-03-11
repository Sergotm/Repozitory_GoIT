import sys 
from py_1 import main as greeting
from py_2 import main as exiting

def main():
    try:
        if sys.argv[1] == 'greet':
            greeting()
        elif sys.argv[1] == 'goodbuy':
            exiting()
        else:
            print(f'Unknown argument')
    except IndexError:
        print("Argumnet must be 'greet' and 'goodbuy' ")  


if __name__ == '__main__':
    main()

