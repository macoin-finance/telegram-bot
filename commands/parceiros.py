MESSAGE_TEXT='**Carteira de MACOIN da Associação Reconstruir Cannabis:**\t0xE14EA0C3FCF43b0f8423c23840Cf34F26F8d0cBe\n\nSite:\thttps://reconstruir.org.br\n\nInstagram:\thttps://instagram.com/reconstruircannabis'

def parceiros(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
