import requests

MACOIN = requests.get('https://bsc.api.0x.org/swap/v1/price?sellToken=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd&buyToken=BUSD&sellAmount=1').json()

MESSAGE_TEXT = f"**MaCoin price:** ${MACOIN['price']}"

def price(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
