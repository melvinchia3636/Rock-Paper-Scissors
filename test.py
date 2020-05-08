from random import randint

def getUserChoice():
    userInput = input('Enter your choice: ').lower()
    return userInput if (userInput == 'rock' or userInput == 'paper' or userInput == 'scissors') else 'User does not input [\'rock\', \'paper\', \'scissors\']'

def getComputerChoice():
    num = randint(0,2)
    return 'rock' if num == 0 else 'paper' if num == 1 else 'scissors' if num == 2 else ''

def determineWinner(userChoice, computerChoice):
    return 'The game is tie' if userChoice == computerChoice else 'Computer won' if (userChoice == 'rock' and computerChoice == 'paper') else 'Computer won' if (userChoice == 'paper' and computerChoice == 'scissors') else 'Computer won' if (userChoice == 'scissors' and computerChoice == 'rock') else 'You won'

def playGame():
    userChoice = getUserChoice()
    computerChoice = getComputerChoice()
    print('You threw: ', userChoice, '\nThe computer threw: ', computerChoice, '\n')
    print(determineWinner(userChoice, computerChoice))

playGame()
