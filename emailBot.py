from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 


bot = ChatBot('EmailBot')
bot.set_trainer(ListTrainer)


def get_response(userText):
    bot = ChatBot('Bot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        {
            'import_path': 'chatterbot.logic.BestMatch'
            },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sory, but I dont not understand.'
            }
        ],
    trainer ='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)

    while True:

        if userText.strip() != 'Bye':
            result = bot.get_response(userText)
            reply = bot.get_response(message)
            return(reply)
        if userText.strip() == 'Bye':
            return('Bye')
            break
