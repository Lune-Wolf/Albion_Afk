import pyautogui
import time
from pynput.mouse import Listener
import subprocess

points = []
timeReload = [15, 50]
num_point = int(input("Количество точек: "))  

def run_secundomer():
    path = r"G:\project\afk\Secundomer.py"
    subprocess.Popen(["python", path])

def on_click(x, y, button, pressed):
    if pressed:
        points.append((x, y))
        print("Координата клика:", (x, y))
        if len(points) == num_point:
            run_secundomer()
            return False

pyautogui.FAILSAFE = True  # Инициализация fail-safe

try:
    with Listener(on_click=on_click) as listener:
        listener.join()
except Exception as e:
    print(f"Ошибка: {e}")

try:
    while True:
        time.sleep(30)
        for coord in points:
            pyautogui.moveTo(coord[0], coord[1], 1)
            pyautogui.click()
            time.sleep(10)  
except KeyboardInterrupt:
    print("Программа завершена")
