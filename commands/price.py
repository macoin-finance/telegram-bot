import requests
from datetime import datetime


def get_api_data(url):

    try:
        response = requests.get(url)
        result = response.json()
    except equests.exceptions.RequestException:
        result = {}
    return result

usd_brl = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL').json()['price']


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
        message_text += 'Preço atualizado em: {}'.format(humantime)
    else:
        message_text = 'api.pancakeswap.info fora do ar. Tente novamente em alguns minutos'
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
        else:
            message_text = 'bsc.api.0x.org fora do ar. Tente novamente em alguns minutos'
    else:
        message_text = '**API da Pancakeswap.info e bsc.api.0x.org fora do ar. Tente novamente em alguns minutos.'
    message_text = '**MaCoin price USD:** ${}\n'.format(macoin_usd)
    message_text += '**MaCoin price BNB:** ${}\n'.format(macoin_bnb)
    message_text += '**MaCoin price BRL:** R${}'.format(macoin_brl)

def price(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode='markdown')
