import RPi.GPIO as GPIO
import time

from application.ports.inbound.gate_oppener import GateOppener


class RassberryGateOpenner(GateOppener):

    def __init__(self, pin_number, oppeing_time) -> None:
        GPIO.cleanup()
        self.pin_number = pin_number
        self.oppeing_time = oppeing_time
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.OUT)
        
    def __del__(self):
        GPIO.cleanup()

    def open_gate(self) -> None:
        GPIO.output(self.pin_number, GPIO.HIGH)
        time.sleep(self.oppeing_time)
        GPIO.output(self.pin_number, GPIO.LOW)
