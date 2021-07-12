MESSAGE_TEXT='Comandos disponíveis aos MaCoinHEIROS:\n/site\tSite oficial da MaCoin\n/video\tExibe os tutoriais em video\n/contract\tExibe o contrato da MaCoin\n/price\tExibe o preço atual da MaCoin\n/metamask\tTutorial para metamask\n/trust\tTutorial para trust wallet\n/graph\tExibe o gráfico da MaCoin\n/news\tExibe as últimas notícias\n/discord\tDiscord Oficial da MaCoin/\n/store\tLoja oficial da MaCoin\n/help\tExibe esta mensagem de ajuda'

def macoin_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT)
