MESSAGE_TEXT='**For medicinal purposes only!**\n'

def hemp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
