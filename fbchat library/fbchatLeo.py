from fbchat import Client
from fbchat.models import *
username = "username"
password = "password"

def msg_fn():
    msg = "What's up ningen!"
    for i in range(1000):
        msg += "What's up ningen!"
    return msg


my_msg = msg_fn()

client = Client(username, password)
client.send(Message(text = my_msg), thread_id='2651262271654809', thread_type=ThreadType.GROUP)
