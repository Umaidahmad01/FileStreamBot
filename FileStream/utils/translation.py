from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Hᴇʏ, </b>{Mantion}\n 
<b>I'ᴍ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴀs ᴡᴇʟʟ ᴅɪʀᴇᴄᴛ ʟɪɴᴋs ɢᴇɴᴇʀᴀᴛᴏʀ ғᴏʀ <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a></b>\n
<b>ᴡᴏʀᴋɪɴɢ ᴏɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ</b>\n"""

    HELP_TEXT = """
<b>- ᴀᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</b>
<b>- sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴍᴇᴅɪᴀ</b>
<b>- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ</b>\n
<b>🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.</b>\n
<i><b> ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>""""

    ABOUT_TXT = "<b>⟦{mantion}⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n⌬ ᴏᴡɴᴇʀ : <a href=https://t.me/rin_nanakura>ʀɪɴ</a>\n⌬ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Ongoing_society'>ᴏɴɢᴏɪɴɢ sᴏᴄɪᴇᴛʏ</a>\n⌬ ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ : <a href='https://t.me/anime_sub_society'>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>\n⌬ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/team_society_1'>ʙᴏᴛ sᴏᴄɪᴇᴛʏ</a>\n⌬ sᴏᴄɪᴇᴛʏ ᴄʜᴀᴛ ᴢᴏɴᴇ : <a href='https://t.me/ahss_help_zone'>ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n࿂ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/i_killed_my_clan'>❰⏤͟͞ 𝚯𝗕𝗜𝗧𝗢 -//-❱</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"


    STREAM_TEXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>Sʜᴀʀᴇ :</b> <code>{}</code>\n
<b>⛩️ <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>"""

    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>Sʜᴀʀᴇ :</b> <code>{}</code>\n
<b>⛩️ <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n<a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>"Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/Anime_Sub_Society')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/Anime_Sub_Society')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/Anime_Sub_Society')]
        ]
    )
