import csv
from termcolor import colored
from colorama import init
init()

score = 0
total = 0
path = ''
with open(path, encoding='utf-8') as csv_file:
    #format : question| answer a| answer b| answer c| answer d| correct answer letter like (A,B,C, or D)
    csv_reader = csv.reader(csv_file, delimiter = '|')
    counter = 0
    for rows in csv_reader:
        print(str(counter+1) + " . " + rows[0])
        print('    A.' + rows[1])
        print('    B.' + rows[2])
        print('    C.' + rows[3])
        print('    D.' + rows[4])
        answerInput = input("\n>: Answer: ")
        answerInput = answerInput.upper()
        if (answerInput == rows[5].strip()):
            print(colored('Correct!', 'green'))
            total = total + 1
            score = score + 1
        else:
            print(colored('Incorrect.', 'red') + 'The correct answer was: ' + rows[5])
            total = total + 1

        counter = counter + 1
    if score >= total/2:
        print(colored('Pass!', 'green') + ' Score: ' + str(score) + '/' + str(total))
    else:
        print(colored('Mission failed, we\'ll get em next time.', 'red') + ' Score: ' + str(score) + '/' + str(total))
