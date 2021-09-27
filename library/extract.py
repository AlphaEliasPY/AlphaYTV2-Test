# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : YoTube Downloader [ Telegram ]
# Repo     : https://github.com/AlphaEliasPY/AlphaYT
# Author   : AlphaElias [ https://t.me/AlphaElias ]
# Credits  : https://github.com/SpEcHiDe/AnyDLBot

from youtubesearchpython import *

async def youtube_search(query):
    search = VideosSearch(query)
    result = search.result()['result']
    return result

async def yt_link_search(url):
    videoInfo = Video.getInfo(url, mode=ResultMode.dict)
    return videoInfo

