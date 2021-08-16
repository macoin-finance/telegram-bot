MESSAGE_TEXT='**Carteira de MACOIN do Dr. Geovane Massa:**\t0x50f69C1683713AADeD613022a0f38Dbc1Cecc2Dd\n\nSite:\thttps://espacosativa.com.br/equipe-profissional/dr-geovane-massa/\n\nInstagram:\thttps://www.instagram.com/drgeovanemassa/\n\nMédico | Professor | Pesquisador | CRM: 26.153 BA\n\nContato: +55 71 99695-6256\n#############################\n\n'

def medicos(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
