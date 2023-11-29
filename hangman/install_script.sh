#!/bin/bash

mkdir -p ~/.local/bin
cp hangman.py ~/.local/bin/hangman-cli
chmod +x ~/.local/bin/hangman-cli

mkdir -p ~/.local/share/icons
cp hangman-cli.ico ~/.local/share/icons/

# Create a desktop file
mkdir -p ~/.local/share/applications
DESKTOP_FILE=~/.local/share/applications/hangman-cli.desktop
echo "[Desktop Entry]" > "$DESKTOP_FILE"
echo "Version=1.2.0" >> "$DESKTOP_FILE"
echo "Type=Application" >> "$DESKTOP_FILE"
echo "Name=Hangman-CLI" >> "$DESKTOP_FILE"
echo "GenericName=Hangman" >> "$DESKTOP_FILE"
echo "Comment=Hangman, the classic word game" >> "$DESKTOP_FILE"
echo "Exec=$HOME/.local/bin/hangman-cli" >> "$DESKTOP_FILE"
echo "Icon=$HOME/.local/share/icons/hangman-cli.ico" >> "$DESKTOP_FILE"
echo "Terminal=true" >> "$DESKTOP_FILE"
echo "StartupNotify=false" >> "$DESKTOP_FILE"
echo "Categories=Game;LogicGame;" >> "$DESKTOP_FILE"

# Update the icon cache
gtk-update-icon-cache -f -t ~/.local/share/icons/

# Update the desktop database (for menu item)
update-desktop-database ~/.local/share/applications/

echo "Installation complete!"
