import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def depozit(self):
        for i in range(100):
            value = randint(50, 100)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            value = randint(50, 100)
            print(f'Запрос на {value}')
            if value <= self.balance:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.depozit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
