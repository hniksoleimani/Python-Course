import random
options = ['Rock', 'Paper', 'Scissor']
scores = {'user':0, 'computer':0}
computer_choice = random.choice(options)
round = 0
# while round <= 4:
def game():
    for i in range(3):
        user_choice = input('Play the game:')
        if user_choice =='Rock' and computer_choice == 'Paper':
            print('Computer wins.')
            scores['computer'] += 1
        elif user_choice == 'Rock' and computer_choice == 'Scissor':
            print('You win.')
            scores['user'] += 1
        elif user_choice == 'Paper' and computer_choice == 'Paper':
            print('Draw...!')
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            print('You win...!')
            scores['user'] += 1
        elif user_choice == 'Paper' and computer_choice == 'Scissor':
            print('Computer wins...!')
            scores['computer'] += 1
        elif user_choice == 'Scissor' and computer_choice == 'Rock':
            print('Computer wins...!')
            scores['computer'] += 1
        elif user_choice == 'Scissor' and computer_choice == 'Paper':
            print('You win...!')
            scores['user'] += 1
        elif user_choice == 'Scissor' and computer_choice == 'Scissor':
            print('Draw...!')
        elif user_choice == 'Rock' and computer_choice == 'Rock':
            print('Draw...!')
def scoring():
    if int(scores['user']) > int(scores['computer']):
        print('Congratulations you won the match...!')
    elif int(scores['user']) < int(scores['computer']):
        print('You lost the match against the computer.')
    elif int(scores['user']) == int(scores['computer']):
        print('The game is drawn.')

def show_scores():
    print('Your total score is:' + str(scores['user']) + '\t' + 'Computer score is:' + str(scores['computer']) )


game()
show_scores()
scoring()