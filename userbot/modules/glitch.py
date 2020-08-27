"""
designed By @Krishna_Singhal in userge
ported to telethon by @mrconfused and @sandy1709
"""

import os
from PIL import Image
from glitch_this import ImageGlitcher
from userbot.utils.funtions import runcmd, take_screen_shot
from userbot import bot, LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

@register(pattern="^.glitch(?: |$)(.*)", outgoing=True)
async def glitch(cat):
    await cat.edit("```Glitching... 😁```")
    cmd = cat.pattern_match.group(1)
    catinput = cat.pattern_match.group()
    reply = await cat.get_reply_message(2)
    if not (reply and (reply.media)):
        await cat.edit("`Media not found...`")
        return
    if not os.path.isdir("TEMP_DOWNLOAD_DIRECTORY"):
        os.mkdir("TEMP_DOWNLOAD_DIRECTORY")
    catid = cat.reply_to_msg_id
    catsticker = await reply.download_media(file = "TEMP_DOWNLOAD_DIRECTORY")
    if not catsticker.endswith(('.mp4','.webp','.tgs','.png','.jpg')):
        os.remove(catsticker)
        await cat.edit("`Media not found...`")
        return
    file = os.path.join("TEMP_DOWNLOAD_DIRECTORY", "glitch.png")
    if catinput:
        if not catinput.isdigit():
            await cat.edit("`You input is invalid, check help`")
            return
        catinput = int(catinput)
        if not 0 < catinput< 9:
            await cat.edit("`Invalid Range...`")
            return
    else:
        catinput = 2
    if catsticker.endswith(".tgs"):
        catfile = os.path.join("TEMP_DOWNLOAD_DIRECTORY", "glitch.png")
        catcmd = f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`catsticker not found...`")
            LOGS.info(stdout + stderr)
        glitch_file = catfile
    elif catsticker.endswith(".webp"):
        catfile = os.path.join("TEMP_DOWNLOAD_DIRECTORY", "glitch.png")
        os.rename(catsticker , catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`catsticker not found... `")
            return
        glitch_file = catfile
    elif catsticker.endswith(".mp4"):
        catfile = os.path.join("TEMP_DOWNLOAD_DIRECTORY", "glitch.png")
        await take_screen_shot(catsticker , 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```catsticker not found...```")
            return
        glitch_file = catfile
    else:
        glitch_file = catsticker
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    if cmd == "glitchs":
        glitched = "TEMP_DOWNLOAD_DIRECTORY" + "glitched.webp"
        glitch_img = glitcher.glitch_image(img, catinput, color_offset=True)
        glitch_img.save(glitched)
        await bot.send_file(
            cat.chat_id,
            glitched,
            reply_to_message_id= catid)
        os.remove(glitched)
        await cat.delete()
    elif cmd == "glitch":
        Glitched = "TEMP_DOWNLOAD_DIRECTORY" + "glitch.gif"
        glitch_img = glitcher.glitch_image(img, catinput, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            Glitched,
            format='GIF',
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP)
        await bot.send_file(
            cat.chat_id,
            Glitched,
            reply_to_message_id=catid)
        os.remove(Glitched)
        await cat.delete()
    for files in (catsticker, glitch_file):
        if files and os.path.exists(files):
            os.remove(files)

CMD_HELP.update({
    "glitch":
    "**SYNTAX : **`.glitch` reply to media file\
    \n**USAGE :** glitches the given mediafile(gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    \n\n**SYNTAX : **`.glitchs` reply to media file\
    \n**USAGE :** glitches the given mediafile(gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    "
})            
