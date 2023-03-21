from fbchat import Client
from fbchat.models import *

username = "fb username"
password = "password"



thread_id = "100012322592565"
thread_type = ThreadType.USER

# class KeepTyping(Client):
#     def onMessageDelivered(self, msg_ids=None, delivered_for=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
#         self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)

client = Client(username, password)
client.setTypingStatus(status = TypingStatus.TYPING, thread_id = thread_id, thread_type = thread_type)
client.listen()
