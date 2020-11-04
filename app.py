from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

start_counter = 9886 #set your start counter
end_counter = 10017 #set your end counter

break_counter = start_counter + 100
counter = start_counter

sleep(3) # so you can select your were you wanne tipe

while end_counter >= counter:
    keyboard.type(f'{counter}')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    if counter == break_counter:
        break_counter += 100
        sleep(5)
    sleep(1)
    counter += 1