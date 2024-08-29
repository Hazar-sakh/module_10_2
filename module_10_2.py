from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        counter = 0
        rang = int(enemies / self.power)
        for i in range(0, rang):
            if enemies > 0:
                enemies -= self.power
                time.sleep(1)
                counter += 1
                print(f'{self.name} сражается {counter} день..., осталось {enemies} воинов')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')


Threads = []
first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
Threads.append(first_knight)
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
Threads.append(second_knight)
