# -*- coding: UTF-8 -*-

from fbchat import log, Client

username = "fb username"
password = "fb password"
# Subclass fbchat.Client and override required methods

def memefy(sentence):
        #Splitting the sentence into words    
        words = sentence.split()    
        new_words = []
        
        for word in words:
            
            each_word_letter_list = []
            for letter in word:
                each_word_letter_list.append(letter)
            
            
            each_word_replaced_letters = []
            for letter in each_word_letter_list:            
                if letter != 'a' and letter != 's' and letter != 'h' and letter != 'o':
                    letter = letter
                elif letter == 'a':
                    letter = '@'
                elif letter == 's':
                    letter = '$'
                elif letter == 'h':
                    letter = '#'
                elif letter == 'o':
                    letter = '0'
                each_word_replaced_letters.append(letter)
                
            new_word = "".join(each_word_replaced_letters)
            new_words.append(new_word)
        
        try:
            #Capitalizing the 4th word of the sentence
            new_words[3] = new_words[3].upper()
            
            #Memefying the sixth word of the sentence
            sixth_word_letters = [i for i in new_words[5]]
            index = 0
            mem_sixth= []
            
            while index < len(sixth_word_letters):
                if index % 2 == 0:
                    mem_sixth.append(sixth_word_letters[index])
                else:
                    mem_sixth.append(sixth_word_letters[index].upper())
                index += 1
            sixth_word = "".join(mem_sixth)
            new_words[5] = sixth_word
            
        except:
            pass
            
        memefied = " ".join(new_words)
        return memefied

class EchoBot(Client):   
                
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)


client = EchoBot(username, password)
client.listen()
