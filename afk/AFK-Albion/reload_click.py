import threading
import pyautogui
import time

points = [(687, 428), (686, 582), (862, 664)]

def reload_click():
    for coord in points:
            pyautogui.moveTo(coord[0], coord[1], 1)
            pyautogui.click()
            time.sleep(2)
    print("Перезагрузка в", time.strftime("%H:%M:%S"))

def run_at_time(hour, minute, function):
    now = time.localtime()
    run_time = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, hour, minute, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    
    delay = run_time - time.time()
    
    if delay < 0:
        run_time += 86400  # Если указанное время уже прошло, добавляем день
    
    print("Запуск функции в", time.strftime("%H:%M:%S", time.localtime(run_time)))
    
    timer = threading.Timer(delay, function)
    timer.start()

