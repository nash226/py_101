"""This is the Bonus rock paper scissor game!"""
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

SHORTCUTS = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock', 'spock'],
    'scissors': ['lizard', 'paper'],
    'lizard':   ['spock', 'paper'],
    'spock':    ['scissors', 'rock']
}

player_score = 0
computer_score = 0

def prompt(message):
    """Decorates our print messages"""
    print(f'==> {message}')

def player_wins(player_choice, comp_choice):
    """Determines if the computer choice is in the winning combos for 
    player"""
    return comp_choice in WINNING_COMBOS[player_choice]

def keep_score(player, computer, count_player, count_computer):
    """Keeps score for best of 5 and declares grand winner"""
    if player_wins(player, computer):
        count_player += 1
    elif player != computer:
        count_computer += 1

    print(f'Best of 5 Player: {count_player} vs Computer: {count_computer}!')

    if count_computer == 3:
        print('The grand winner is computer, Game over.')
    elif count_player == 3:
        print('You are the grand winner! Game over.')

    return count_player, count_computer

def display_winner(player, computer):
    """Displays winner of each rps match"""
    if player_wins(player, computer):
        prompt("You win!!!")
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")


while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)} (r, p, sc, l, sp)" )
    choice = input().lower().strip()

    while choice not in SHORTCUTS:
        prompt('Thats not a valid choice')
        choice = input().lower().strip()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {SHORTCUTS[choice]}, computer chose {computer_choice}')

    display_winner(SHORTCUTS[choice], computer_choice)

    player_score, computer_score = keep_score(SHORTCUTS[choice],
                                              computer_choice, player_score,
                                              computer_score)

    if player_score == 3 or computer_score == 3:
        break

    prompt('Do you want to keep playing? (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n". ')
        answer = input().lower()

    if answer[0] == 'n':
        break
