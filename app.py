# import files
from chatterbot.response_selection import get_first_response
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

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


@app.route('/api', methods=['GET'])
def get_bot_response():
    userText = str(request.args['query'])
    x = str(chatbot.get_response(userText))
    return jsonify(x)


if __name__ == "__main__":
    app.run()
