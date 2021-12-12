# -*- coding: utf-8 -*-
import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
with open('words.txt', 'r', encoding='utf-8') as file:
    word_list = file.read().splitlines()
