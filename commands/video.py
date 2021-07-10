MESSAGE_TEXT='**Android:** https://macoin.finance/android\n**iPhone:** https://macoin.finance/video'

def video(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
