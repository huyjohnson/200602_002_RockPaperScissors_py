# - Rock, Paper, Scissors game -
import random

print('ROCK, PAPER, SCISSORS')
gamelist = ['ROCK', 'PAPER', 'SCISSORS']
w = 0
l = 0
t = 0

def score():
    score = [w, l, t]
    print('{} Wins, {} Losses, {} Ties'.format(score[0], score[1], score[2]))

def cpuR():
    global w, l, t
    cpuChoice = random.choice(gamelist)
    print(cpuChoice)
    if cpuChoice == gamelist[0]:
        print('It is a tie!')
        t += 1
    elif cpuChoice == gamelist[1]:
        print('You lose.')
        l += 1
    else:
        print('You win!')
        w += 1
        
def cpuP():
    global w, l, t
    cpuChoice = random.choice(gamelist)
    print(cpuChoice)
    if cpuChoice == gamelist[0]:
        print('You win!')
        w += 1
    elif cpuChoice == gamelist[1]:
        print('It is a tie!')
        t += 1
    else:
        print('You lose.')
        l += 1

def cpuS():
    global w, l, t
    cpuChoice = random.choice(gamelist)
    print(cpuChoice)
    if cpuChoice == gamelist[0]:
        print('You lose.')
        l += 1
    elif cpuChoice == gamelist[1]:
        print('You win!')
        w += 1
    else:
        print('It is a tie!')
        t += 1
        
while True:
    score()
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    choice = input()
    lowerChoice = choice.lower()
    if lowerChoice == 'r':
        print('ROCK versus...')
        cpuR()
    elif lowerChoice == 'p':
        print('PAPER versus...')
        cpuP()
    elif lowerChoice == 's':
        print('SCISSORS versus...')
        cpuS()
    elif lowerChoice == 'q':
        score = [w, l, t]
        print('The match is finished. The final score is {} Wins, {} Losses, {} Ties.'.format(score[0], score[1], score[2]))
        break
