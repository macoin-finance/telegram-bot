MESSAGE_TEXT='**Latest news**:\n\nhttps://www.lacryptomonnaie.net/portugais/macoin-est-le-nouveau-token-meme-cree-au-bresil/\n\nhttps://criptoeconomia.com.br/macoin-e-o-novo-token-meme-criado-no-brasil/\n\nhttps://www.reddit.com/r/farialimabets/comments/oat7b6/macoin_beck_token_100_brasileiro_focado_em/\n\nCoin Gecko:\thttps://www.coingecko.com/en/coins/macoin\n\nDetail Review:\thttps://www.youtube.com/watch?v=UKCalIK5D90\n\nCoin Sniper:\thttps://coinsniper.net/coin/7600\n\n\n\nAccess our channel for news about MaCoin: https://t.me/macoinfinance'

def news(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
