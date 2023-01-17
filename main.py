import random
options = ('piedra', 'papel', 'tijera')
user_wins = 0
computer_wins = 0
rounds = 1

while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    user_option = input('piedra, papel o tijera =>')
    user_option = user_option.lower()
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    rounds += 1

    if  not user_option in options:
        print('esa opcion no es valida')
        continue

    if user_option == computer_option:
        print('empate!')
    elif user_option == 'piedra':
        if computer_option == 'papel':
            print('papel gana piedra')
            print('computer gano!')
            computer_wins += 1
        else:
            print(f'{user_option} gana a tijera')
            print('user gano')
            user_wins += 1
    elif user_option == 'papel':
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("user gano")
            user_wins += 1
        else:
            print("tijera gana a papel")
            print("computer gano")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("user gano")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("computer gano")
            computer_wins += 1
    if computer_option == 2:
        print('el ganador es la computadora')
        break
    if user_wins == 2:
        print('el ganador es el usuario')
        break
