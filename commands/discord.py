MESSAGE_TEXT='**Link to access our Discord:** https://macoin.com.br/discord'

def discord(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
