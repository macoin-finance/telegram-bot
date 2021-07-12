MESSAGE_TEXT='**Loja Oficial MaCoin:** https://montink.com/boyxbitcoin?produto=macoin'

def store(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown')
