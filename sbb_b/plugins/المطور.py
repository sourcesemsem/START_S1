from telethon import Button, events

from sbb_b import sbb_b 

from ..Config import Config

ROZ_PIC = "https://telegra.ph/file/1d033934ba8ab84145760.jpg"
RAZAN = Config.TG_BOT_USERNAME
ROZ_T = (
    f"**مطورين سيمو سبايدر **\n"
  
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("المطور") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("سمير", "https://t.me/DEV_SAMIR"),
                    Button.url("🕷", "https://t.me/FTTUTY"),
                    Button.url("الـقـناة 🕷", "https://t.me/FTTUTY"),
                    Button.url("الجروب 🕷", "https://t.me/FTTUTY"),
                    
                ]
            ]
            
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ_T, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="JMTHON - sbb_b",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JMTHON - sbb_b",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@sbb_b.ar_cmd(pattern="المطور")
async def repo(event):
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(FTTUTY, "المطور")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @RR77R
