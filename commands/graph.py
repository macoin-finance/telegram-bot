MESSAGE_TEXT='**Link to access the chart :** https://charts.bogged.finance/?token=0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd'

def graph(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown')
