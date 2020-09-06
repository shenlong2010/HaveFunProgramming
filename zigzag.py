# Loc - FunProgramming

# Zigzag, by Al Sweigart
# Shows a simple zig zag animation

# Ctrl-C to stop the program
import time

# constant
constants = {
    "DELAY": 0.05,  # Pause for 50 milliseconds
    "INDENT_CHARACTER": " ",
    "SPECIAL_CHARACTER": "********",
}

indentSize = 0  # How many spaces to indent

while True:  # main loop
    # Zig to the right 20 times:
    for i in range(20):
        indentSize += 1
        indentation = constants["INDENT_CHARACTER"] * indentSize
        print(indentation + constants["SPECIAL_CHARACTER"])
        time.sleep(constants["DELAY"])

    # Zag to the left 20 times:
    for i in range(20):
        indentSize -= 1
        indentation = constants["INDENT_CHARACTER"] * indentSize
        print(indentation + constants["SPECIAL_CHARACTER"])
        time.sleep(constants["DELAY"])
