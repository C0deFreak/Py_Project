import random
from WordList import spliting_words
from turtle import *
import time
from datetime import datetime
import keyboard


def logo():
    penup()
    goto(-100, 0)
    color('green')
    write('P', align='center', font=('Arial', 40, 'bold'))
    penup()
    goto(-60, 0)
    write('y', align='center', font=('Arial', 40, 'bold'))
    penup()
    goto(-20, 0)
    color('green')
    write('w', align='center', font=('Arial', 40, 'bold'))
    penup()
    goto(20, 0)
    color('white')
    write('o', align='center', font=('Arial', 40, 'bold'))
    penup()
    goto(60, 0)
    color('white')
    write('o', align='center', font=('Arial', 40, 'bold'))
    penup()
    goto(100, 0)
    color('yellow')
    write('n', align='center', font=('Arial', 40, 'bold'))
    penup()


# Shortcut for letter_holder()
def eachletter(color_of_holder):
    pendown()
    letter_holder(letter_write=guess_letters[answer_index], write_color=color_of_holder)


# Shortcut for writing lose/win txt
def textdraw():
    penup()
    color('white')
    goto(0, 0)
    pendown()
    clear()


# Draws a holder depending on is the letter correct
def letter_holder(letter_write, write_color):
    color(write_color)
    begin_fill()
    forward(75)
    right(90)
    forward(100)
    right(90)
    forward(75)
    right(90)
    forward(30)
    penup()
    right(90)
    forward(37.5)
    color('white')
    write(f'{letter_write.upper()}', align='center', font=('Arial', 20, 'bold'))
    color(write_color)
    back(37.5)
    left(90)
    pendown()
    forward(70)
    right(90)
    penup()
    forward(85)
    end_fill()


# Delays the program from ending too quickly
def ending():
    textinput('End Program', 'Write anything to end program')
    bye()


secret_word = spliting_words()

tries = 0

guess_limit = 6

secret_word_letters = []

secret_number = random.randint(0, 2499)

guess_letters = []

time_now = int(datetime.now().strftime('%H'))

time_list = [11, 12, 13]


title('Pywoon')

hideturtle()
speed(1000)

bgcolor('gray11')

option = textinput('OPTIONS', 'RULES / START').upper()

if option == 'START':

    if time_now in time_list:

        logo()
        time.sleep(3)
        clear()

        for column in range(6):
            penup()
            goto(-207.5, (325 - (column * 110)))
            pendown()
            color('darkgray')
            begin_fill()
            for row in range(5):
                pendown()
                for drawing in range(2):
                    forward(75)
                    right(90)
                    forward(100)
                    right(90)
                penup()
                forward(85)
            end_fill()

        for letters in secret_word[secret_number]:
            secret_word_letters.append(letters)

        while tries < guess_limit:
            
            guess = ''
            number_for_guessing = 0
            goto(-207.5, (325 - (tries * 110)))
            while number_for_guessing < 5:
                color('white')
                input_letters = keyboard.read_key()
                penup()
                sety(325 - (tries * 110))
                forward(75)
                right(90)
                forward(100)
                right(90)
                forward(75)
                right(90)
                forward(30)
                right(90)
                forward(37.5)
                write(f'{input_letters.upper()}', align='center', font=('Arial', 20, 'bold'))
                back(37.5)
                left(90)
                pendown()
                forward(70)
                right(90)
                penup()
                forward(85)
                guess += str(input_letters)
                number_for_guessing += 1

            number_for_guessing = 0

            answer_mark = ''

            answer_index = 0

            guess_letters.clear()

            for letters_of_guess in guess:
                guess_letters.append(letters_of_guess)

            penup()
            goto(-207.5, (325 - (tries * 110)))
            if guess in secret_word:
                for answers in guess_letters:

                    if answers == secret_word_letters[answer_index]:
                        eachletter('green')

                    elif answers in secret_word_letters and guess_letters[answer_index] != secret_word_letters[answer_index]:
                        eachletter('yellow')

                    else:
                        eachletter('darkgray')

                    answer_index += 1

                if guess == secret_word[secret_number]:
                    textdraw()
                    write(f'You won in {tries + 1} tries!', align='center', font=('MS Sans Serif', 35, 'bold'))
                    ending()
                    break

                tries += 1
                print(answer_mark)
            else:
                color('darkgray')
                for repeat1 in range(5):
                    for repeat2 in range(4):
                        pendown()
                        begin_fill()
                        forward(75)
                        right(90)
                        forward(100)
                        right(90)
                        end_fill()
                    penup()
                    forward(85)
                pass

        else:
            textdraw()
            write(f'Failed, the word was "{secret_word[secret_number]}"!', align='center', font=('MS Sans Serif', 35, 'bold'))
            ending()

    else:
        write('Come back between 11h - 13h', align='center', font=('MS Sans Serif', 40, 'bold'))
        ending()

elif option == 'RULES':
    logo()
    time.sleep(3)
    clear()

    # Green TUTORIAL
    penup()
    goto(-207.5, 140)
    color('green')
    begin_fill()
    for drawing1 in range(2):
        forward(75)
        right(90)
        forward(100)
        right(90)
    penup()
    forward(85)
    end_fill()
    color('darkgray')
    begin_fill()
    for row1 in range(4):
        pendown()
        for drawing1 in range(2):
            forward(75)
            right(90)
            forward(100)
            right(90)
        penup()
        forward(85)
    end_fill()
    goto(0, 0)
    pendown()
    write('GREEN - Right letter & place', align='center', font=('MS Sans Serif', 20, 'bold'))
    time.sleep(5)
    clear()

    # Yellow TUTORIAL
    penup()
    goto(-207.5, 140)
    color('yellow')
    begin_fill()
    for drawing1 in range(2):
        forward(75)
        right(90)
        forward(100)
        right(90)
    penup()
    forward(85)
    end_fill()
    color('darkgray')
    begin_fill()
    for row1 in range(4):
        pendown()
        for drawing1 in range(2):
            forward(75)
            right(90)
            forward(100)
            right(90)
        penup()
        forward(85)
    end_fill()
    goto(0, 0)
    pendown()
    write('YELLOW - Right letter but wrong place', align='center', font=('MS Sans Serif', 20, 'bold'))
    time.sleep(5)
    clear()

    # Gray TUTORIAL
    penup()
    goto(-207.5, 140)
    begin_fill()
    for row1 in range(5):
        pendown()
        for drawing1 in range(2):
            forward(75)
            right(90)
            forward(100)
            right(90)
        penup()
        forward(85)
    end_fill()
    goto(0, 0)
    pendown()
    write('GRAY - Wrong letter', align='center', font=('MS Sans Serif', 20, 'bold'))
    time.sleep(5)
    bye()

else:
    write('Wrong Input!', align='center', font=('MS Sans Serif', 40, 'bold'))
    ending()
