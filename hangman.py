import tkinter
import time
import random
import sys
import hangman_logic as hl

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def draw_gallows(pa_x, pa_y):
    base = pa_x - 150, pa_y + 160, pa_x - 50, pa_y + 160
    gallows = \
        pa_x, pa_y, pa_x, pa_y - 40, \
        pa_x - 100, pa_y - 40, pa_x - 100, pa_y + 160
    canvas.create_line(base, width=15)
    canvas.create_line(gallows, width=5)


def draw_hangman(pa_x, pa_y):
    head = canvas.create_oval(pa_x - 20, pa_y, pa_x + 20, pa_y + 40, width=3, state=tkinter.HIDDEN)
    torso = canvas.create_line(pa_x, pa_y + 40, pa_x, pa_y + 90, width=3, state=tkinter.HIDDEN)
    larm = canvas.create_line(pa_x - 40, pa_y + 60, pa_x, pa_y + 60, width=3, state=tkinter.HIDDEN)
    rarm = canvas.create_line(pa_x + 40, pa_y + 60, pa_x, pa_y + 60, width=3, state=tkinter.HIDDEN)
    lleg = canvas.create_line(pa_x, pa_y + 90, pa_x - 30, pa_y + 130, width=3, state=tkinter.HIDDEN)
    rleg = canvas.create_line(pa_x, pa_y + 90, pa_x + 30, pa_y + 130, width=3, state=tkinter.HIDDEN)
    return head, torso, larm, rarm, lleg, rleg


def draw_letters(pa_x, pa_word, pa_letters_in_word):
    for letter in pa_word:
        if letter is not " ":
            canvas.create_line(pa_x + 5, 100, pa_x + 35, 100, width=2)
            letter_id = canvas.create_text(pa_x + 20, 85, text=letter.upper(), font="arial 30", state=tkinter.HIDDEN)
            pa_letters_in_word[letter].append(letter_id)
        pa_x += 40


def draw_letter_placeholders(pa_x, pa_word):
    for letter in pa_word:
        if letter is not " ":
            canvas.create_line(pa_x + 5, 100, pa_x + 35, 100, width=2)
        pa_x += 40


def capture_user_input():
    while True:
        user_input = input("Guess a letter: ")
        first_letter = hl.take_first_letter_from_input(user_input)
        if hl.is_input_valid(first_letter):
            break
        else:
            print("You have to enter a letter")
            continue
    return first_letter


def show_letters_in_word(pa_letter_ids, pa_letter):
    letter_ids_to_be_shown = hl.find_letter_ids_to_be_shown(
        pa_letter_ids,
        pa_letter
    )
    for letter_id in letter_ids_to_be_shown:
        canvas.itemconfig(letter_id, state=tkinter.NORMAL)


def show_next_hangman_bodypart(
        pa_letter_ids,
        pa_already_guessed,
        pa_hangman_bodyparts):
    bodypart_index = hl.next_hangman_bodypart_index(
        pa_letter_ids,
        pa_already_guessed)
    canvas.itemconfig(
        pa_hangman_bodyparts[bodypart_index],
        state=tkinter.NORMAL)


def evaluate_game(pa_game_state):
    text, color = hl.evaluate_game(pa_game_state)
    canvas.create_text(320, 240, text=text, font="arial 45", fill=color)
    canvas.update()
    pause_game(3)


def pause_game(seconds):
    time.sleep(seconds)


draw_gallows(300, 240)
hangman_bodyparts = draw_hangman(300, 240)

words = hl.load_words_from_file("sk_words.txt")
random_word = hl.select_word_from_list(words, random.randint(0, len(words)))
del words

hl.add_word_letters_to_dict(random_word, hl.word_letters_with_ids)
starting_x_coord = 320 - (40 * len(random_word)) / 2
draw_letter_placeholders(starting_x_coord, random_word)
draw_letters(starting_x_coord, random_word, hl.word_letters_with_ids)
del random_word

while hl.the_game_can_continue(
        hl.number_of_hangman_bodyparts(hangman_bodyparts),
        hl.word_letters_with_ids,
        hl.already_guessed):
    canvas.update()
    try:
        guess = capture_user_input()
    except KeyboardInterrupt:
        sys.exit(1)

    if guess not in hl.already_guessed:
        hl.add_letter_to_already_guessed(guess)
    else:
        print("You've already guessed letter '" + guess + "'")
        continue

    if guess in hl.word_letters_with_ids:
        show_letters_in_word(hl.word_letters_with_ids, guess)
    else:
        show_next_hangman_bodypart(
            hl.word_letters_with_ids,
            hl.already_guessed,
            hangman_bodyparts)

    hl.game_state = hl.check_game_state(
        hl.number_of_hangman_bodyparts(hangman_bodyparts),
        hl.word_letters_with_ids,
        hl.already_guessed
    )

    canvas.update()

evaluate_game(hl.game_state)
