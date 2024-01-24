import RPi.GPIO as GPIO
import time

servo_pin = 18
frequency = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, frequency)

def rotate_servo(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)

pwm.start(0)

def door_automate(val):
    if val == 0:
        rotate_servo(90)
    elif val == 1:
        rotate_servo(0)

door_automate(0)
door_automate(1)

pwm.stop()
GPIO.cleanup()
