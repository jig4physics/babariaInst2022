import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

button = 10
led    = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

# client of MQTT
client = mqtt.Client("Jignesh")

 # on connect
def on_connect(clinet,userdata,flag, rc):
    print("Connected with result code" +str(rc))

# Suscribe topic 
def on_message(client, userdata,msg):
    print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))
    command = str(msg.payload.decode("utf-8"))
    print(command)
    if command == "START":
        GPIO.output(led, True)
    else:
        GPIO.output(led, False)

client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883)
client.subscribe("my/led")

client.loop_start()


