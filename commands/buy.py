MESSAGE_TEXT='**Buy using BNB:**\thttps://macoin.finance/buy\n\n**Buy using PIX (BRL):**\thttps://macoin.finance/pix'

def buy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
