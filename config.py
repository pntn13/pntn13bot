# -*- coding: utf-8 -*-
import os

token = os.environ.get("TELEBOT_TOKEN")

if token is None:
    raise Exception("TELEBOT_TOKEN is not set!")
