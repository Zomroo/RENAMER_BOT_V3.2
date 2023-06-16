import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5752952621:AAGO61IiffzN23YuXyv71fbDztA_ubGM6qo")

API_ID = int(os.environ.get("API_ID", "14091414"))

API_HASH = os.environ.get("API_HASH", "1e26ebacf23466ed6144d29496aa5d5b")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
