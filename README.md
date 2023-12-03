<p align="center">
  <img src="hangman/hangman-cli.ico" alt="Hangman Logo">
</p>

# Hangman-CLI
The classic word game, implemented in Python.

The current version selects words from a chosen subject.

## Rules of the game
#### Objective:
Your goal is to guess the hidden word, phrase, or sentence chosen by the computer opponent.

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
Hangman-CLI requires Python version 3.9 or later.
This is usually available by default in Linux.
For other operating systems, Python may be downloaded from:
[Python.org](https://www.python.org/downloads/).

## Where to Download Hangman-CLI
Latest release (all files):
[Hangman-CLI Releases](https://github.com/SteveDaulton/Hangman-CLI/releases/latest/).

Each release includes:
- **hangman.py**: The Python application.
- **ascii_art.py**: The game's ascii artwork.
- **lexicon.py**: The game's wordlists.
- **hangman_installer.run**: An installer for Linux only.
- **Source code (zip)**: The source code (ZIP archive).
- **Source code (tar.gz)**: The source code (tarball),

### Using the Linux installer
The installer app has been tested on Ubuntu and Debian.If you have any
difficulty with it on your system, please post an issue [HERE](https://github.com/SteveDaulton/Hangman-CLI/issues)

1. Download the file:
[hangman_installer.run](https://github.com/SteveDaulton/Hangman-CLI/releases/latest/download/hangman_installer.run)
2. Set the file permissions to executable.
   - **GUI method:**

     - Right click on file > Properties
     - in the 'Permissions' tab, enable _"Allow this file to run as a program."_

   - **Command line method:**

     `chmod +x hangman_installer.run`

3. Double-click on the installer to install the game.

The installer will extract the following files:
* hangman-cli -> ~/.local/bin/Hangman-CLI/hangman-cli
* ascii_art.py -> ~/.local/bin/Hangman-CLI/ascii_art.py
* lexicon.py -> ~/.local/bin/Hangman-CLI/lexicon.py
* hangman-cli.ico -> `~/.local/share/icons/hangman-cli.ico`
* hangman-cli.desktop -> `~/.local/share/applications/hangman-cli.desktop`

The `hangman-cli.desktop` file should be detected automatically by the
Desktop menu and create a launcher in the `Games` section.

After installation, the game may be launched, either from your Applications menu
or by entering the command `hangman-cli` in a Terminal window.

**Uninstalling**
To uninstall hangman, run the installer in a terminal window:

    bash hangman_installer.run -- --clean

### All Platforms
If you don't have Linux, or prefer to play the game without installing,
Hangman-CLI is also available as a ZIP package.

#### Windows
**Preferred Method:**
1. Download the file: 
[hangman.py](https://github.com/SteveDaulton/Hangman-CLI/releases/latest/download/hangman-cli.zip)
2. Extract the contents of the ZIP file somewhere convenient.
3. Double-click on the hangman.py file.

**Alternate Method:**
1. Download the file: 
[hangman.py](https://github.com/SteveDaulton/Hangman-CLI/releases/latest/download/hangman-cli.zip)
2. Extract the contents of the ZIP file somewhere convenient.
3. Open Command Prompt by typing "cmd" in the Start menu.
4. Use `cd path\to\hangman.py` to navigate to the folder containing `hangman.py`
5. Launch the game with the command: `py hangman.py`

#### macOS
1. Download the file: 
[hangman.py](https://github.com/SteveDaulton/Hangman-CLI/releases/latest/download/hangman.py)
2. Extract the contents of the ZIP file somewhere convenient.
3. Drag the `hangman.py` file to **PythonLauncher**.

#### Linux
1. Download the file: 
[hangman.py](https://github.com/SteveDaulton/Hangman-CLI/releases/latest/download/hangman-cli.zip)
2. Extract the contents of the ZIP file somewhere convenient.
3. Open a Terminal window from the Applicatins menu, or "Ctrl + Alt + T".
4. Use `cd path/to/hangman.py` to navigate to the folder containing `hangman.py`
5. Launch the game with the command: `python3 hangman.py`

## License
This program is released under the [MIT license](https://github.com/SteveDaulton/Hangman-CLI/blob/master/LICENSE).

## Issues
Please report any issues [HERE](https://github.com/SteveDaulton/Hangman-CLI/issues).

## Acknowledgments
The installer for this game was created using [makeself](https://makeself.io/).
