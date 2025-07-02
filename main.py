import random
name=input('Please Enter Your Name: ')
print(f'''{name}! Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.
    Please select the difficulty level:
    
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    4. Impossible (2 chances)
    5. Crazy (1 chance)''')
rounds=0
wins=0 
losses=0
high_score=0
while True:
    rounds+=1
    player_chances = 0
    game_diff = ''
    is_guessed= False
    the_number=random.randint(1, 100)
    attempts = 0
    while player_chances == 0:
        try:
            player_choice = int(input('Your Choice: '))
        except:
            print('Please Type A Valid Number')
            continue
        if player_choice  == 1:
            player_chances = 10
            game_diff = 'Easy'
        elif player_choice  == 2:
            player_chances = 5
            game_diff = 'Medium'
        elif player_choice  == 3:
            player_chances = 3
            game_diff = 'Hard'
        elif player_choice  == 4:
            player_chances = 2
            game_diff = 'Impossible'
        elif player_choice  == 5:
            player_chances = 1
            game_diff = 'Crazy'
        else:
            print('Please Select 5/4/3/2/1')
            continue
    
    print(f'Great! You have selected the {game_diff} difficulty level.Let\'s start the game!')
    while is_guessed is False:
        if attempts >= player_chances:
            losses+=1
            print('Sorry, Your Attempts Are 0.')
            break
        try:
            the_guess=int(input('guess your number:'))
        except:
            print('please Type A Valid Number')
            continue
        if the_guess == the_number:
            attempts+=1
            wins+=1
            if high_score > attempts or high_score == 0:
                high_score = attempts
            print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
            break
        else:
            attempts+=1
            if the_number < the_guess:
                print(f'Incorrect! The number is less than {the_guess}.')
            else:
               print(f'Incorrect! The number is greater than {the_guess}.')
            continue
    answer='ok'
    while answer.lower() != 'y' and answer.lower() != 'n' and answer.lower() != 's':
        answer = input('''Do You Wanna Play Again ? ^_^.
    1. Y: Yes
    2. N: No 
    3. S: Stats
    Answer: ''')
    if answer.lower() == 'y':
        print('''Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    4. Impossible (2 chances)
    5. Crazy (1 chance)''')
        continue
    elif answer.lower() == 'n':
        print(f'{name}, Thank You For Playing <3')
    else:
        print(f'''
        {name}'s Stats:
            Total Rounds: {rounds}
            Wins: {wins}
            Losses: {losses}
            high score: {high_score}
            ''')
        while answer.lower() != 'y' and answer.lower() != 'n':
            answer = input(f'''{name}, Do You Wanna Play Again ? ^_^.
    1. Y: Yes
    2. N: No 
    3. S: Stats
    Answer: ''')
        if answer.lower() == 'y':
            print('''Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    4. Impossible (2 chances)
    5. Crazy (1 chance)''')
            continue
        elif answer.lower() == 'n':
            print(f'{name}, Thank You For Playing <3')
            break
        
