from discord.ext import commands
import discord
from database.models import Words

class ProfanityFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print("cogs_CensoredWords: loaded")
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.message):
        self.words = await Words.all().values_list("word")
        if any(item[0] in message.content.lower().split(",") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split(" ") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split(".") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split("*") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split("/") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split("@") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split("+") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split("-") for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        elif any(item[0] in message.content.lower().split() for item in self.words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} такие слова запрещены! \n Выражайтесь культурней.")
        else:
            pass

            

def setup(bot):
    bot.add_cog(ProfanityFilter(bot))
