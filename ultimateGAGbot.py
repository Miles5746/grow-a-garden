from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key, Listener
import time
import pyautogui
import threading

mouse = MouseController()
keyboard = KeyboardController()

running = False
stop_program = False  


def bot_sequence():
    global running
    while True:
        if running:
      
            mouse.position = (950, 100)
            mouse.click(Button.left, 1)

            pyautogui.keyDown('w')
            time.sleep(1.4)
            pyautogui.keyUp('w')

            pyautogui.keyDown('d')
            time.sleep(0.5)
            pyautogui.keyUp('d')

            for i in range(35):
                keyboard.press('e')
                keyboard.release('e')
                time.sleep(0.1)

            pyautogui.keyDown('d')
            time.sleep(0.45)
            pyautogui.keyUp('d')

            for i in range(35):
                keyboard.press('e')
                keyboard.release('e')
                time.sleep(0.1)

            pyautogui.keyDown('d')
            time.sleep(0.45)
            pyautogui.keyUp('d')

            for i in range(35):
                keyboard.press('e')
                keyboard.release('e')
                time.sleep(0.1)

            mouse.position = (1250, 100)
            mouse.click(Button.left, 1)

            time.sleep(0.5)

            keyboard.press('e')
            keyboard.release('e')

            time.sleep(2)

            mouse.position = (1250, 550)
            mouse.click(Button.left, 1)

            time.sleep(2)
  
        else:
            time.sleep(0.1)  


def on_press(key):
    global running, stop_program
    try:
        if key.char == 'n':
            running = not running
            print(f"{'Started' if running else 'Stopped'} bot.")
        elif key == Key.esc:
            stop_program = True
            print("Exiting bot.")
            return False  
    except AttributeError:
        pass



threading.Thread(target=bot_sequence, daemon=True).start()

print("Press 'n' to toggle the bot, 'Esc' to quit.")
with Listener(on_press=on_press) as listener:
    while not stop_program:
        time.sleep(0.1)
