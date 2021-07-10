# MaCoin Bot

## Installation

### (Optional) Create a virtual environment and git clone the bot

```bash
useradd -m morfetico
su - morfetico
git clone https://github.com/macoin-finance/telegram-bot.git
mv telegram-bot /home/morfetico/morfetico-telegram
```

### Create a `.env` file and add your bot api token

```
BOTAPITOKEN=paste your api token here
```
### Install dependencies:
- python-telegram-bot
- requests
- python-dotenv

```bash
pip install -r requirements.txt
```

### Run your bot

```bash
bash -x start.sh
```
