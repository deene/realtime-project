from Pubnub import Pubnub
import time
import serial
import threading

systemStatus = "idle"
ser = serial.Serial('COM1', 9600)

pubnub = Pubnub(publish_key="pub-c-6a3d5bbe-652b-49a2-bca1-ccb6db8bb50d", subscribe_key="sub-c-5fa82184-f7ba-11e4-8fd2-02ee2ddab7fe")

def _callback(message, channel):
    if message["sender"] == "browser":
        print(message['setSystemStatus'])
        systemStatus = message["setSystemStatus"]
        #time.sleep(2)
        out_message = {"sender": "bric", "body": "status update"}
        pubnub.publish("demo_tutorial", out_message, callback=callback, error=callback)

def _error(message):
    print("error")

pubnub.subscribe(channels="demo_tutorial", callback=_callback, error=_error)

def callback(message):
    print(message)

while True:
    print "status: " + systemStatus
    for thread in threading.enumerate():
        print thread

    if systemStatus == "idle":
        time.sleep(1)
    elif systemStatus == "debug":
        serialMessage = ser.readline()
        if serialMessage:
                pubnub.publish("demo_tutorial", serialMessage, callback=callback(serialMessage), error=callback(serialMessage))
    elif systemStatus == "reconfiguration":
        print("Programming Arduino...done")
        out_message = {"sender": "bric", "body": "Programming Arduino Done."}
        pubnub.publish("demo_tutorial", out_message, callback=callback(out_message), error=callback(out_message))
        systemStatus = "idle"
