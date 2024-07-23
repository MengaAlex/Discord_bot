import discord
from dotenv import load_dotenv
import os
import asyncio
from tortoise import Tortoise
load_dotenv()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
bot = discord.Bot(intents = discord.Intents.all(), loop = loop, debug_guilds=[247358581714714635])

@bot.event
async def on_ready():
    print("bot ready")


"""hello = ["Привет Menga", "Пока Menga"]
@bot.event
async def on_message(message: discord.Message):
    for content in message.content.split("!"):
        for hi in hello:
            if content == hi:
                print("ok")
                await message.channel.send(f"Привет {message.author.mention}!")"""


bot.load_extension("extensions.commands.command_help")
bot.load_extension("extensions.commands.command_learn")
bot.load_extension("extensions.commands.command_feedback")
bot.load_extension("extensions.cogs.cog_userInfo")
bot.load_extension("extensions.cogs.cog_censoredwords")





async def main():
    await Tortoise.init(db_url=os.getenv("DB_URL"), modules={"discord": ["database.models"]})
    await Tortoise.generate_schemas()
    await bot.login(os.getenv("BOT_TOKEN"))
    await bot.connect()
try:
    loop.run_until_complete(main())
finally:
    loop.run_until_complete(Tortoise.close_connections())