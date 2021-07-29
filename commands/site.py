MESSAGE_TEXT='**Link to access our website:** https://macoin.com.br'

def site(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
