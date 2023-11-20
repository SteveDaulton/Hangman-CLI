#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Hangman - A simple CLI game.

Guess a secret word letter by letter.
The player has a limited number of incorrect guesses before
the hangman is fully drawn.

This game displays ASCII art of the hangman, and updates it with
each incorrect guess. The player wins by guessing all letters of
the secret word correctly within the given attempts.

Usage:
    python3 hangman.py

Instructions:

- Enter your name when prompted.
- You'll be given a limited number of attempts to guess the secret word.
- Enter a single letter as your guess for each round. Letters may be
  capital letters or small letters, it makes no difference.
- If your guess is correct, the letter will be revealed in the word.
- If your guess is incorrect, a part of the hangman will be drawn.
- You win if you guess all letters before the hangman is fully drawn.

Good luck and have fun playing Hangman!

"""

import os
import sys
from collections import namedtuple
from random import randint
from time import sleep

PuzzleLetter = namedtuple('PuzzleLetter', ['character', 'guessed'])
Puzzle = list[PuzzleLetter]


def images() -> tuple[str, ...]:
    """Return a tuple of hangman (ascii) drawings."""
    return (
        r"""






=====""",

        r"""
    +
    |
    |
    |
    |
    |
=====""",

        r"""
 +--+
    |
    |
    |
    |
    |
=====""",

        r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""
    )


def get_word_list(category: str = 'animals') -> list[str]:
    """Return a list of quiz words.

    Define your list of words here.
    Words must be separated by white-space only.
    Each word list must have a unique name, and have an
    entry in the word_list_dict.

    Parameters
    ----------
    category: str
        Types of words, default: "animals"

    Returns
    -------
    list[str]
        List of words of selected category

    Raises
    ------
    ValueError
        If 'category' invalid.
    """

    category = category.lower()

    animal_words = """
    Dog Cat Elephant Lion Tiger Giraffe Zebra Bear Koala
    Panda Kangaroo Penguin Dolphin Eagle Owl Fox Wolf Cheetah
    Leopard Jaguar Horse Cow Pig Sheep Goat Chicken Duck Goose
    Swan Octopus Shark Whale Platypus Chimpanzee Gorilla Orangutan
    Baboon Raccoon Squirrel Bat Hedgehog Armadillo Sloth Porcupine
    Anteater Camel Dingo Kangaroo Rat Lemur Meerkat Ocelot Parrot
    Quokka Vulture Wombat Yak Iguana jaguar Kakapo Lemming
    Manatee Nutria Ostrich Pangolin Quail Rhinoceros Serval
    Wallaby Coypu Tapir Pheasant
    """

    word_list_dict = {'animals': animal_words}

    try:
        words: str = word_list_dict[category]
        return [word.upper() for word in words.split()]
    except KeyError as exc:
        raise ValueError("Invalid category.") from exc


def get_secret_word() -> str:
    """Return a random word from multiple options."""
    try:
        words: list[str] = get_word_list()
    except ValueError as exc:
        raise RuntimeError("Unable to retrieve word list.") from exc
    secret_word = words[randint(0, len(words) - 1)]
    if isinstance(secret_word, str) and len(secret_word) > 0:
        return secret_word
    raise RuntimeError("Unable to return secret word.")


class GameState:  # pylint: disable=too-many-instance-attributes
    """Manage state for the game.

    Provides getters and setters for current game state,
    update_game_state() with new guess.
    """

    def __init__(self) -> None:
        """Initialise attributes.
        """
        self._player_name: str = ''
        self._word: str = ''
        self._current_guess: str = ''
        self._guesses: set[str] = set()  # All letters guessed so far.
        self._remaining: set[str] = set()
        self._puzzle: Puzzle = []
        self._image_idx: int = 0  # Index of image to display

    def reset_current_game(self) -> None:
        """Reset current game settings.

        Some game settings, such as _player_name, need to persist
        across multiple games.
        """
        self._word = ''
        self._current_guess = ''
        self._guesses = set()
        self._remaining = set()
        self._puzzle = []
        self._image_idx = 0

    @property
    def player_name(self):
        """Return the player's name."""
        return self._player_name

    # Setter method
    @player_name.setter
    def player_name(self, val):
        self._player_name = val

    @property
    def word(self):
        """Return mystery word."""
        return self._word

    @word.setter
    def word(self, val):
        self._word = val

    @property
    def current_guess(self) -> str:
        """Return the current guess."""
        return self._current_guess

    @property
    def remaining_letters(self) -> set[str]:
        """Return set of letters still required."""
        return self._remaining

    def initialise_game(self, puzzle_word: str) -> None:
        """Add characters of word to _remaining set."""
        self.word = puzzle_word
        self._remaining = set(puzzle_word)
        self._puzzle = [PuzzleLetter(char, False) for char in puzzle_word]

    @property
    def guesses(self) -> set[str]:
        """Return set of all guesses tried in this game."""
        return self._guesses

    @property
    def image_idx(self) -> int:
        """Return image index."""
        return self._image_idx

    @property
    def puzzle(self) -> Puzzle:
        """Return puzzle list."""
        return self._puzzle

    def update_puzzle(self) -> None:
        """Return updated puzzle.

        Add 'True' to each matching tuple and return result.
        """
        self._puzzle = [PuzzleLetter(char, val or char == self.current_guess)
                        for char, val in self._puzzle]

    def update_game_state(self, new_guess: str) -> None:
        """Update game attributes according to current guess.

        If current_guess is in word, update game state.
        - update_puzzle()
        - List of remaining letters in word.

        Returns
        _______
        bool
            True if current guess in word.
        """
        self._current_guess = new_guess
        self._guesses.add(new_guess)
        try:
            self._remaining.remove(self.current_guess)
            self.update_puzzle()
        except KeyError:
            self._image_idx += 1  # Not in word

    def is_good_guess(self) -> bool:
        """Return True if current guess in puzzle word."""
        return self.current_guess in self._word

    def get_image(self) -> str:
        """Return hangman ascii drawing."""
        return images()[self._image_idx]

    def player_loses(self) -> bool:
        """Return True if player has lost."""
        return self.image_idx == len(images()) - 1


class UI:
    """User interface class."""

    def __init__(self, game_state: GameState) -> None:
        """Initialise UI.

        Parameters
        ----------
        game_state: GameState
            Game state
        """
        self.game_state = game_state
        self._indent = ' ' * 4

    def reset_game(self) -> None:
        """Reset GameState parameters that refer to current game."""
        self.game_state.reset_current_game()

    def indent_text(self, text: str):
        """Indent each printed line."""
        indented = '\n'.join(
            [self._indent + line for line in str(text).split('\n')])
        return indented

    def display_message(self, message: str) -> None:
        """Display arbitrary text message to player."""
        message = self.indent_text(message)
        print(message)

    def do_welcome(self) -> None:
        """Welcome new player.

        Get player's name, print welcome message and
        return player's name.

         Returns
         -------
         str
            The player's name.
        """
        UI.clear_terminal()
        self.print_slowly("Hi there. What's your name?", end=' ')
        player_name = input().title()
        self.print_slowly(f"Hello {player_name}.", end='\n')
        self.print_slowly(
            "You can quit at any time by pressing 'Ctrl + C'.", 8)
        self.game_state.player_name = player_name

    def print_intro(self) -> None:
        """Print introduction to game.
        """
        self.print_slowly(f"OK {self.game_state.player_name}, let's play.")
        self.print_slowly("I'll think of a word""", end='')
        self.print_slowly(' .' * randint(3, 8), speed=5, indent=False)
        UI.clear_terminal()

    @staticmethod
    def get_guess(game: GameState) -> str:
        """Return a new guess.

        Parameters
        ----------
        game: GameState
            The current game state.

        Returns
        -------
        str
            The guess - a single character string.
        """
        while True:
            print("Guess a letter: ", end='')
            new_guess = input().strip().upper()

            if len(new_guess) != 1:
                print("Guesses must be one letter only.")
                continue
            if new_guess in game.guesses:
                print(f"You've already guessed '{new_guess}'")
                continue
            return new_guess

    def print_game_start(self) -> None:
        """Inform user of word length."""
        self.print_slowly(
            "I've thought of a word.\n"
            f"The word has {len(self.game_state.word)} letters.")
        sleep(1)
        UI.clear_terminal()

    def print_game_result(self, is_winner: bool, correct_answer: str) -> None:
        """Congratulate or console player."""
        if is_winner:
            self.print_slowly(f"Well done {self.game_state.player_name}. "
                              f"YOU WIN!", 20)
        else:
            self.print_slowly(
                f"Too bad {self.game_state.player_name}, you loose. "
                f"The word was {correct_answer}."
                "Better luck next time.", 6)

    @staticmethod
    def prompt_confirm(prompt: str) -> bool:
        """Prompt for yes/no answer.

        Parameters
        ----------
        prompt: str
            The message prompt.

        Returns
        -------
        bool
            True if yes, else False.
        """
        yes = ('y', 'yes')
        no = ('n', 'no')
        while True:
            print(prompt, end='')
            val = input()
            if val in yes:
                return True
            if val in no:
                return False
            print("Enter 'Y' or 'N'.")

    def update_screen(self, clear: bool = True) -> None:
        """Refresh screen with current game state."""
        if clear:
            UI.clear_terminal()
        # Print hangman image.
        print(self.indent_text(self.game_state.get_image()))
        # Print underscores and guessed letters.
        output = [f'{char} ' if val else '_ ' for
                  char, val in self.game_state.puzzle]
        print(self.indent_text(f'{"".join(output)}\n\n'))

    def do_quit(self) -> None:
        """Exit the program."""
        print(self.indent_text(f"\nBye {self.game_state.player_name}."),
              flush=True)
        sys.exit()

    @staticmethod
    def clear_terminal() -> None:
        """Clear the terminal.

        This method is intended to support both Posix and Windows
        even though hangman-cli 1.x only officially supports Linux."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_slowly(self,
                     message: str,
                     speed: float = 10.0,
                     end: str = '\n',
                     indent: bool = True) -> None:
        """Print message one character at a time.

        Pauses for 1/speed seconds between characters

        Parameters
        ----------
        message: str
            The message to print
        end: str
            Line termination
        speed: int
            How fast to print. Higher = faster
        indent: bool
            Whether to indent the line, default: True
        """
        try:
            delay = abs(1 / speed)
        except ZeroDivisionError:
            print(self.indent_text("Invalid speed. Defaulting to speed = 4"))
            delay = 0.25
        for line in message.split('\n'):
            if indent:
                print(self._indent, end='')
            for char in line:
                sleep(delay)
                print(char, flush=True, end='')
            print(end=end)


def play_game(ui: UI) -> bool:
    """Play game.

    Main game loop.

    Parameters
    ----------

    Returns
    -------
    bool:
        True if player wins, else False.
    """
    game = ui.game_state
    ui.update_screen(clear=False)

    while game.remaining_letters:
        # Update the game state from player guess.
        game.update_game_state(ui.get_guess(game))
        # Display the result.
        ui.update_screen()
        if game.is_good_guess():
            ui.display_message(f"{game.current_guess} is correct.")
        else:
            ui.display_message(f"{game.current_guess} is wrong.")

        # Return False if hangman complete.
        if game.player_loses():
            return False
    return True


def game_session(ui: UI) -> None:
    """Start the Hangman game for the named player.

    Displays a welcome message to the player, generates a secret word, and
    initiates the game loop. Prints a win or loose message when game completes.
    """
    if ui.game_state.player_name == '':
        ui.do_welcome()
    ui.print_intro()
    game_state = ui.game_state

    try:
        secret_word = get_secret_word()
        game_state.initialise_game(secret_word)
    except RuntimeError as exc:
        print(f"Sorry, there has been an error: {exc}")
        sys.exit()
    ui.print_game_start()
    # Play game and get result
    player_wins = play_game(ui)
    ui.print_game_result(player_wins, game_state.word)
    ui.reset_game()


def main():
    """Main loop.

    Instantiate an instance of GameState(), which will persist for
    life of program. A new user interface UI() object is created
    for each game. Play game repeatedly until player quits.
    """
    state = GameState()
    while True:
        ui = UI(state)
        try:
            game_session(ui)
        except KeyboardInterrupt:
            ui.do_quit()
        if ui.prompt_confirm("Play again? [y/n] "):
            continue
        ui.do_quit()


if __name__ == '__main__':
    # Check Python version
    if sys.version_info < (3, 9):
        print("Hangman-CLI requires Python 3.9 or later.")
        print("Please update your Python version.")
        sys.exit(1)
    main()
