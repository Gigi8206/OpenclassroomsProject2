
from bs4 import BeautifulSoup
import constants
from pathlib import Path
import requests
import re
import os
from tqdm import tqdm

from phase1 import phase1
from phase2 import phase2
from phase3 import phase3

def get_selection():
    selection = input(
        "Please choose the phase you want to get images with:\n"
        "1: Phase 1\n"
        "2: Phase 2\n"
        "3: Phase 3\n"
        "Your choice ? "
    )
    return selection

def main():
    invalid_selection = "Invalid selection, please retry and enter a number between 1 and 3"

    selection = 0
    while type(selection) != int or selection < 1 or selection > 3:
        selection = get_selection()
        try:
            selection = int(selection)
        except ValueError:
            print(invalid_selection)

        if type(selection) == int and (selection < 1 or selection > 3):
            print(invalid_selection)

    if selection == 1:
        phase1(upload_images=True)
    elif selection == 2:
        phase2(upload_images=True)
    else:
        phase3(upload_images=True)

if __name__ == '__main__':
    main()



