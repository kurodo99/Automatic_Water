import RPi.GPIO as GPIO


class Relay:
    ACTIVATE = 1
    DEACTIVATE = 0

    def __init__(self, name, gpio, status, time):

        self.name = name
        self.time = time
        self.status = status
        self.gpio = gpio
        GPIO.setmode(GPIO.BCM)

        if gpio is not None:
            GPIO.setup(gpio, GPIO.OUT)

    def turn_on(self):
        if self.gpio is None:
            print("Error can't not found GPIO")
        else:
            GPIO.output(self.gpio, GPIO.HIGH)

    def turn_off(self):
        if self.gpio is None:
            print("Error can't not found GPIO")
        else:
            GPIO.output(self.gpio, GPIO.LOW)

    def get_state(self):
        return GPIO.input(self.gpio)

    def clear_relay(self):
        self.turn_off()
        GPIO.cleanup()
