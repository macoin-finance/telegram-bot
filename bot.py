from dotenv import load_dotenv
from os import getenv
import logging
import datetime
from telegram.ext import Updater, CommandHandler

from commands.contract import contract
from commands.tutorial_metamask import metamask
from commands.tutorial_trustwallet import trust
from commands.price import price
from commands.help import macoin_help
from commands.site import site
from commands.tokenomics import tokenomics
from commands.graph import graph
from commands.video import video
from commands.news import news
from commands.discord import discord
from commands.store import store
from commands.instagram import instagram
from commands.twitter import twitter
from commands.about import about
from commands.buy import buy
from commands.clubhouse import clubhouse
from commands.paper import paper
from commands.parceiros import parceiros
from commands.doe import doe
from commands.hemp import hemp
from commands.medicos import medicos

# get bot api token from .env
load_dotenv('.env')
BOTAPI = getenv('BOTAPITOKEN')

# Set logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# create updater object
updater = Updater(token=BOTAPI, use_context=True)

# set dispatcher locally for quick access
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o bot da MaCoin. Use o comando /help para exibir os comandos disponíveis.")


# set command handler
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', macoin_help)
contract_handler = CommandHandler('contract', contract)
price_handler = CommandHandler('price', price)

tut_metamask_handler = CommandHandler('metamask', metamask)
tut_trust_handler = CommandHandler('trust', trust)
site_macoin_handler = CommandHandler('site', site)
tokenomics_macoin_handler = CommandHandler('tokenomics', tokenomics)
graph_macoin_handler = CommandHandler('graph', graph)
video_macoin_handler = CommandHandler('video', video)
news_macoin_handler = CommandHandler('news', news)
discord_macoin_handler = CommandHandler('discord', discord)
store_macoin_handler = CommandHandler('store', store)
instagram_macoin_handler = CommandHandler('instagram', instagram)
twitter_macoin_handler = CommandHandler('twitter', twitter)
about_macoin_handler = CommandHandler('about', about)
buy_macoin_handler = CommandHandler('buy', buy)
clubhouse_macoin_handler = CommandHandler('clubhouse', clubhouse)
paper_macoin_handler = CommandHandler('paper', paper)
parceiros_macoin_handler = CommandHandler('parceiros', parceiros)
doe_macoin_handler = CommandHandler('doe', doe)
hemp_macoin_handler = CommandHandler('hemp', hemp)
medicos_macoin_handler = CommandHandler('medicos', medicos)

# add handlers to dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(contract_handler)
dispatcher.add_handler(tut_metamask_handler)
dispatcher.add_handler(tut_trust_handler)
dispatcher.add_handler(price_handler)
dispatcher.add_handler(site_macoin_handler)
dispatcher.add_handler(tokenomics_macoin_handler)
dispatcher.add_handler(graph_macoin_handler)
dispatcher.add_handler(video_macoin_handler)
dispatcher.add_handler(news_macoin_handler)
dispatcher.add_handler(discord_macoin_handler)
dispatcher.add_handler(store_macoin_handler)
dispatcher.add_handler(instagram_macoin_handler)
dispatcher.add_handler(twitter_macoin_handler)
dispatcher.add_handler(about_macoin_handler)
dispatcher.add_handler(buy_macoin_handler)
dispatcher.add_handler(clubhouse_macoin_handler)
dispatcher.add_handler(paper_macoin_handler)
dispatcher.add_handler(parceiros_macoin_handler)
dispatcher.add_handler(doe_macoin_handler)
dispatcher.add_handler(hemp_macoin_handler)
dispatcher.add_handler(medicos_macoin_handler)

# start bot
updater.start_polling()
