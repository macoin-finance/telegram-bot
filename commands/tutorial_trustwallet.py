MESSAGE_TEXT='**Como adicionar a rede binance smart chain na Trust Wallet:** https://www.evernote.com/shard/s705/sh/637c5a78-3df7-093f-3097-54212d2bbc12/05169afa76999b20ea0aa5b251f2f3fb'

def trust(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
