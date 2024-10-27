import random

from logo import start_logo

flag = False
answer = "y"
select_level = -1
guess_num = -1

print("***   START GUESSING GAME!!!   ***")
print(start_logo)
print("You will need to find the number invented by your computer! (from 0 to 100)")


def game():
    global select_level
    select_level = int(input("\nSelect number of attempts: from 5 to 10\n"))

    guess_num = random.randint(0, 100)

    while select_level > 0:
        user_num = int(input("Type your number (from 0 to 100)!"))
        print(f"You entered the number << {user_num} >>")
        if user_num != guess_num:
            print("No this number!")
            if user_num > guess_num:
                print("Too high")
            else:
                print("Too low")
            select_level -= 1
            print(f"You are having {select_level} attemp(s)")
        elif user_num == guess_num:
            print(f"*** WIN!!! You guessed the number! It is << {user_num} >>   ***")
            select_level = -1

    if select_level == 0:
        print(f"*** LOSE!!! Guessed number was < {guess_num} >***")

    print("*** THIS GAME FINISHED ***\n")


while answer == "y":
    if flag == False:
        game()
        flag == True
        answer = input("Are you going to continue game? Y/N\n").lower()

    else:
        print("***   OK!!! START NEW GAME!!! \n   ***")
        game()
        answer = input("Are you going to continue game? Y/N\n").lower()
