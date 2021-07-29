MESSAGE_TEXT='**Charts:**\n\nhttps://charts.bogged.finance/?token=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd\n\nhttps://nomics.com/assets/beck-macoin?interval=30d\n\n'

def graph(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
