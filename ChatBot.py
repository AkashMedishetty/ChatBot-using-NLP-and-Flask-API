
#install packages
# pip install "chatterbot==1.0.0"
# pip install pytz
#      OR
# pip install -r requirements.txt

# import required packages
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.response_selection import get_first_response

# create ChatBot
chatbot = ChatBot("ERMIN",
                  storage_adapters = 'chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter',
                      'chatterbot.logic.BestMatch',
                      {"import_path": "chatterbot.logic.BestMatch",
                       'default_response': 'I am sorry, but I do not understand. I am still learning.',
            "statement_comparison_function": 'chatterbot.comparisons.LevenshteinDistance',
            'response_selection_method': get_first_response
                          }
                      ],
                        database_uri = 'sqlite:///database.sqlite3')

# create ChatBot trainer
training_data_simple = open('./training.txt').read().splitlines()
training_data_personal = open('./jarvis.txt').read().splitlines()

training_data = training_data_simple + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Greeting from chat bot
print("Hi, I am ChatBot")

# keep communicating with ChatBot
while True:
    # take user input/query
    query = input(">>>")
    # response from ChatBot
    # put query on Statement format to avoid runtime alert messages
    # Statement(text=query, search_text=query)
    print(chatbot.get_response(Statement(text=query, search_text=query)))
