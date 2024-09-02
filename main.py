import os
import platform
print('Welcome to the Auction')
data = {}
max = 0
name = ''
game_on = True

def clear():
    if platform.system() == 'Windows':
        os.system('cls')




while game_on:
    user_name = input("what is your name? ").lower()
    user_bid =int(input("what is your bid?"))
    another_user = input("Is there any person for bid?(yes/no) ").lower()

    data[user_name]= user_bid


    if another_user=='yes':
        clear()
    elif another_user=='no':
        for i,j in data.items():
            if j >max:
                max=j
                name = i

        print(f"winner is {name} and bit amount {max}")
        game_on=False
        break
