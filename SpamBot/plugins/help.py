from SpamBot import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from SpamBot import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/af4d078f6feba0fef9cd5.jpg"

DOLL_Help = "๐ฅ ๐๐ฅ๐๐ข ๐ฝ๐ค๐ฉ ๐ฅ\n\n"

DOLL_Help = "**๊ง๐ฎ๐ณ ๐  ๐๐ถ๐น๐ ๐ผ๐ ๐ผ๐๐น๐พ๐ถ  ๐ ๐ฎ๐ณ๊ง**\n"
 
DOLL_Help += f"__แดแดษดแดs แดแด แดษชสแดสสแด ษชษด sแดแดแด สแดแด__\n\n"

DOLL_Help += f" โง ๐๐๐ด๐๐ฑ๐พ๐ ๐ฒ๐ผ๐ณ๐ โง\n\n"

DOLL_Help += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n\n"
 
DOLL_Help += f" โง ๐ป๐ด๐ฐ๐๐ด ๐ฒ๐ผ๐ณ โง\n\n"

DOLL_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DOLL_Help += f" โง ๐๐ฟ๐ฐ๐ผ ๐ฒ๐ผ๐ณ๐ โง\n\n"

DOLL_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `!delayspam` - this cmd use for delay spam\n\n"

DOLL_Help += f" `!pornspam` - ษช แดกษชสส ๊ฑแดษขษขแด๊ฑแด แดแดษด'แด แด๊ฑแด แดสษช๊ฑ แดแดแดแดแดษดแด๐ โง\n\n"

DOLL_Help += f" `!hang` - ๐ โง\n\n"

DOLL_Help += f" `!bspam` - ๐๐๐ฅ๐ง๐๐๐๐ฌ ๐ฆ๐ฃ๐๐ ๐ฅต โง\n\n"

DOLL_Help += f"ยฉ @TechnoBot_Updates\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DOLL_Help,
                                  buttons=[
        [
        Button.url("โบ๏ธแดสแดษดษดแดสโบ๏ธ", "https://t.me/TechnoBot_Updates")
        ] 
        ]
        )
