import machine
import time
from machine import Pin
class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        # Init echo pin (in)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0)
        time.sleep_us(5)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = self._time_pulse(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex

    def _time_pulse(self, pin, pulse_level, timeout_us):
        nchanges = 2
        start = time.ticks_us()
        while True:
            dt = time.ticks_us() - start
            if(pin.value() == pulse_level):
                nchanges = nchanges - 1
                if(nchanges == 0):
                    return dt
                pulse_level = 1 - pulse_level
                start = time.ticks_us()
                continue
            if(dt >= timeout_us):
                return -nchanges

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms