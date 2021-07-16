import requests
from bs4 import BeautifulSoup

def get_holders():
  try:
    response = requests.get("https://bscscan.com/token/0x20f23bc6f28bd31f9869b9c7750fdeafed7d22cd")
    soup = BeautifulSoup(response.content, 'html.parser')
    holders = soup.select("#ContentPlaceHolder1_tr_tokenHolders > div > div.col-md-8 > div > div")
    result = holders[0].text
    result = result.replace('\n', '')
  except:
    result = ''
  return result

def get_coins_available_to_buy():
  try:
    response = requests.get("https://bscscan.com/token/0x20f23bc6f28bd31f9869b9c7750fdeafed7d22cd?a=0x2b2e99f2ddd6c92ecfc11b6a82fdea14e2e8ab8c")
    soup = BeautifulSoup(response.content, 'html.parser')
    holders = soup.select("#ContentPlaceHolder1_divFilteredHolderBalance")
    result = holders[0].text
    result = result.replace('\n', '')
    result = result.replace('Balance', '')
  except:
    result = ''
  return result

def get_coins_burned():
  try:
    response = requests.get("https://bscscan.com/token/0x20f23bc6f28bd31f9869b9c7750fdeafed7d22cd?a=0x000000000000000000000000000000000000dead")
    soup = BeautifulSoup(response.content, 'html.parser')
    holders = soup.select("#ContentPlaceHolder1_divFilteredHolderBalance")
    result = holders[0].text
    result = result.replace('\n', '')
    result = result.replace('Balance', '')
  except:
    result = ''
  return result

def get_transfers():
  try:
    response = requests.get("https://bscscan.com/token/0x20f23bc6f28bd31f9869b9c7750fdeafed7d22cd")
    soup = BeautifulSoup(response.content, 'html.parser')
    transfers = soup.select("#d-md-flex justify-content-between mb-4")
    result = transfers[0].text
    result = result.replace('\n', '')
  except:
    result = ''
  return result

message_text = "MaCoin contract: 0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd\n\nBSC scan: https://bscscan.com/token/0x20F23bC6F28bd31f9869b9C7750fDEaFED7d22Cd\n\n"
message_text += "MaCoin holders: {}".format(get_holders())
message_text += "\nCoins available to buy: {}".format(get_coins_available_to_buy())
message_text += "\nCoins burned: {}".format(get_coins_burned())

def contract(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode='markdown', disable_web_page_preview='True')
