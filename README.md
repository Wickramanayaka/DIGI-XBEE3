# DIGI-XBEE3
Micropython Libraries for DIGI-XBEE3

## How to use bmp180

1. Copy the bmp180.py into /flash/lib/ of XBEE3 file system.
2. Run REPL
3. Put REPL in to paste mode by clicking CRTL+E
4. Copy and paste the below code into REPL

```python
from bmp import BMP180
from machine import I2C, Pin
bus = I2C(1, freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325
temp = bmp180.temperature
p = bmp180.pressure
print("Values : ", temp, p)
```
5. Press CTRL+D to exit from paste mode and run the code.

## How to use hc-sr-04

1. Copy the hcrs04.py into /flash/lib/ of XBEE3 file system.
2. Run REPL
3. Put REPL in to paste mode by clicking CRTL+E
4. Copy and paste the below code into REPL

```python
fimport hcsr04
from machine import Pin
p = hcsr04.HCSR04(Pin.board.D0,Pin.board.D1)
p.distance_mm()
```
5. Press CTRL+D to exit from paste mode and run the code.
