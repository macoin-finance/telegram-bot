MESSAGE_TEXT='**Últimas notícias**:\n\nhttps://www.lacryptomonnaie.net/portugais/macoin-est-le-nouveau-token-meme-cree-au-bresil/\n\nhttps://criptoeconomia.com.br/macoin-e-o-novo-token-meme-criado-no-brasil/\n\nhttps://www.reddit.com/r/farialimabets/comments/oat7b6/macoin_beck_token_100_brasileiro_focado_em/\n\n\n\nAcesse nosso canal para obter as novidades sobre a MaCoin: https://t.me/macoinfinance'

def news(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
