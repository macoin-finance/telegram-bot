MESSAGE_TEXT='**Club oficial da primeira comunidade brasileira - CYPHERPUNKS & BIOHACKERS - da macoin.com.br - Desde Março de 2021 no Clubhouse:**\thttps://www.clubhouse.com/club/cypherpunks-biohackers'

def clubhouse(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
