import pyautogui
import time
from pynput.mouse import Listener

import subprocess
from reload_click import reload_click, run_at_time


points = []
timeReload = [15, 50]
num_point = int(input("Количество точек: "))  

def run_secundomer():
    path = r"D:\project\afk\Secundomer.py"
    subprocess.Popen(["python", path])

def on_click(x, y, button, pressed):
    if pressed:
        points.append((x, y))  
        print("Clicked at:", (x, y))
        if len(points) == num_point:
            run_secundomer()
            if __name__ == "__main__":
                run_at_time(timeReload[0], timeReload[1], reload_click)

            return False


with Listener(on_click=on_click) as listener:
    listener.join()

try:
    while True:
        time.sleep(30)
        for coord in points:
            pyautogui.moveTo(coord[0], coord[1], 1)
            pyautogui.click()
            if pyautogui.press('space'):
                reload_click()
            time.sleep(10)  
except KeyboardInterrupt:
    pyautogui.FAILSAFE = True
    print("Программа завершена")

