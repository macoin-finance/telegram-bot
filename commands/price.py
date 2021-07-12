import requests
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=30, backoff_factor=50.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
from datetime import datetime



try:
    MACOIN = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()["data"]
    TIMESTAMP = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()['updated_at']
    HUMANTIME = datetime.fromtimestamp(int(TIMESTAMP/1000))

    MESSAGE_TEXT = f"**MaCoin price USD:** ${MACOIN['price']}\n**MaCoin price BNB:** ${MACOIN['price_BNB']}\n\nPreço atualizado em: {HUMANTIME}"

    def price(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')

except requests.exceptions.ConnectionError:
    try:

        MACOINUSD = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BUSD&sellAmount=1').json()
        MACOINBNB = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BNB&sellAmount=1').json()

        MESSAGE_TEXT0x = f"**MaCoin price USD:** ${MACOINUSD['price']}\n**MaCoin price BNB:** ${MACOINBNB['price']}"

        def price(update, context):
            context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT0x, parse_mode='markdown')

#except requests.exceptions.RequestException as e:
#except urllib.error.URLError:
#
#

    except requests.exceptions.RequestException as e:

            MESSAGE_TEXTOFF = f"**API da Pancakeswap.info e bsc.api.0x.org fora do ar. Tente novamente em alguns minutos."

            def price(update, context):
                context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXTOFF, parse_mode='markdown')
