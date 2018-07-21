def _normalize_word_index(pa_word_list, pa_index):
    return pa_index % len(pa_word_list)


def select_word_from_list(pa_word_list, pa_index):
    index = _normalize_word_index(pa_word_list, pa_index)
    word = pa_word_list[index]
    return word


def load_words_from_file(pa_file_name):
    try:
        with open(pa_file_name, "r") as fp:
            word_list = fp.read().splitlines()
        return word_list
    except FileNotFoundError:
        return []


def add_word_letters_to_dict(pa_word, pa_letter_ids):
    word_letters = set(pa_word)

    try:
        word_letters.remove(" ")
    except KeyError:
        pass

    for letter in word_letters:
        pa_letter_ids[letter] = []
    return word_letters_with_ids.keys()


def add_letter_to_already_guessed(pa_letter):
    already_guessed.add(pa_letter)


def number_of_wrong_guesses(pa_letter_ids, pa_already_guessed):
    word_letters = set(pa_letter_ids.keys())
    already_guessed_letters = set(pa_already_guessed)
    return len(already_guessed_letters.difference(word_letters))


def is_input_valid(pa_user_input):
    return len(pa_user_input) == 1 \
           and pa_user_input.isalpha() \
           and pa_user_input is not ""


def take_first_letter_from_input(pa_user_input):
    if len(pa_user_input) <= 0:
        return ""
    first_letter = pa_user_input[0]
    return first_letter


def find_letter_ids_to_be_shown(pa_letter_ids, pa_letter):
    return pa_letter_ids.get(pa_letter, list())


def number_of_hangman_bodyparts(pa_hangman_bodyparts):
    return len(pa_hangman_bodyparts)


def next_hangman_bodypart_index(pa_letter_ids, pa_already_guessed):
    return number_of_wrong_guesses(pa_letter_ids, pa_already_guessed) - 1


def max_num_of_wrong_guesses(pa_num_of_hangman_bodyparts):
    return pa_num_of_hangman_bodyparts - 1


def too_many_wrong_guesses(
        pa_num_of_hangman_bodyparts,
        pa_letter_ids,
        pa_already_guessed):
    return number_of_wrong_guesses(pa_letter_ids, pa_already_guessed) \
           > \
           max_num_of_wrong_guesses(pa_num_of_hangman_bodyparts)


def all_letters_guessed(pa_letter_ids, pa_already_guessed):
    word_letters = set(pa_letter_ids.keys())
    already_guessed_letters = set(pa_already_guessed)
    return word_letters.issubset(already_guessed_letters)


# Truth table, when the game should continue, and when should it stop
# -------------------------------------------------------------------
# Wrong_guesses_limit_reached   All_letters_guessed   Game continues
# 0                             0                     1
# 0                             1                     0
# 1                             0                     0
# 1                             1                     0
def the_game_can_continue(
        pa_num_of_hangman_bodyparts,
        pa_letter_ids,
        pa_already_guessed):
    return \
        not(too_many_wrong_guesses(
                pa_num_of_hangman_bodyparts,
                pa_letter_ids,
                pa_already_guessed)
            or
            all_letters_guessed(pa_letter_ids, pa_already_guessed))


def check_game_state(
        pa_num_of_hangman_bodyparts,
        pa_letter_ids,
        pa_already_guessed):
    if all_letters_guessed(pa_letter_ids, pa_already_guessed):
        return "WIN"
    elif too_many_wrong_guesses(
            pa_num_of_hangman_bodyparts,
            pa_letter_ids,
            pa_already_guessed):
        return "LOSS"
    return "RUNNING"


def evaluate_game(pa_game_state):
    if pa_game_state == "WIN":
        return "CONGRATULATIONS", "GREEN"
    elif pa_game_state == "LOSS":
        return "GAME OVER", "RED"
    elif pa_game_state == "RUNNING":
        return "RUNNING", "YELLOW"
    else:
        return "game state not defined", "GRAY"


word_letters_with_ids = {}
already_guessed = set()
game_state = ""
