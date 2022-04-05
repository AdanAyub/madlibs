import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, 'sp' for spock, 'l' for lizard\n")
    computer = random.choice(['r', 'p', 's', 'sp', 'l'])

    if user == computer:
        return 'It\'s a draw'

    # r > s, s > p, p > r, r > l, l > sp, sp > s, s > l, l > p, p > sp, sp > r, 
    if is_win(user, computer):
        return 'congratulations You won!'

    return 'You lost that\s too bad!'

def is_win(character, rival):
    # return true if player wins
    # r > s, s > p, p > r, r > l, l > sp, sp > s, s > l, l > p, p > sp, sp > r, 
    if (character == 'r' and rival  == 's') or (character == 's' and rival == 'p') \
        or (character == 'p' and rival == 'r') or (character == 'r' and rival == 'l') or (character == 'l' and rival == 'sp') or (character == 'sp' and rival == 's') or (character == 's' and rival == 'l') or (character == 'l' and rival == 'p') or (character == 'p' and rival == 'sp') or (character == 'sp' and rival == 'r'):
        return True

print(play())
    