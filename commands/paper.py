MESSAGE_TEXT='**GreenPaper:**\thttps://github.com/macoin-finance/macoin-site/blob/main/paper/MaCoin-GreenPaper-v0.pdf'

def paper(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
