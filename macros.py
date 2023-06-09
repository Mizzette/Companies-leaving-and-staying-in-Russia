import pyautogui
import time

# copying name
x, y = pyautogui.position()
time.sleep(3)

for i in range(2000):
    # Moving to db
    pyautogui.moveTo(149, 24)
    pyautogui.click()

    # Copying item
    pyautogui.typewrite(['down'])
    pyautogui.hotkey('command', 'c', interval=0.1)
    # Moving to СПАРК
    pyautogui.moveTo(406, 31)
    pyautogui.click()

    if i % 4 == 0:
        pyautogui.moveTo(85, 62)
        pyautogui.click()
        time.sleep(1)

    # Deleting the search bar
    pyautogui.moveTo(489, 467)
    pyautogui.click()
    pyautogui.hotkey('command', 'a', interval=0.1)
    pyautogui.typewrite(['Backspace'])

    # Finding INN and copying it
    pyautogui.hotkey('command', 'v', interval=0.1)
    pyautogui.moveTo(1213, 469)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(349, 821)
    pyautogui.rightClick()
    pyautogui.click()
    pyautogui.hotkey('command', 'c', interval=0.1)

    # Moving to db
    pyautogui.moveTo(149, 24)
    pyautogui.click()

    # Pasting item
    pyautogui.typewrite(['right'])
    pyautogui.hotkey('command', 'v', interval=0.1)
    pyautogui.typewrite(['left'])
