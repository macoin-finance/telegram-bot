MESSAGE_TEXT='**Como adicionar a rede binance smart chain na Metamask:** https://www.evernote.com/shard/s705/sh/9cc833bd-30be-36ed-f82e-34b27edb00fa/921941bf3c9cb4f14ec0943c57bc11cf'
def metamask(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
