# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('test')

conv = ['oi','ola','ola, bom dia', 'bom dia', 'bom dia, como vai?', 'estou bem']
convY = ['yara mila', 'fertilizante', 'quais fertilizantes']

bot.set_trainer(ListTrainer)

bot.train(conv)
bot.train(convY)

while True:
    quest = input('Você: ')

    response = bot.get_response(quest)

    print('Bot: ', response)