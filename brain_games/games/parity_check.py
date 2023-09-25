import prompt
import random

def parity_check():
    print('brain-even\n')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')

    print('Answer "yes" if the number is even, otherwise answer "no"')
    tries = 0
    
    while tries < 3:
    	randomizer = random.randint(1, 100)
    	print('Question ' + str(randomizer))
    	answer = prompt.string('Your answer: ')
    	    	
    	if randomizer % 2 == 0 and answer == 'yes':
    		print('Correct!')
    		tries += 1
    		
    	elif randomizer % 2 != 0 and answer == 'no':
    		print('Correct!')
    		tries += 1  	
    		  		
    	else:
    		print(answer + ''' is wrong answer ;(. Correct answer was 'no'.
Let's try again, ''' + name + "!")
    		break
    	print('Congratulations, ' + name + '!')
