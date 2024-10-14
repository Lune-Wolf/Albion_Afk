import time

num_time = int(input("Время для Таймера: "))

def countdown_timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        time_left = end_time - time.time()
        hours, remainder = divmod(time_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        seconds, milliseconds = divmod(seconds, 1)
        print(f"Осталось времени: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}", end='\r')
        time.sleep(1)  # Обновление каждые 10 миллисекунд

    print("Время вышло!")

# Установите время в секундах для таймера
countdown_timer(num_time)  # Пример: 60 секунд
