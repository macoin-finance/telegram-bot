MESSAGE_TEXT='**Official Store:** https://montink.com/boyxbitcoin?produto=macoin'

def store(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
