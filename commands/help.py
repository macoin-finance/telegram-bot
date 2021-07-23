MESSAGE_TEXT='Commands available to MaCoinEIROS:\n/site\tMaCoin official website\n/video\tDisplay tutorials in video\n/contract\tDisplay MaCoin contract\n/price\tDisplay current MaCoin price\n/metamask\tTutorial for metamask\n/trust\tTutorial for trust wallet\n/graph\tDisplay the MaCoin graph\n/news\tDisplay the latest news\n/discord\tOfficial MaCoin Discord/\n/store\tOfficial MaCoin Store \n/twitter\tOfficial Twitter\n/instagram\tOfficial Instagram\n/tokenomics\tDisplay Tokenomics\n/clubhouse\tClub oficial da primeira comunidade brasileira da macoin no Clubhouse\n/help\tDisplay this help message'

def macoin_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT)
