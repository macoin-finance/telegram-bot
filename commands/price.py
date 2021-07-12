import requests
from datetime import datetime

try:
    MACOIN = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()["data"]
    TIMESTAMP = requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd').json()['updated_at']
    HUMANTIME = datetime.fromtimestamp(int(TIMESTAMP/1000))
    MESSAGE_TEXT = f"**MaCoin price USD:** ${MACOIN['price']}\n**MaCoin price BNB:** ${MACOIN['price_BNB']}\n\nPreço atualizado em: {HUMANTIME}"
    def price(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
except requests.ConnectionError:
    MESSAGE_TEXT = f"**API da Pancakeswap.info fora do ar. Tente novamente em alguns minutos."

    def price(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
