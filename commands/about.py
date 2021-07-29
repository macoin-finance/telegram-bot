MESSAGE_TEXT='IPFS token:\thttp://ipfs.infura.io/ipfs/bafybeifdlbltldt734irjpiffu7lsclqs2iftynoobx46wxuznquaietgi\n\nIPFS Pwnz for the lulz:\thttps://ipfs.infura.io/ipfs/QmdF7DHHWVBwjybuVVacvhmhqMNQYQ33q1wB5J5Ef3MQv1\n\nOpen Source Software (BSD-3 Clause License):\thttps://github.com/macoin.com.br\n\nO que é um Cypherpunk:\thttps://area31.net.br/wiki/Cypherpunk\n\nManifesto Cryptoanarquista:\nhttps://area31.net.br/wiki/Manifesto_Criptoanarquista\n\nCyphernomicon:\thttps://area31.net.br/wiki/Cyphernomicon,_explica%C3%A7%C3%A3o_sobre_a_cultura_e_o_pensamento_dos_cypherpunks'

def about(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT ,  disable_web_page_preview='True')
#    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
