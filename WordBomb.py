#==============FURRO404==============#
#WordBomb.py
import random
import time
import pyautogui
import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageGrab, ImageChops
import time
import os
#-----Misc Python Modules-----#
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#-----------------------------#
def scanScreen():
    image = ImageGrab.grab(bbox=(787,666,832,686))      # GET IMAGE
    image.save('current.png')
    
    image = Image.open('current.png')
    image = image.convert('L')                          # GRAYSCALE THAT SHIT
    image.save('current.png')

    image = Image.open('current.png')
    image = ImageChops.invert(image)                    # INVERT
    image.save('current.png')
    
    image = Image.open('current.png')                        
    enhancer = ImageEnhance.Contrast(image)                  
    factor = 5                                          # CONTRAST THAT SHIT
    image = enhancer.enhance(factor)
    image.save('current.png')

    image = "current.png"
    src = cv2.imread(image, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)         # TRANSPARENT BACKGROUND
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)
    cv2.imwrite("current.png", dst)

    image = cv2.imread('current.png')
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 10 --oem 3')            # EXTRACT TEXT
    text = text.replace("\n", " ")
    text = text.replace(" ", "")                                                                # REMOVE STUPID EXCESS CHARS
    print(text)
    
    letters = []
    letters.append(text[0])
    letters.append(text[2])                             # COLLECT RELEVANT LETTERS
    print(letters)
    
    given = ""
    for letter in letters:
        given += letter                                 # CONJOIN LETTERS INTO STRING
    
    given = given.lower()
    print("Using:", given)                              # FINISH THIS GODAWFUL MESS OF A FUNCTION AND RETURN TWO FUCKING LETTERS
    getWord(given)


def getWord(given):
    acceptable_words = []

    with open('words.txt') as word_list_file:
        words = word_list_file.read()                               # Turn all words from wordfile into a list
        words_list = words.split("\n")

        print(f"\n\nSearching for words with: '{given}'")
        for word in words_list:
            if given in word:                                       # Return words we want into another list
                acceptable_words.append(word)

        print(f'{len(acceptable_words)} words\n')
        
        if len(acceptable_words) > 1:
            for i in range (0, 20):                                 # Give user 10 options
                word = random.choice(acceptable_words)
                print(word)

            word = random.choice(acceptable_words)                  # Choose one option automatically
            print("\n\nI chose", word)
            
            time.sleep(2)
            for letter in word:
                pyautogui.press(letter)                             # Wait 2 sec before typing word out
            
        else:
            print(f"\n\nNo words with: '{given}'")
#-----------------------------#
while True:
    wait = input("Press enter to scan screen")
    scanScreen()
#==============FURRO404==============#
