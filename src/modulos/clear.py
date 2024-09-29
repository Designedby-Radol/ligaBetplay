import os
def clearScreen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux and macOS
        clearScreen()