from random import shuffle
import time
import os

def juego_palito_multiplayer():
    # Clears Linux Terminal for ease of use. Used multiple times through the code
    os.system('clear') 
    # Selects how many players. If not in range 1 to 4, cancels game
    players = int(input('Select players from 1 to 4: '))
    if players not in range(1,5):
        print('Sorry! Only 1 to 4 players can play : (')
        return
    # Copy of 'players' as it is used later and should not be modified. This var is used to calculate sticks in case of singleplayer
    sticks_ammount = players 
    # 'Visual' list of the sticks. Used for most calculations
    lista = ['-','--','---','----'] 
    # The other 'Visual' list of the sticks. This one is only used when choosing
    sticks = ['|','|','|','|'] 
    # Checks if player ammount is between 1 and 3, and then if it is one. If so, changes var sticks_ammount to the selected value. 
    # Else adjusts the sticks to the max players
    if players != 4:
        if players == 1:
            sticks_ammount = int(input('Choose how many sticks (from 2 to 4): '))
            if sticks_ammount not in range(2, 5):
                print("Invalid sticks! Defaulting to 2.")
                sticks_ammount = 2
        lista = lista[:sticks_ammount]
        sticks = sticks[:sticks_ammount]
    # Simple function that uses already existing 'shuffle' but returns a value
    def mezclar(lista):
        shuffle(lista)
        return lista
    # Function for players to choose the stick. Prints the prompt, then asks for input. 
    def probar_suerte():
        g2g = False
        while g2g != True:
            print(f'\nChoose a stick from 1 to {sticks_ammount}: \n \t {" ".join(sticks)}\n\n\t   ')
            
            try:
                intento = int(input())

            except ValueError:
                os.system('clear')
                print("Invalid input! Please enter a whole number.")
                continue        

            # The input is checked to see if its between 1 and sticks_ammount
            if intento < 1 or intento > sticks_ammount:
                os.system('clear')
                print(f'Invalid stick! Select a number from 1 to {sticks_ammount}')
            # If it is, then checks if the stick was already picked before
            elif sticks[intento - 1] == 'X':
                os.system('clear')
                print(f'That stick has already been selected!')
            # If the input is not between 1 and sticks_ammount, or the stick was picked, 'g2g' will not turn True, therefore the loop is repeated.
            # If both previous conditions are false (intento in range, and sticks != 'X'), 'g2g' will turn True
            else:
                 g2g = True

        # Lastly, it marks the chosen stick with an 'X' and returns the value / position of chosen stick
        sticks[intento - 1] = 'X'
        return intento
    # Stick list is shuffled
    mezclar(lista)
    # Multiple var are created: 2 for all player choices and names, 2 for winner choices and names, 1 for loser choice and name
    # Other vars are 'player_tries' for the while loop to execute as many times as players left, then individual var for name and attempt / choice
    # This could have been a much simpler scenario, reducing the ammount of variables, but it was done this way for learning purposes
    player_choices = []
    player_tries = players
    # Collects information about name of the player, then runs 'probar_suerte()', appends the results to a list and reduces the ammount of remaining loops by 1
    while player_tries != 0:
        os.system('clear')
        player_name = input('Introduce your name: ')
        player_attempt = probar_suerte()
        player_choices.append((player_name,player_attempt))
        player_tries -= 1
    loser = []
    winner_name = []
    winner_choice = []
    # Separates winners names and choices from loser
    for name,attempt in player_choices:
        index = attempt - 1
        if lista[index] == min(lista):
            loser = [name,lista[index]]
        else:
            winner_name.append(name)
            winner_choice.append(lista[index])
    # Simple var to count the ammount of winners
    total_winners = len(winner_name)
    os.system('clear')
    # Reveals winners, waiting a few seconds between reveals (for tension O: ). It also shows the chosen and remaining sticks
    for n in range(total_winners): 
        print(f'The player {winner_name[n]} is free as they picked the stick {winner_choice[n]}')
        lista.remove(winner_choice[n])
        print(f'The sticks remaining are {lista}')
        time.sleep(3)
        print('\t...')
        time.sleep(2)
    if loser == []:
        return print('No one loses!!')
    else:
        return print(f'The loser is {loser[0]}!! as they picked the stick {loser[1]}\n')

juego_palito_multiplayer()