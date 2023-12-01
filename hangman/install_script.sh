#!/bin/bash

APP_DIR="$HOME/.local/bin/Hangman-CLI"
ICON_DIR="$HOME/.local/share/icons"
DESKTOP_DIR="$HOME/.local/share/applications"

# Cleanup old version if present
if [ -f "$APP_DIR/hangman-cli" ]; then
    rm "$APP_DIR/hangman-cli"
fi

# Ensure the installation directories exist
mkdir -p "$APP_DIR"
mkdir -p "$ICON_DIR"
mkdir -p "$DESKTOP_DIR"

# Copy the .py files
cp hangman.py "$APP_DIR/hangman-cli"
cp ascii_art.py "$APP_DIR"
cp lexico.py "$APP_DIR"

# Copy the icon file
cp hangman-cli.ico "$ICON_DIR"

# Make app executable
chmod +x "$APP_DIR/hangman-cli"

# Create a desktop file
DESKTOP_FILE="$APP_DIR/hangman-cli.desktop"
echo "[Desktop Entry]" > "$DESKTOP_FILE"
echo "Version=1.2.0" >> "$DESKTOP_FILE"
echo "Type=Application" >> "$DESKTOP_FILE"
echo "Name=Hangman-CLI" >> "$DESKTOP_FILE"
echo "GenericName=Hangman" >> "$DESKTOP_FILE"
echo "Comment=Hangman, the classic word game" >> "$DESKTOP_FILE"
echo "Exec=$APP_DIR/hangman-cli" >> "$DESKTOP_FILE"
echo "Icon=$ICON_DIR/hangman-cli.ico" >> "$DESKTOP_FILE"
echo "Terminal=true" >> "$DESKTOP_FILE"
echo "StartupNotify=false" >> "$DESKTOP_FILE"
echo "Categories=Game;LogicGame;" >> "$DESKTOP_FILE"

# Update the icon cache
if gtk-update-icon-cache -f -t "$ICON_DIR"; then
    echo "Icon cache updated."
else
    echo "Failed to update icon cache."
fi

# Update the desktop database (for menu item)
if update-desktop-database "$DESKTOP_DIR"; then
    echo "Desktop database updated."
else
    echo "Failed to update desktop database."
fi

echo "Installation complete!"
