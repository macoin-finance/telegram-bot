MESSAGE_TEXT='**Buy using PancakeSwap:**\thttps://macoin.com.br/buy\n\n**Buy using PIX (Brazil)  or credit card:**\thttps://macoin.com.br/xchange'

def buy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
