<p align="center">
  <img src="hangman/hangman-cli.ico" alt="Hangman Logo">
</p>

# Hangman-CLI
The classic word game, implemented in Python.

The current version selects words that are all names of animals.

## Rules of the game
#### Objective:
Your goal is to guess the hidden word, phrase, or sentence chosen by the other player.

#### How to play:
1. Enter your name when prompted.
2. The computer will think of a secret word and tell you how many letters are in the word.
3. Make guesses one letter at a time to guess the secret word.
4. Each time you guess a letter, all occurrences of that letter in the word will be shown.
5. If your guess is incorrect, a part of the hangman figure will be drawn.
6. Continue guessing letters to reveal the entire word.
7. You may quit at any time by pressing "Ctrl + C".

**Winning and Losing:**

* If you correctly guess the entire word before the full hangman figure is drawn, you win.
* If the full hangman figure is drawn before you guess the word, you lose.


## Installation Requirements
Hangman-CLI requires Python 3. This is usually available by default
in Linux. For other operating systems, it may be obtained from:
https://www.python.org/downloads/

## Where to Download
The latest version of Hangman-CLI may be downloaded from
https://github.com/SteveDaulton/Hangman-CLI/releases

### Linux installer
The installer app has been tested on Ubuntu and Debian.If you have any
difficulty with it on your system, please post an issue to:
https://github.com/SteveDaulton/Hangman-CLI/issues

1. Download the file: ` hangman_installer.run `
2. Double-click on the installer to install the game.

The installer will extract the following files:
* hangman-cli -> `~/.local/bin/hangman-cli`
* hangman-cli.ico -> `~/.local/share/icons/hangman-cli.ico`
* hangman-cli.desktop -> `~/.local/share/applications/hangman-cli.desktop`

The `hangman-cli.desktop` file should be detected automatically by the
Desktop menu and create a launcher in the `Games` section.

After installation, the game may be launched either from your Applications menu
or by entering the command `hangman-cli` in a Terminal window.

### All Platforms
The game is available from the same location as a single Python file:
1. Download the file: `hangman.py`
2. Open a Terminal, Command Prompt or PowerShell
3. Navigate to the folder containing `hangman.py`
4. Launch the game with the command: `python3 hangman.py`

## License
This program is released under the MIT license.
https://github.com/SteveDaulton/Hangman-CLI/blob/master/LICENSE

## Issues
Please report any issues here:
https://github.com/SteveDaulton/Hangman-CLI/issues

## Acknowledgments
The installer for this game was created using [makeself](https://makeself.io/).
