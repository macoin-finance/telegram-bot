MESSAGE_TEXT='https://macoin.com.br/tokenomics'

def tokenomics(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown')
