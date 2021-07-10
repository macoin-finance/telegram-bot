
CONTRACT='**MaCoin contract:** 0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd \n\n**BSC scan:** https://bscscan.com/token/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd'
def contract(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=CONTRACT, parse_mode='markdown')
