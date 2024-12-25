#import directories

from random import choice
from time import sleep

#main function

def generate_password():
    variants =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ,"1","2","3","4","5","6","7","8","9","0"]
    print("Эта программа сенерирует тебе пароль!")
    sleep(1.5)
    password =""
    for i in range(16):

#generating
        
        numbers = choice(variants)
        password +=numbers
    print(f"Твой пароль: {password}")

#chekig for launch

if __name__ =="__main__":
    generate_password()
