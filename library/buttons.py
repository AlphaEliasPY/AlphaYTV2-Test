# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : YoTube Downloader [ Telegram ]
# Repo     : https://github.com/AlphaEliasPY/AlphaYT
# Author   : AlphaElias [ https://t.me/AlphaElias ]
# Credits  : https://github.com/SpEcHiDe/AnyDLBot

from urllib.parse import quote
from presets import Presets
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = [
    [
        InlineKeyboardButton('View Thumb', callback_data='view_btn'),
        InlineKeyboardButton('Del Thumb', callback_data='del_btn')

    ],
    [
        InlineKeyboardButton('Ayuda', callback_data='help_btn'),
        InlineKeyboardButton('Soporte', url='t.me/RMProjects')
    ],
    [
        InlineKeyboardButton('Cerrar', callback_data='close_btn'),
        InlineKeyboardButton('buscar en linea', switch_inline_query_current_chat='')
    ]
]


del_thumb = [
    [
        InlineKeyboardButton("DEL THUMB", callback_data="thumb_del_conf_btn"),
        InlineKeyboardButton("Back", callback_data="a_back_btn")
    ]
]

join_channel = [
    [
        InlineKeyboardButton('⚙ Grupo Android', url='https://telegram.me/AndroidCave'),
        InlineKeyboardButton('buscar en linea', switch_inline_query_current_chat='')
    ]
]


back_button = [
    [
        InlineKeyboardButton('⬅️ Atras', callback_data='back_btn')
    ]
]

close_button = [
    [
        InlineKeyboardButton('❌ Cerrar', callback_data='close_btn'),
        InlineKeyboardButton('Home', callback_data='home_btn')
    ]
]

cancel_button = [
    [
        InlineKeyboardButton('Cancelar', callback_data='cancel_btn')
    ]
]

prompt_thumb_btn = [
    [
        InlineKeyboardButton('SI', callback_data='set_thumb_btn'),
        InlineKeyboardButton('No', callback_data='close_btn')
    ]
]

reply_markup_cancel = InlineKeyboardMarkup(cancel_button)
reply_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_join = InlineKeyboardMarkup(join_channel)
reply_markup_del_thumb = InlineKeyboardMarkup(del_thumb)
reply_markup_start = InlineKeyboardMarkup(start_btn)
reply_markup_thumb = InlineKeyboardMarkup(prompt_thumb_btn)

def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Presets.SHARE_BUTTON_TEXT.format(username=username))
    buttons = [[InlineKeyboardButton('Share bot', url=url),
                InlineKeyboardButton("Search Inline", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share
