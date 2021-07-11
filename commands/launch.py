MESSAGE_TEXT='**Data do lançamento oficial:** 17-07-2021\n**Dias restantes para o lançamento:** 6'

def launch(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown')
