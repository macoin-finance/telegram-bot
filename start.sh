#!/bin/bash

echo 'BOTAPITOKEN="xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxx"' > /home/morfetico/morfetico-telegram/.env

cd /home/morfetico/morfetico-telegram
python bot.py
