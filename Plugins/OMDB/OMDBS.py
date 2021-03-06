# @lx575
from bot import autoforward
from asyncio import sleep
from Plugins.OMDB import get_movie_info
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
               
@autoforward.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        r, title = message.text.split(None, 1)        
        try:
            poster, id, text = get_movie_info(title)
            buttons=[[InlineKeyboardButton('ð ð¨ð¬ð£ð»', url=f"https://www.imdb.com/title/{id}"), InlineKeyboardButton('ð¥ððððð ð®ð ð¦ððððð»', url=f"https://GitHub.com/lx575")]]    
            m=await message.reply_text("ð¥ððð½ððð ð£ð¾ððºððð..")
            await message.reply_photo(photo=poster.replace("SX300",""), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
            await sleep(2)
            await m.delete()                                                          
        except ValueError:
            m=await message.reply_text("ð²ðððð,\nð¨ ð¢ðºð'ð ð¥ððð½ ð¯ðððð¾ðð.\nð²ð¾ðð½ððð ð ððºðððºð»ðð¾ ð£ð¾ððºððð..")
            await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
            await sleep(4)
            await m.delete()
        except Exception as e:
            buttons=[[InlineKeyboardButton('ð ð²ð¾ðºðð¼ð ð®ð ð¦ððððð¾.', url=f'https://google.com/search?q={title.replace(" ","+")}')]]
            await message.reply_text(text="ð¢ðððð½ð'ð ð¥ð¾ðð¼ð ð£ð¾ððºððð\nð³ðð ð³ð ð¢ðð¾ð¼ð yoðð ð²ðð¾ððððð.", reply_markup=InlineKeyboardMarkup(buttons))  
            await m.delete()   
            print(e)
