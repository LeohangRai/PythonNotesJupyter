# -*- coding: UTF-8 -*-

from fbchat import log, Client
from fbchat.models import *

username = "fb username"
password = "password"

# Change this to your group id
old_thread_id = "1761910477266427"

# Change these to match your liking
old_color = ThreadColor.MESSENGER_BLUE
old_emoji = "👍"
old_title = "This group belongs to me now! Hihi hahaha"
old_nicknames = {
    "100003725769977": "The Lord Leohang",
    "100007701307870": "Sandip Thapa",
    "100006459560975": "Abhishek Magar",
    "100012322592565": "Bandariya",
}


class KeepBot(Client):
    def onColorChange(self, author_id, new_color, thread_id, thread_type, **kwargs):
        if old_thread_id == thread_id and old_color != new_color:
            log.info(
                "{} changed the thread color. It will be changed back".format(author_id)
            )
            self.send(Message(text = "You tried to change the theme color, but it won't work! khikhikhi"), thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.changeThreadColor(old_color, thread_id=thread_id)

    def onEmojiChange(self, author_id, new_emoji, thread_id, thread_type, **kwargs):
        if old_thread_id == thread_id and new_emoji != old_emoji:
            log.info(
                "{} changed the thread emoji. It will be changed back".format(author_id)
            )
            self.send(Message(text = "You tried to change the Emoji, but it won't work! khikhikhi"), thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.changeThreadEmoji(old_emoji, thread_id=thread_id)

    def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
        if old_thread_id == thread_id and author_id != self.uid:
            log.info("{} got added. They will be removed".format(added_ids))
            self.send(Message(text = "You tried to add people, but it won't work! khikhikhi"), thread_id=thread_id, thread_type=ThreadType.GROUP)
            for added_id in added_ids:
                self.removeUserFromGroup(added_id, thread_id=thread_id)

    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        # No point in trying to add ourself
        if (
            old_thread_id == thread_id
            and removed_id != self.uid
            and author_id != self.uid
        ):
            log.info("{} got removed. They will be re-added".format(removed_id))
            self.send(Message(text = "You tried to remove someone, but it won't work! khikhikhi"), thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.addUsersToGroup(removed_id, thread_id=thread_id)

    def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kwargs):
        if old_thread_id == thread_id and old_title != new_title:
            log.info(
                "{} changed the thread title. It will be changed back".format(author_id)
            )
            self.send(Message(text = "You tried to change the title, but it won't work! khikhikhi"), thread_id=thread_id, thread_type=ThreadType.GROUP)

            self.changeThreadTitle(
                old_title, thread_id=thread_id, thread_type=thread_type
            )

    def onNicknameChange(
        self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs
    ):
        if (
            old_thread_id == thread_id
            and changed_for in old_nicknames
            and old_nicknames[changed_for] != new_nickname
        ):
            log.info(
                "{} changed {}'s' nickname. It will be changed back".format(
                    author_id, changed_for
                )
            )
            self.changeNickname(
                old_nicknames[changed_for],
                changed_for,
                thread_id=thread_id,
                thread_type=thread_type,
            )


client = KeepBot(username, password)
client.listen()
