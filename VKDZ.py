# -*- coding: utf-8 -*-
AUTOREZE_URL = "https://oauth.vk.com/authorize"
APP_ID = 6217022
VERSION = "5.68"

params = {
        "client_id": APP_ID,
        "display": "page",
        "redirect_uri": "https://oauth.vk.com/blank.html",
        "scope": "friends",
        "respons_type": "token",
        "v": VERSION
        }

print ('?').join(
        (AUTOREZE_URL, urlencode(params)
        ))