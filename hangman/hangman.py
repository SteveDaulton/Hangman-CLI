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

Author: Steve Daulton

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


def clear_terminal() -> None:
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def images() -> tuple[str, ...]:
    """Return a tuple of hangman (ascii) drawings."""
    return (r"""
    
    
    
    
    
    
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
    =====""")


def word_list() -> list[str]:
    """Return a list of quiz words.

    Define your list of words here.
    Words must be separated by white-space only.
    """
    quiz_words = """
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
    return [word.upper() for word in quiz_words.split()]


def print_slowly(message: str, speed: float = 10.0, end: str = '\n') -> None:
    """Print message one character at a time.

    Pauses for 1/speed seconds between characters

    Parameters
    ----------
    message: str
        The message to print
    end: str
        Line termination.

    speed: int
        How fast to print. Higher = faster
    """
    try:
        delay = abs(1 / speed)
    except ZeroDivisionError:
        print("Invalid speed. Defaulting to speed = 4")
        delay = 0.25
    for char in message:
        sleep(delay)
        print(char, end='', flush=True)
    print(end=end)


def get_secret_word() -> str:
    """Return a random word from multiple options."""
    words = word_list()
    return words[randint(0, len(words) - 1)]


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
        val = input(prompt)
        if val in yes:
            return True
        if val in no:
            return False
        print("Enter 'Y' or 'N'.")


def do_quit(player: str) -> None:
    """Exit the program."""
    print(f"\nBye {player}.")
    sys.exit()


def play_game(word_to_guess: str) -> bool:
    """Play game.

    Main game loop.

    Parameters
    ----------
    word_to_guess: str
        The secret word that the player has to guess.

    Returns
    -------
    bool:
        True if player wins, else False.
    """
    game = GameState(word_to_guess)
    update_screen(game, clear=False)

    while game.remaining_letters:
        # Update the game state from player guess.
        game.update_game_state(get_guess(game))
        # Display the result.
        update_screen(game)
        if game.is_good_guess():
            print(f"{game.current_guess} is correct.")
        else:
            print(f"{game.current_guess} is wrong.")

        # Return False if hangman complete.
        if game.player_loses():
            return False
    return True


class GameState:
    """Manage state for the game."""

    def __init__(self, word: str) -> None:
        """Initialise attributes."""
        self.__word = word
        self.__current_guess = ''
        self.__guesses: set[str] = set()  # All letters guessed so far.
        self.__remaining: set[str] = set(word)
        self.__puzzle: Puzzle = [PuzzleLetter(char, False) for char in word]
        self.__image_idx = 0  # Index of image to display

    def update_puzzle(self) -> None:
        """Return updated puzzle.

        Add 'True' to each matching tuple and return result.
        """
        self.__puzzle = [PuzzleLetter(char, val or char == self.current_guess)
                         for char, val in self.__puzzle]

    @property
    def current_guess(self) -> str:
        """Return the current guess."""
        return self.__current_guess

    @property
    def remaining_letters(self) -> set[str]:
        """Return set of letters still required."""
        return self.__remaining

    @property
    def guesses(self) -> set[str]:
        """Return set of all guesses tried in this game."""
        return self.__guesses

    @property
    def image_idx(self) -> int:
        """Return image index."""
        return self.__image_idx

    @property
    def puzzle(self) -> Puzzle:
        """Return puzzle list."""
        return self.__puzzle

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
        self.__current_guess = new_guess
        self.__guesses.add(new_guess)
        try:
            self.__remaining.remove(self.current_guess)
            self.update_puzzle()
        except KeyError:
            self.__image_idx += 1  # Not in word

    def is_good_guess(self) -> bool:
        """Return True if current guess in puzzle word."""
        return self.current_guess in self.__word

    def get_image(self) -> str:
        """Return hangman ascii drawing."""
        return images()[self.__image_idx]

    def player_loses(self) -> bool:
        """Return True if player has lost."""
        return self.image_idx == len(images()) - 1


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
        new_guess = input("Guess a letter: ").strip().upper()

        if len(new_guess) != 1:
            print("Guesses must be one letter only.")
            continue
        if new_guess in game.guesses:
            print(f"You've already guessed '{new_guess}'")
            continue
        return new_guess


def update_screen(game: GameState, clear: bool = True) -> None:
    """Refresh screen with current game state."""
    if clear:
        clear_terminal()
    # Print hangman image.
    print(game.get_image())
    # Print underscores and guessed letters.
    output = [f'{char} ' if val else '_ ' for char, val in game.puzzle]
    print(''.join(output))
    print()


def main(player: str) -> None:
    """Start the Hangman game for the named player.

    Displays a welcome message to the player, generates a secret word, and
    initiates the game loop. Prints a win or loose message when game completes.

    Parameters
    ----------
    player : str
        The name of the player.
    """
    print_slowly(f"OK {player}. Let's play Hangman.")
    print_slowly("I'll think of a word.""", end=' ')
    print_slowly('. ' * randint(3, 8), 5)
    clear_terminal()
    word = get_secret_word()
    print_slowly("I've thought of a word.")
    print_slowly(f"The word has {len(word)} letters.")
    sleep(1)
    clear_terminal()
    # Play game and get result
    player_wins = play_game(word)
    if player_wins:
        print_slowly(f"Well done {player}. YOU WIN!", 20)
    else:
        print_slowly(f"Too bad {player}, you loose. "
                     f"The word was {word}."
                     f"Better luck next time.", 6)


if __name__ == '__main__':
    clear_terminal()
    print_slowly("Hi there. What's your name?", end=' ')
    name = input()
    print_slowly(f"Hello {name}.")
    print_slowly("\nYou can quit at any time by pressing 'Ctrl + C'.\n", 8)
    while True:
        try:
            main(name)
        except KeyboardInterrupt:
            do_quit(name)
        if not prompt_confirm("Play again? [y/n] "):
            do_quit(name)
