import random

def predict(x):
    unique_number = random.randint(1, x)
    predict = 0
    while predict != unique_number:
        predict = int(input(f'predict a number between 1 and {x} '))
        if predict < unique_number:
            print('Sorry prediction too low guess again.')
        elif predict > unique_number:
            print('Sorry, predict again. Too high.')

    print('Yay, Congrats you have predicted the number {unique_number} correctly!!')

def machine_predict(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            predict = random.randint(low, high)
        else:
            predict = low #could also be high b/c low = high
        feedback = input(f'Is {predict} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback =='h':
            high = predict - 1
        elif feedback == 'l':
            low = predict + 1 

    print(f'Yay the machine predicted your number, {predict}, correctly!')

predict(10)
