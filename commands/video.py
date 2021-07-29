MESSAGE_TEXT='**Android:** https://macoin.com.br/android\n**iPhone:** https://macoin.com.br/iphone'

def video(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
