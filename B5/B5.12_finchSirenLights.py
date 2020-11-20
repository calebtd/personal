from finch import Finch
import time

finchy = Finch()



def flash():
    finchy.led(255,0,0)
    time.sleep(.75)
    finchy.led(0,0,255)
    time.sleep(.75)


def chase():
    x = 587
    while x < 880:
        finchy.buzzer_with_delay(.019, x)
        x += 6
    while x > 587:
        finchy.buzzer_with_delay(.019, x)
        x -= 6


def parade():
    finchy.buzzer_with_delay(.45, 784)
    finchy.buzzer_with_delay(.45, 622)



while True:
    for i in range(5):
        parade()
    for i in range(2):
        chase()