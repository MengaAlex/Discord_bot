from discord.ext import commands
import discord

@commands.slash_command()
async def help(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="HELP",
        description="Навигация по боту",
        color=0x42AAFF
    )
    embed.set_author(name="КИГМ23", url=None, icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
    embed.add_field(name="/info", value="Команда на переход к информации о пользователях", inline=False)
    embed.add_field(name="/learn", value="Команда на переход к учебным материалам", inline=False)
    embed.add_field(name="/rules", value="Команда на переход к правилам чата", inline=False)
    embed.set_thumbnail(url="https://i.postimg.cc/qvTV9zvM/logo.png")
    embed.set_footer(text="Будьте вежливы и не используйте грубые выражения в чате")
    
    await ctx.respond("Пожалуйста!", embed=embed)

def setup(bot: discord.Bot):
    bot.add_application_command(help)