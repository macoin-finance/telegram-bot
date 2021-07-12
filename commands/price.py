import requests
import time

from datetime import datetime



try:

    pancakeswap = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()
    macoin = pancakeswap.get('data')
    timestamp = pancakeswap.get('updated_at')
    humantime = datetime.fromtimestamp(int(timestamp/1000))
    usd_brl = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL').json()['price']
    macoin_usd = pancakeswap.get('data', {}).get('price')
    macoin_bnb = pancakeswap.get('data', {}).get('price_BNB')

    valuebrl = float(usd_brl)
    valueusd = float(macoin_usd)
    macoinbrlresult = (valuebrl * valueusd)
    macoin_brl = (round(macoinbrlresult, 20))

    MESSAGE_TEXT = f"**MaCoin price USD:** ${macoin_usd}\n**MaCoin price BNB:** ${macoin_bnb}\n**MaCoin price BRL:** R${macoin_brl}\n\nPreço atualizado em: {humantime}"
    def price(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')

except requests.exceptions.RequestException as e:
    try:
        org = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BUSD&sellAmount=1').json()
        orgbnb = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BNB&sellAmount=1').json()
        macoin_usd = org.get('price')
        macoin_bnb = orgbnb.get('price')
        usd_brl = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL').json()['price']

        valuebrl = float(usd_brl)
        valueusd = float(macoin_usd)
        macoinbrlresult = (valuebrl * valueusd)
        macoin_brl = (round(macoinbrlresult, 20))

        MESSAGE_TEXT0x = f"**MaCoin price USD:** ${macoin_usd}\n**MaCoin price BNB:** ${macoin_bnb}\n**MaCoin price BRL:** R${macoin_brl}"
        def price(update, context):
            context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')

    except requests.exceptions.RequestException as e:
 
             MESSAGE_TEXTOFF = f"**API da Pancakeswap.info e bsc.api.0x.org fora do ar. Tente novamente em alguns minutos."
 
             def price(update, context):
                 context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXTOFF, parse_mode='markdown')
