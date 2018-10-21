from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer 
import os 

bot = ChatBot('Bot',
        storage_adapter = "chatterbot.storage.SQLStorageAdapter"        
        )

bot.set_trainer(ListTrainer)





for files in os.listdir('./trainingData/'):
    data = open('./trainingData/' + files, 'r').readlines()
    bot.train(data)


my_storage = {}



while True:
    for x in range(5):
        message = input('You:')
        if message.strip() != 'Bye':
        
            reply = bot.get_response(message)
            print('ChatBot: ',reply)
            key = input(message)
            value =input(reply)
            my_storage[key]=value

        if message.strip() == 'Bye':
            print('ChatBot: Bye!')
            break



for key in my_storage:
    print(key, my_storage[key]) 

