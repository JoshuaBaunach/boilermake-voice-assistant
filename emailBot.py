from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def get_response(userText, input_adapter='chatterbot.input.VariableInputTypeAdapter'):
    bot = ChatBot('Bot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.70,
                    'default_response': 'I am sorry, but I do not understand.'
                }
                ],
                input_adapter=input_adapter,
                trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    if userText.strip().lower() != 'bye':
        result = bot.get_response(userText)                        
        reply = str(result)
        return(reply)
    else:
        return('Bye')
