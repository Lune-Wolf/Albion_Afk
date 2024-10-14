import time
import os

def clear_console():
    # Очистка консоли для Windows
    os.system('cls')

def stopwatch():
    start_time = time.time()
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            
            clear_console()
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nСекундомер остановлен.\n")

# Запуск секундомера
stopwatch()
