# Inline-Tube-Mate (YouTube Downloader)

**An Inline Telegram bot that can download YouTube videos with permanent thumbnail support**

<br>

  - Bot need to be in Inline Mode
  - Search keyword inline (In bot chat).
  - Send a photo to bot to set custom thumbnail permanently.
  - The thumbnail will be in all the downloads until clear it in options.
  - View the custom thumbnail in option.
  - If no thumbnail available, bot will set the default YouTube video thumbnail in downloading.
  - If Authorized users are available, bot will serve to them only. If not, bot will be in public domain.

<br>

<p align="left">
  <a href="https://heroku.com/deploy?template=https://github.com/AlphaEliasPY/AlphaYT">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a>
</p>

## [@BotFather](https://t.me/botfather) Commands

* `start - Check alive`
* `send - broadcast` (As a reply to any message)
* `subs - Count active subscribers`

## Mandatory Variables

* `API_HASH`    Your API Hash from my.telegram.org
* `API_ID`      Your API ID from my.telegram.org
* `BOT_TOKEN`   Your bot token from @BotFather.
* `AUTH_USERS`  Create a list of User Ids to use this bot. (If kept empty, bot will be in public domain)
* `SUDO_USERS`  Create a list of Super User Ids to use this bot. (For Broadcasting )
* `DB_URI`  (Mandatory when deployed in local)

## Deploy Locally
Create a database URI with the [TUTORIAL](https://telegra.ph/Clonebot-UI-Help-05-30)

Create a `config.py` with the above variables (Refer sample_config.py)
```
git clone https://github.com/AlphaEliasPY/AlphaYT
cd inline-tube-mate
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```
<br>


## Credits

[Dan](https://github.com/delivrance) for his [Pyrogram Tg Framework](https://github.com/pyrogram/pyrogram)

[Shrimadhav UK](https://github.com/SpEcHIDe) for his [AnyDLBot](https://github.com/SpEcHiDe/AnyDLBot)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/AlphaEliasPY/AlphaYT&plugins=postgresql&envs=TOKEN_BOT%2CAPI_ID%2CAPI_HASH%2CAUTH_USERS%2CENV%2CSUDO_USERS)
