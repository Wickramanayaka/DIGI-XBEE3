from machine import Pin 
import time
p = Pin(Pin.board.D0, Pin.IN)
while True:
  p.value()
  time.sleep_ms(500)
