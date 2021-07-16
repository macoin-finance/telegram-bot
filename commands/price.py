import requests
from datetime import datetime


def get_api_data(url):

    try:
        response = requests.get(url, timeout=5)
        result = response.json()
        if 'message' in result:
            result = {}
    except requests.exceptions.RequestException:
        result = {}
    except:
        result = {}
    return result

def price(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode='markdown')


usd_brl_api = get_api_data('https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL')
if 'price' not in usd_brl_api:
    message_text = 'binance API down. Try again in a few minutes.'
else:
    usd_brl = usd_brl_api['price']

    pancakeswap = get_api_data('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd')
    if pancakeswap:
        macoin = pancakeswap.get('data')
        timestamp = pancakeswap.get('updated_at')
        humantime = datetime.fromtimestamp(int(timestamp/1000))
        macoin_usd = pancakeswap.get('data', {}).get('price')
        macoin_bnb = pancakeswap.get('data', {}).get('price_BNB')
    
        if usd_brl:
            value_brl = float(usd_brl)
            value_usd = float(macoin_usd)
            macoin_brl = round(value_brl * value_usd, 20)
    
            message_text = '**MaCoin price USD:** ${}\n'.format(macoin_usd)
            message_text += '**MaCoin price BNB:** ${}\n'.format(macoin_bnb)
            message_text += '**MaCoin price BRL:** R${}\n\n'.format(macoin_brl)
            message_text += 'Updated at: {}'.format(humantime)
        else:
            message_text = 'api.pancakeswap.info down. Try again in a few minutes.'
    else:
        usd = get_api_data('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BUSD&sellAmount=1')
        bnb = get_api_data('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BNB&sellAmount=1')
        if usd and bnb:
            macoin_usd = usd.get('price')
            macoin_bnb = bnb.get('price')
            if usd_brl:
                value_brl = float(usd_brl)
                value_usd = float(macoin_usd)
                macoin_brl = round(value_brl * value_usd, 20)
                message_text = '**MaCoin price USD:** ${}\n'.format(macoin_usd)
                message_text += '**MaCoin price BNB:** ${}\n'.format(macoin_bnb)
                message_text += '**MaCoin price BRL:** R${}'.format(macoin_brl)
            else:
                message_text = 'bsc.api.0x.org down. Try again in a few minutes.'
        else:
            message_text = 'Pancakeswap.info and bsc.api.0x.org API down. Try again in a few minutes.'
