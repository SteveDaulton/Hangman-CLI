#!/bin/bash

OLD_APP_DIR="$HOME/.local/bin"
APP_DIR="$HOME/.local/bin/Hangman-CLI"
ICON_DIR="$HOME/.local/share/icons"
DESKTOP_DIR="$HOME/.local/share/applications"

function update_menus() {
  echo "Updating menus ..."

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
  }

function handle_error() {
  echo "Error occurred. Cleaning up..."
  uninstall
  exit 1
  }

function uninstall() {
  echo "Uninstalling Hangman-CLI..."
  local error_flag=0

  uninstall_old

  if [ -d "$APP_DIR" ]; then
    rm -r "$APP_DIR" || {
      echo "Failed to delete $APP_DIR"
      error_flag=1
      }
  fi

  if [ -f "$ICON_DIR/hangman-cli.ico" ]; then
    rm "$ICON_DIR/hangman-cli.ico" || {
      echo "Failed to delete $ICON_DIR/hangman-cli.ico"
      error_flag=1
      }
  fi

  if [ -f "$DESKTOP_DIR/hangman-cli.desktop" ]; then
    rm "$DESKTOP_DIR/hangman-cli.desktop" || {
      echo "Failed to delete $DESKTOP_DIR/hangman-cli.desktop"
      error_flag=1
      }
  fi
  exit "$error_flag"
  }


function uninstall_old() {
  # Cleanup old version if present
  if [ -f "$OLD_APP_DIR/hangman-cli" ]; then
    rm "$OLD_APP_DIR/hangman-cli"
  fi
}


# Check for command-line argument to print help.
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
  echo "Usage:"
  echo -e "\tsh install_script.sh [options]\n"
  echo "-h, --help \tShow this help and exit."
  echo "-c, --clean \tUninstall Hangman-CLI."
  exit 0
fi


# Check for command-line argument to uninstall.
if [ "$1" == "-c" ] || [ "$1" == "--clean" ]; then
  if uninstall; then
    echo "Uninstall complete."
  else
    echo "Some components may require manual removal."
  fi
  exit 0
fi


# Ensure the installation directories exist
mkdir -p "$APP_DIR"
mkdir -p "$ICON_DIR"
mkdir -p "$DESKTOP_DIR"

# Copy the .py files
cp hangman.py "$APP_DIR/hangman-cli" || handle_error
cp ascii_art.py "$APP_DIR" || handle_error
cp lexicon.py "$APP_DIR" || handle_error

# Copy the icon file
cp hangman-cli.ico "$ICON_DIR" || handle_error

# Make app executable
chmod +x "$APP_DIR/hangman-cli" || handle_error

# Create a desktop file
DESKTOP_FILE="$DESKTOP_DIR/hangman-cli.desktop" || handle_error
echo "[Desktop Entry]" > "$DESKTOP_FILE"
{
  echo "Version=1.2.0"
  echo "Type=Application"
  echo "Name=Hangman-CLI"
  echo "GenericName=Hangman"
  echo "Comment=Hangman, the classic word game"
  echo "Exec=$APP_DIR/hangman-cli"
  echo "Icon=$ICON_DIR/hangman-cli.ico"
  echo "Terminal=true"
  echo "StartupNotify=false"
  echo "Categories=Game;LogicGame;"
  } >> "$DESKTOP_FILE" || handle_error

update_menus || handle_error

echo "Installation complete!"
