import random

a = input("Who is the first player? \n")
b = input("Who is the second player? \n")

comp_guess = random.randint(1,3)

if comp_guess == 1:
    print(f'I think {a} will win the game.')
    
elif comp_guess ==2:
    print(f'I think {b} will win the game.')
    
else:
    print("Match Draw")


def first_player():
    print(f"\n {a} Start the game.\n")
    random_num1 = random.randint(1,100) 
    user_num1 = int(input(" Guess the number: \t")) 
    numberof_guesses1 = 1

    while (user_num1 != random_num1):
        numberof_guesses1 += 1
        if (user_num1 > random_num1):
            print("\n Guess Lower Number please")
            user_num1 = int(input("Guess the number: \t"))
        
        elif (user_num1 < random_num1):
            print("\n Guess Greater number please")
            user_num1 = int(input("Guess the number: \t")) 
        
    return numberof_guesses1

def second_player():
    print(f"\n {b} Your turn now \n")
    random_num2 = random.randint(1,100) 
    user_num2 = int(input(" Guess the number: \t")) 
    numberof_guesses2 = 1

    while (user_num2 != random_num2):
        numberof_guesses2 += 1
        if (user_num2 > random_num2):
            print("\n Guess Lower Number please")
            user_num2 = int(input("Guess the number: \t"))
        
        elif (user_num2 < random_num2):
            print("\n Guess Greater number please")
            user_num2 = int(input("Guess the number: \t")) 
            
    return numberof_guesses2

first = first_player()
second = second_player()

print(f'{a}: {first}')
print(f'{b}: {second}')

if first < second:
    print(f'Congratulations {a} won the game.')

elif first > second:
    print(f'Congratulations {b} won the game.')
    
else:
    print("Draw. Play Again.")
s