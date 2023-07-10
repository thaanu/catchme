# Developed by Shan (@thaanu16)

# Imports go at the top
from microbit import *
import music
import random

ledSeq = '00000:00000:00000:00000:00000'

# This method generates a led sequence by setting the lum of the led
def mngLed(sequence, led, lum):
    o = ''
    for i in range(1,30):
        if i == led and sequence[i-1] != ':':
            o += lum
        else:
            o += sequence[i-1]
    return o

# This method turns a led on
def ledOn( led, lum ):
    global ledSeq
    ledSeq = mngLed(ledSeq, led, lum)
    display.show(Image(ledSeq))

# This method turns a led off
def ledOff( led ):
    global ledSeq
    ledSeq = mngLed(ledSeq, led, "0")
    display.show(Image(ledSeq))

# This method turns the sequence leds on
def lightOn( xyz ):
    display.show(Image(xyz))


newGame = True
gameResetCount = 0
matchSequence = ""
speed = 100
start = 25
numOfRetries = 5

# Code in a 'while True:' loop repeats forever   
while True:

    # Set a new game if new game flag is on
    if newGame :
        music.play(music.JUMP_UP)
        display.scroll("New Game", delay=80)
        nLed = random.randint(1,30)
        matchSequence = mngLed(ledSeq, nLed, "9")
        print(matchSequence)
        start = nLed
        
        display.scroll("Ready", delay=50)
        lightOn(matchSequence)
        sleep(5000)
        display.show(1)
        sleep(1000)
        display.show(2)
        sleep(1000)
        display.show(3)
        sleep(1000)
        display.show("GO")

    # Set new game flag to false, so the game continues
    newGame = False
    
    # Looping all the 5 leds in a row
    for i in range(start, start + 5):
        ledOn( i, "9")

        # Start a new game
        if button_b.is_pressed():
            newGame = True

        # Handle button event
        if button_a.is_pressed():
            if ledSeq == matchSequence:
                newGame = True
                music.play(music.POWER_UP)
            else:
                music.play(music.POWER_DOWN)
                # Increment the reset game count if missed
                gameResetCount = gameResetCount + 1
                
        sleep(speed)
        ledOff(i)

    # Increment the reset game count if missed
    gameResetCount = gameResetCount + 1

    # Reset the game, if reset game count is greater or equal to 5 and new game flag is false
    if gameResetCount >= numOfRetries and newGame == False:
        newGame = True
        music.play(music.JUMP_DOWN)
        display.scroll("Game Over", delay=80)

    # Reset all the game to get a new game
    if newGame:
        gameResetCount = 0
        matchSequence = mngLed(ledSeq, 27, "9")
    





        
        
    
