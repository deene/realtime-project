from Pubnub import Pubnub
import time
import serial
import threading
import subprocess

systemStatus = "idle"
signal = threading.Event()
signal.clear()

ser = serial.Serial('COM1', 9600)

pubnub = Pubnub(publish_key="pub-c-6a3d5bbe-652b-49a2-bca1-ccb6db8bb50d", subscribe_key="sub-c-5fa82184-f7ba-11e4-8fd2-02ee2ddab7fe")

def _callback(message, channel):
    if message["sender"] == "browser":
        print(message['setSystemStatus'])
        signal.set()
        #time.sleep(2)
        out_message = {"sender": "bric", "body": "status update"}
        pubnub.publish("demo_tutorial", out_message, callback=callback, error=callback)

def _error(message):
    print("error")

pubnub.subscribe(channels="demo_tutorial", callback=_callback, error=_error)

def callback(message):
    print("callback place holder")

while True:
    if not signal.is_set():
        time.sleep(1)
    elif signal.is_set():
        print "status configuration"
        time.sleep(2)
        output = subprocess.check_output('ipconfig')
        print("Programming Arduino...done")
        out_message = {"sender": "bric", "body": output}
        pubnub.publish("demo_tutorial", out_message, callback=callback(out_message), error=callback(out_message))
        print "entering idle..."
        signal.clear()
