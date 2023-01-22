import time
import random
def guessing_game():

    random_number= random.randrange(1,100); 

    print("""
    ~Welcome to Conner's Higher and Lower Number Guessing Game~
    You have 7 tries so be careful >:)
    Please Input a number from (1-100)!
    """)

    time.sleep(2.4)
    
    
    for tries in range(7):
        guess= int(input("What is the number you want to guess: "))
        finalvalue = tries + 1
       
        if guess < random_number:
            print ("Your guess is Lower than the Number") 

        elif guess > random_number:
            print ("Your guess is Higher than the Number")

       
        elif guess== random_number:
            print("Congrats you guessed the number!")
            print(f"It took you {finalvalue} tries!")
            break;

        if tries == 6:
            print ("Try again!")
            guessing_game()
guessing_game()