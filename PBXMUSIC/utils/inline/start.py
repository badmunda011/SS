from pyrogram.types import InlineKeyboardButton

import config
from PBXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=" ʜᴇʟᴘ ", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text=" sᴇᴛ ", callback_data="settings_helper"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" ʜᴇʟᴘ ", callback_data="settings_back_helper")
            InlineKeyboardButton(text=" ᴅᴇᴠ ", url=f"https://t.me/ll_BAD_MUNDA_ll"),
            ],
                    [
                    InlineKeyboardButton(text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons
    
