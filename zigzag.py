# Loc - FunProgramming

# Zigzag, by Al Sweigart
# Shows a simple zig zag animation

# Ctrl-C to stop the program
import time

# constants
constants = {
    "DELAY": 0.05,  # Pause for 50 milliseconds
    "INDENT_CHARACTER": " ",
    "SPECIAL_CHARACTER": "********",
}
    
# Zig to the right 20 times:
def zig(indentSize):
    for i in range(20):
        indentSize += 1
        indentation = constants["INDENT_CHARACTER"] * indentSize
        print(indentation + constants["SPECIAL_CHARACTER"])
        time.sleep(constants["DELAY"])
    return indentSize

# Zag to the left 20 times:
def zag(indentSize):
    for i in range(20):
        indentSize -= 1
        indentation = constants["INDENT_CHARACTER"] * indentSize
        print(indentation + constants["SPECIAL_CHARACTER"])
        time.sleep(constants["DELAY"])

def main():
    # How many spaces to indent
    indentSize = 0
    # main loop
    while True:
        nextIndext = zig(indentSize)
        zag(nextIndext)

if __name__ == '__main__':
    main()