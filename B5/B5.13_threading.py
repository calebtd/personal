from finch import Finch
import time
import threading

finchy = Finch()


def flash():
    while True:
        finchy.led(255, 0, 0)
        time.sleep(.75)
        finchy.led(0, 0, 255)
        time.sleep(.75)


def chase():
    x = 587
    while x < 880:
        finchy.buzzer_with_delay(.04, x)
        x += 15
    while x > 587:
        finchy.buzzer_with_delay(.04, x)
        x -= 15


def parade():
    finchy.buzzer_with_delay(.45, 784)
    finchy.buzzer_with_delay(.45, 622)


def siren():
    while True:
        for i in range(4):
            parade()
        for i in range(2):
            chase()


# ----

threading.Thread(target=flash).start()
threading.Thread(target=siren).start()
