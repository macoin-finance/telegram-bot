MESSAGE_TEXT='Comandos disponíveis aos MaCoineiros:\n/site\tSite oficial da MaCoin\n/video\tExibe os tutoriais em video\n/contract\tExibe o contrato da MaCoin\n/price\tExibe o preço atual da MaCoin\n/metamask\tTutorial para metamask\n/trust\tTutorial para trust wallet\n/graph\tExibe o gráfico da MaCoin\n/help\tExibe esta mensagem de ajuda\n/launch\tData do lançamento oficial'

def macoin_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT)
