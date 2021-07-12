import requests
import time

from datetime import datetime



try:
    MACOIN = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()["data"]
    TIMESTAMP = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()['updated_at']
    HUMANTIME = datetime.fromtimestamp(int(TIMESTAMP/1000))
    USDBRL = requests.get('https://economia.awesomeapi.com.br/all/USD').json()['USD']['high']
    MACOINUSD = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()["data"]['price']


    valuebrl = float(USDBRL)
    valueusd = float(MACOINUSD)
    macoinbrlresult = (valuebrl * valueusd)
    MACOINBRL = (round(macoinbrlresult, 20))

    MESSAGE_TEXT = f"**MaCoin price USD:** ${MACOIN['price']}\n**MaCoin price BNB:** ${MACOIN['price_BNB']}\n**MaCoin price BRL:** R${MACOINBRL}\n\nPreço atualizado em: {HUMANTIME}"

    def price(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')

except requests.exceptions.RequestException as e:
     try:

         USDBRL = requests.get('https://economia.awesomeapi.com.br/all/USD').json()['USD']['high']
         MACOINUSD = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BUSD&sellAmount=1').json()
         MACOINBUSD = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BUSD&sellAmount=1').json()
         MACOINBNB = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BNB&sellAmount=1').json()
 
         valuebrl = float(USDBRL)
         valueusd = float(MACOINBUSD)
         macoinbrlresult = (valuebrl * valueusd)
         MACOINBRL = (round(macoinbrlresult, 20))
 
         MESSAGE_TEXT0x = f"**MaCoin price USD:** ${MACOINUSD['price']}\n**MaCoin price BNB:** ${MACOINBNB['price']}\n**MaCoin price BRL:** R${MACOINBRL}"
 
         def price(update, context):
             context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT0x, parse_mode='markdown')
 
     except requests.exceptions.RequestException as e:
 
             MESSAGE_TEXTOFF = f"**API da Pancakeswap.info e bsc.api.0x.org fora do ar. Tente novamente em alguns minutos."
 
             def price(update, context):
                 context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXTOFF, parse_mode='markdown')
