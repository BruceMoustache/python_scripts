import keyboard
import time

recorded = keyboard.record(until='esc')
time.sleep(5)
keyboard.play(recorded, speed_factor=1)

