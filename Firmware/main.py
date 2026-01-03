# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D26, board.D28, board.D27, board.D4, board.D2, board.D3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

PASTE = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
)

COPY = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

SAVE = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.S),
    Release(KC.LCTL)
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.ESCAPE, SAVE, KC.BSPACE, COPY, PASTE, KC.ENTER,]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()

# I Dont Know What I'm Going To Display On The Oled Screen , Cause I Got Too Many idea , but i'm gonna give it life when i'll get the parts .