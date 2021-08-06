MESSAGE_TEXT='**Carteira de MACOIN da Associação Perifericos:**\t0x0945DF3d9081DE4eA2d947B7cE2547Dc5D5409b3\n\nDoação de cobertores, mantimentos e afins\n\nContato:\tAffonso Jr. - @affonsoj\n'

def doe(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
