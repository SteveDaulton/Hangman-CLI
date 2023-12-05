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
from dataclasses import dataclass, field
from random import randint
from time import sleep

from ascii_art import ascii_images as art
from lexicon import get_word_list, get_categories

PuzzleLetter = namedtuple('PuzzleLetter', ['character', 'guessed'])
"""Type definition for a namedtuple('character', 'guessed').

character: str
    One of the characters from the mystery word.
guessed: bool
    True if the letter has been guessed, else False.
"""

Puzzle = list[PuzzleLetter]
"""Type definition for a list of PuzzleLetter's."""


def get_secret_word(category: str) -> str:
    """Return a random word from multiple options."""
    try:
        words: list[str] = get_word_list(category)
    except ValueError as exc:
        raise RuntimeError("Unable to retrieve word list.") from exc
    secret_word = words[randint(0, len(words) - 1)]
    if isinstance(secret_word, str) and len(secret_word) > 0:
        return secret_word
    raise RuntimeError("Unable to return secret word.")


@dataclass
class GameState:
    """Manage state for the game.

    Attributes
    ----------
    player_name : str
        The player's name.
    score : dict[str, int]
        Game wins and losses.
    word : str
        The mystery word.
    current_guess : str
        The current guess.
    guesses : set
        The set of all guesses tried in this game.
    remaining_letters : set
        The set of letters still required.
    puzzle : list
        Puzzle list.
    image_idx : int
        Index of the image to display.
    """
    # pylint: disable=too-many-instance-attributes
    player_name: str = ''
    score: dict[str, int] = field(default_factory=dict)
    category: str = ''
    word: str = ''
    current_guess: str = ''
    guesses: set[str] = field(default_factory=set)
    remaining_letters: set[str] = field(default_factory=set)
    puzzle: Puzzle = field(default_factory=list)
    image_idx: int = 0

    def initialise_game_state(self) -> None:
        """Post-instantiation initialisation.

        Complete the initialisation of GameState after
        puzzle_word has been set.
        """
        self.remaining_letters = set(self.word)
        self.puzzle = [PuzzleLetter(char, False) for char in self.word]

    def update_state_on_guess(self) -> None:
        """Update the game state based on the current guess.

        Checks first for a whole word guess.
        Tries to remove the guessed letter from the remaining_letters set.
        If the letter is not in the word, increment the image index.
        """
        if len(self.current_guess) > 1:  # Word guess
            if self.current_guess == self.word:  # Correct guess
                self.remaining_letters.clear()
                self.update_puzzle()
            else:
                self.image_idx += 1  # Wrong word.
        try:
            self.remaining_letters.remove(self.current_guess)
            self.update_puzzle()
        except KeyError:
            self.image_idx += 1  # Not in word.

    def update_puzzle(self) -> None:
        """Return updated puzzle.

        Called by update_game_state to handle updating the puzzle data.
        Add 'True' to each matching tuple and return result.
        """
        if self.current_guess == self.word:  # Whole word guessed.
            self.puzzle = [PuzzleLetter(char, True) for char, _ in self.puzzle]
            return
        self.puzzle = [
            PuzzleLetter(char, val or (char == self.current_guess))
            for char, val in self.puzzle]

    def reset_current_game(self) -> None:
        """Reset current game settings.

        Does not reset entire session as some game settings,
        such as _player_name, need to persist across multiple games.
        """
        self.word = ''
        self.current_guess = ''
        self.guesses = set()
        self.remaining_letters = set()
        self.puzzle = []
        self.image_idx = 0


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

    def indent_text(self, text: str):
        """Indent each printed line."""
        indented = '\n'.join(
            [self._indent + line for line in str(text).split('\n')])
        return indented

    def display_message(self, message: str, end: str = '\n') -> None:
        """Display arbitrary text message to player.

        In the CLI interface, text is indented for an improved
        aesthetic appearance.
        """
        message = self.indent_text(message)
        print(message, end=end)

    def do_welcome(self) -> str:
        """Welcome new player.

        Get player's name, print welcome message and return player's name.

        Returns
        -------
        str
            The player's name.
        """
        UI.clear_terminal()
        self.print_slowly("Hi there. What's your name?", end=' ')
        player_name = input().title()
        self.print_slowly(f"Hello {player_name}.", end='\n\n')
        self.print_slowly(
            "You can quit at any time by pressing 'Ctrl + C'.",
            speed=8, end='\n\n')
        return player_name

    def prompt_category(self, categories: tuple) -> str:
        """Prompt user to select a category.

        Returns
        -------
        str
            The name of the selected category.
        """
        self.display_message("Select one of these categories:")
        for idx, cat in enumerate(categories):
            self.display_message(f"{idx}. {cat}")
        while True:
            category = input("Enter a number: ")
            try:
                category = categories[int(category)]
            except (ValueError, IndexError):
                self.display_message(f"{category} is not an option.")
                self.display_message("Please try again.")
            else:
                return category

    def print_intro(self) -> None:
        """Print introduction to game.
        """
        self.print_slowly(f"OK {self.game_state.player_name}, let's play.")
        self.print_slowly("I'll think of a word""", end='')
        self.print_slowly(' .' * randint(3, 8), speed=5, indent=False)
        UI.clear_terminal()

    def get_guess(self) -> str:
        """Return a new guess.

        Returns
        -------
        str
            The guess - a single character or a whole word.
        """
        while True:
            print("Guess a letter: ", end='')
            new_guess = input().strip().upper()

            if new_guess in self.game_state.guesses:
                print(f"You've already guessed '{new_guess}'")
                continue
            if (len(new_guess) != 1 and
                    len(new_guess) != len(self.game_state.word)):
                word_len = len(self.game_state.word)
                print("Guesses must be one letter or"
                      f"the whole {word_len} letter word.")
                continue
            return new_guess

    def display_game_start_screen(self) -> None:
        """Inform user of word length."""
        self.print_slowly(
            "I've thought of a word.\n"
            f"The word has {len(self.game_state.word)} letters.")
        sleep(1)
        UI.clear_terminal()

    def display_game_result(self,
                            is_winner: bool,
                            correct_answer: str) -> None:
        """Congratulate or console player."""
        self.clear_terminal()
        # Print score
        wins, losses = self.game_state.score.values()
        self.display_message(f"Won: {wins}  Lost: {losses}\n")

        if is_winner:
            self.print_slowly(f"Well done {self.game_state.player_name}. "
                              f"YOU WIN!", 20)
        else:
            self.print_slowly(
                f"Too bad {self.game_state.player_name}, you loose. "
                f"The word was {correct_answer}.")
            self.print_slowly("Better luck next time.", 6)

    def get_image(self) -> str:
        """Return hangman ascii drawing."""
        return art()[self.game_state.image_idx]

    def prompt_confirm(self, prompt: str) -> bool:
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
            self.display_message(prompt, end='')
            val = input()
            if val in yes:
                self.clear_terminal()
                return True
            if val in no:
                self.clear_terminal()
                return False
            print("Enter 'Y' or 'N'.")

    def update_screen(self, clear: bool = True) -> None:
        """Refresh screen with current game state."""
        if clear:
            UI.clear_terminal()
        # Print score
        wins, losses = self.game_state.score.values()
        self.display_message(f"Won: {wins}  Lost: {losses}")
        # Print hangman image.
        self.display_message(self.get_image())
        # Print underscores and guessed letters.
        output = [f'{char} ' if val else '_ ' for
                  char, val in self.game_state.puzzle]
        self.display_message(f'{"".join(output)}\n\n')

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
            self.display_message("Invalid speed. Defaulting to speed = 4")
            delay = 0.25
        for line in message.split('\n'):
            if indent:
                print(self._indent, end='')
            for char in line:
                sleep(delay)
                print(char, flush=True, end='')
            print(end=end)

    def display_exit_dialog(self) -> None:
        """Dialog before quitting."""
        self.display_message(f"\nBye {self.game_state.player_name}.")


class Hangman:
    """Game logic class.

    Attributes
    ----------
    self.state: GameState
        Game state manager.
    self.ui: UI
        User interface.
    """
    def __init__(self) -> None:
        """Constructor of game logic class."""
        self.state = GameState()
        self.ui = UI(self.state)
        self.wins: int = 0
        self.losses: int = 0

    def play_game(self) -> bool:
        """Play game.

        Main game loop.

        Returns
        -------
        bool:
            True if player wins, else False.
        """
        self.ui.update_screen(clear=False)

        while self.state.remaining_letters:
            # Update the game state from player guess.
            # Get new guess
            new_guess = self.ui.get_guess()
            self.update_game_state(new_guess)
            # Display the result.
            self.ui.update_screen()
            if self.is_good_guess():
                self.ui.display_message(
                    f"{self.state.current_guess} is correct.")
            else:
                self.ui.display_message(
                    f"{self.state.current_guess} is wrong.")

            # Return False if hangman complete.
            if self.player_loses():
                self.losses += 1
                self.state.score['losses'] = self.losses
                return False
        self.wins += 1
        self.state.score['wins'] = self.wins
        return True

    def initialise_game(self, puzzle_word: str) -> None:
        """Post-instantiation initialisation.

        Complete the initialisation from puzzle_word.
        """
        self.state.word = puzzle_word
        self.state.initialise_game_state()

    def update_game_state(self, new_guess: str) -> None:
        """Update game attributes according to current guess.

        Guess may be a single letter or the entire word.
        - update GameState::current_guess
        - update GameState::guesses
        Then tell GameState() instance to manage its own update,
        """
        self.state.current_guess = new_guess
        # state.guesses is usually single letters but may
        # be a whole word.
        self.state.guesses.add(new_guess)
        self.state.update_state_on_guess()

    def is_good_guess(self) -> bool:
        """Return True if current guess in puzzle word."""
        return self.state.current_guess in self.state.word

    def player_wins(self) -> None:
        """Handle player winning.

        Game is won when word is guessed before final
        hangman image is displayed.
        """
        self.state.score['wins'] += 1

    def player_loses(self) -> bool:
        """Return True if player has lost.

        Game is lost when final hangman image is displayed.
        """
        return self.state.image_idx == len(art()) - 1

    def do_quit(self) -> None:
        """Exit the program."""
        self.ui.display_exit_dialog()
        sleep(2)
        sys.exit()


def new_game(game: Hangman) -> None:
    """A single complete game.

    Displays a welcome message to the player, generates a secret word, and
    initiates a game. Prints a win or loose message when game completes.

    Parameters
    ----------
    game: Hangman
        Instance of the game logic class.
    """
    state = game.state
    state.score = {'wins': game.wins, 'losses': game.losses}
    ui = game.ui

    # player_name initialised only in first game.
    if state.player_name == '':
        state.player_name = ui.do_welcome()

    state.category = ui.prompt_category(get_categories())

    ui.print_intro()

    try:
        secret_word = get_secret_word(state.category)
    except RuntimeError as exc:
        print(f"Sorry, there has been an error: {exc}")
        sys.exit()
    # Now that we have player_name and secret_word
    # we can complete initialisation of GameState.
    game.initialise_game(secret_word)

    ui.display_game_start_screen()

    # Play game and get result
    player_wins = game.play_game()
    ui.display_game_result(player_wins, state.word)

    # Reset for next game.
    state.reset_current_game()


def main():
    """Main loop.

    Instantiate an instance of Hangman game, which will
    persist for the life of program.
    Play game repeatedly until player quits.
    """
    new_game_session = Hangman()
    while True:
        try:
            new_game(new_game_session)
        except KeyboardInterrupt:
            new_game_session.do_quit()
        if new_game_session.ui.prompt_confirm("Play again? [y/n] "):
            continue
        new_game_session.do_quit()


if __name__ == '__main__':
    # Check Python version
    if sys.version_info < (3, 9):
        print("Hangman-CLI requires Python 3.9 or later.")
        print("Please update your Python version.")
        sys.exit(1)
    main()
