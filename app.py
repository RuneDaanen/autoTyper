from time import sleep
from pynput.keyboard import Key, Controller
keyboard = Controller()

startCounter = 9886
endCounter = 10017

breakCounter = startCounter + 100

counter = startCounter

sleep(3)

while endCounter >= counter:
    keyboard.type(f'{counter}')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    if counter == breakCounter:
        breakCounter += 100
        sleep(5)
    sleep(1)
    counter += 1