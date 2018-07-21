import unittest
import hangman_logic


class TestHangman(unittest.TestCase):

    def test_normalize_word_index(self):
        word_list = ['ahoj svet', 'pocasie', 'rukavice', 'nohavice', 'kryštál', 'slnko', 'trtko', 'cesta', 'je mi fajn']
        index = 1000
        self.assertEqual(
            hangman_logic._normalize_word_index(word_list, index),
            1
        )

    def test_select_first_word_from_list(self):
        word_list = ['ahoj svet', 'pocasie', 'rukavice', 'nohavice', 'kryštál', 'slnko', 'trtko', 'cesta', 'je mi fajn']
        self.assertEqual(
            hangman_logic.select_word_from_list(word_list, 0),
            "ahoj svet"
        )

    def test_select_last_word_from_list(self):
        word_list = ['ahoj svet', 'pocasie', 'rukavice', 'nohavice', 'kryštál', 'slnko', 'trtko', 'cesta', 'je mi fajn']
        self.assertEqual(
            hangman_logic.select_word_from_list(word_list, -1),
            "je mi fajn"
        )

    def test_select_nonexistent_word_from_list(self):
        word_list = ['ahoj svet', 'pocasie', 'rukavice', 'nohavice', 'kryštál', 'slnko', 'trtko', 'cesta', 'je mi fajn']
        self.assertEqual(
            hangman_logic.select_word_from_list(word_list, len(word_list) + 100),
            "pocasie"
        )

    def test_load_words_from_existing_file(self):
        filename = "sk_words.txt"
        self.assertEqual(
            hangman_logic.load_words_from_file(filename),
            ['ahoj svet', 'pocasie', 'rukavice', 'nohavice', 'kryštál', 'slnko', 'trtko', 'cesta', 'je mi fajn']
        )

    def test_load_words_from_non_existing_file(self):
        filename = "nonexisting_file.txt"
        self.assertEqual(
            hangman_logic.load_words_from_file(filename),
            []
        )

    def test_add_word_letters_to_dict_contains_letter(self):
        word_letters = set("rukavice")
        letter_dict = {}
        hangman_logic.add_word_letters_to_dict(word_letters, letter_dict)
        self.assertTrue(letter_dict['r'] == [])

    def test_add_word_letters_to_dict_doesnt_contain_letter(self):
        word_letters = set("rukavice")
        letter_dict = {}
        hangman_logic.add_word_letters_to_dict(word_letters, letter_dict)
        self.assertEqual("", letter_dict.get('x', ""))

    def test_add_word_letters_to_dict_contains_space(self):
        word_letters = set("ahoj svet")
        letter_dict = {}
        hangman_logic.add_word_letters_to_dict(word_letters, letter_dict)
        self.assertEqual(
            "no space found",
            letter_dict.get(" ", "no space found")
        )

    def test_take_first_letter_from_input_some_text(self):
        input_str = "asdfghjkl"
        self.assertEqual(
            hangman_logic.take_first_letter_from_input(input_str),
            "a"
        )

    def test_take_first_letter_from_input_no_text(self):
        input_str = ""
        self.assertEqual(
            "",
            hangman_logic.take_first_letter_from_input(input_str)
        )

    def test_is_input_valid_yes(self):
        usr_input = "a"
        self.assertTrue(hangman_logic.is_input_valid(usr_input))

    def test_is_input_valid_no(self):
        usr_input = "asdf"
        self.assertFalse(hangman_logic.is_input_valid(usr_input))

    def test_is_input_valid_number(self):
        usr_input = "1"
        self.assertFalse(hangman_logic.is_input_valid(usr_input))

    def test_is_input_valid_numbers(self):
        usr_input = "1234"
        self.assertFalse(hangman_logic.is_input_valid(usr_input))

    def test_is_input_valid_empty_string(self):
        usr_input = ""
        self.assertFalse(hangman_logic.is_input_valid(usr_input))

    def test_add_letter_to_already_guessed(self):
        hangman_logic.add_letter_to_already_guessed('c')
        self.assertTrue('c' in hangman_logic.already_guessed)

    def test_number_of_wrong_guesses_no_wrong_guesses(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'v', 'i', 'c', 'e']
        self.assertEqual(
            hangman_logic.number_of_wrong_guesses(letter_ids, already_guessed),
            0
        )

    def test_number_of_wrong_guesses_5_wrong_guesses(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 't' 'v', 'i', 'c', 'e']
        self.assertEqual(
            hangman_logic.number_of_wrong_guesses(letter_ids, already_guessed),
            5
        )

    def test_number_of_wrong_guesses_6_wrong_guesses(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 'q', 'x']
        self.assertEqual(
            hangman_logic.number_of_wrong_guesses(letter_ids, already_guessed),
            6
        )

    def test_number_of_hangman_bodyparts(self):
        bodyparts =  (3, 4, 5, 6, 7, 8)
        self.assertEqual(
            hangman_logic.number_of_hangman_bodyparts(bodyparts),
            6
        )

    def test_next_hangman_bodypart_index(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w']
        self.assertEqual(
            hangman_logic.next_hangman_bodypart_index(letter_ids, already_guessed),
            0
        )

    def test_max_num_of_wrong_guesses(self):
        self.assertEqual(
            hangman_logic.max_num_of_wrong_guesses(6),
            5
        )

    def test_wrong_guesses_under_limit(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é']
        self.assertFalse(hangman_logic.too_many_wrong_guesses(6, letter_ids, already_guessed))

    def test_wrong_guesses_above_limit(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 'q', 'x']
        self.assertTrue(hangman_logic.too_many_wrong_guesses(6, letter_ids, already_guessed))

    def test_all_letters_guessed(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'v', 'i', 'c', 'e']
        self.assertTrue(hangman_logic.all_letters_guessed(letter_ids, already_guessed))

    def test_all_letters_guessed_but_some_are_wrong(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['o', 'e', 'r', 'u', 'k', 'a', 'v', 'i', 'c', 'e']
        self.assertTrue(hangman_logic.all_letters_guessed(letter_ids, already_guessed))

    def test_some_letters_not_guessed(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é']
        self.assertFalse(hangman_logic.all_letters_guessed(letter_ids, already_guessed))

    def test_find_letter_ids_to_be_shown_letter_exists(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        letter = 'r'
        self.assertListEqual(
            hangman_logic.find_letter_ids_to_be_shown(letter_ids, letter),
            [10]
        )

    def test_find_letter_ids_to_be_shown_letter_doesnt_exists(self):
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        letter = 'x'
        self.assertListEqual(
            hangman_logic.find_letter_ids_to_be_shown(letter_ids, letter),
            []
        )

    def test_game_should_continue_wrong_guesses_under_limit_not_all_letters_guessed(self):
        num_of_hangman_bodyparts = 6
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é']
        self.assertTrue(hangman_logic.the_game_can_continue(
            num_of_hangman_bodyparts,
            letter_ids,
            already_guessed))

    def test_game_should_not_continue_wrong_guesses_above_limit(self):
        num_of_hangman_bodyparts = 6
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 'q', 'x']
        self.assertFalse(
            hangman_logic.the_game_can_continue(
                num_of_hangman_bodyparts,
                letter_ids,
                already_guessed)
        )

    def test_game_should_not_continue_all_letters_guessed_within_limit(self):
        num_of_hangman_bodyparts = 6
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 'v', 'i', 'c', 'e']
        self.assertFalse(
            hangman_logic.the_game_can_continue(
                num_of_hangman_bodyparts,
                letter_ids,
                already_guessed)
        )

    def test_check_game_state_running(self):
        num_of_hangman_bodyparts = 6
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é']
        self.assertEqual(
            hangman_logic.check_game_state(
                num_of_hangman_bodyparts,
                letter_ids,
                already_guessed
            ),
            "RUNNING"
        )

    def test_check_game_state_win(self):
        num_of_hangman_bodyparts = 6
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 'v', 'i', 'c', 'e']
        self.assertEqual(
            hangman_logic.check_game_state(
                num_of_hangman_bodyparts,
                letter_ids,
                already_guessed
            ),
            "WIN"
        )

    def test_check_game_state_loss(self):
        num_of_hangman_bodyparts = 6
        letter_ids = {'r': [10], 'u': [12], 'k': [14], 'a': [16], 'v': [18], 'i': [20], 'c': [22], 'e': [24]}
        already_guessed = ['r', 'u', 'k', 'a', 'w', 'y', 'z', 'é', 'q', 'x']
        self.assertEqual(
            hangman_logic.check_game_state(
                num_of_hangman_bodyparts,
                letter_ids,
                already_guessed
            ),
            "LOSS"
        )

    def test_evaluate_game_win(self):
        self.assertEqual(
            hangman_logic.evaluate_game("WIN"),
            ("CONGRATULATIONS", "GREEN")
        )

    def test_evaluate_game_loss(self):
        self.assertEqual(
            hangman_logic.evaluate_game("LOSS"),
            ("GAME OVER", "RED")
        )

    def test_evaluate_game_running(self):
        self.assertEqual(
            hangman_logic.evaluate_game("RUNNING"),
            ("RUNNING", "YELLOW")
        )

    def test_evaluate_game_undefined(self):
        self.assertEqual(
            hangman_logic.evaluate_game("UNDEFINED"),
            ("game state not defined", "GRAY")
        )
