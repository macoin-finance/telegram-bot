MESSAGE_TEXT='**Link para acesso ao site:** https://macoin.finance'

def site(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown')
