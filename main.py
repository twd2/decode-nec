import nec
import time
import RPi.GPIO as GPIO

IR = 23
TIMEOUT = 30 # ms

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)

timing = []

GPIO.wait_for_edge(IR, GPIO.BOTH, timeout=30000)
start_time = time.time()
while True:
    GPIO.wait_for_edge(IR, GPIO.BOTH, timeout=TIMEOUT)
    current_time = time.time()
    el = (current_time - start_time) * 1000000
    if el < TIMEOUT * 1000:
        timing.append(el)
    else:
        break
    start_time = current_time

print('begin')
for t in timing:
    print(t)
print('end')
print(len(timing))

bits_str = nec.decode(timing)
print((bits_str, len(bits_str)))