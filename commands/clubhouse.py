MESSAGE_TEXT='**Club oficial da primeira comunidade brasileira da macoin.finance - Desde Março de 2021 no Clubhouse:**\thttps://www.clubhouse.com/club/macoinfinance-oficial'

def clubhouse(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
