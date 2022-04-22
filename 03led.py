from flask import Flask
import RPi.GPIO as GPIO
import time

button = 10
led    = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to IOT"

@app.route("/start")
def start():
    GPIO.output(led, True)
    return "Light Start"

@app.route("/stop")
def stop():
    GPIO.output(led, False)
    return "Light Stop"

if __name__ == '__main__':
    app.run()