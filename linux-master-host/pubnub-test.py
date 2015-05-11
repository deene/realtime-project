from Pubnub import Pubnub
import time

pubnub = Pubnub(publish_key="pub-c-6a3d5bbe-652b-49a2-bca1-ccb6db8bb50d", subscribe_key="sub-c-5fa82184-f7ba-11e4-8fd2-02ee2ddab7fe")
def _callback(message, channel):
    if message["sender"] == "browser":
        print(message['body'])
        #time.sleep(2)
        out_message = {"sender": "bric", "body": "status update"}
        pubnub.publish("demo_tutorial", out_message, callback=callback, error=callback)

def _error(message):
    print(message)

pubnub.subscribe(channels="demo_tutorial", callback=_callback, error=_error)

def callback(message):
    print("published:")
    print(message)

#pubnub.publish(channel, message, callback=callback, error=callback)
