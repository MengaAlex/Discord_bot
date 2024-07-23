from discord.ext import commands
from discord.ui import Select, View
import discord

@commands.slash_command()
async def learn(ctx: discord.ApplicationContext):
    select = Select(
        placeholder="Учебные материалы",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="Заказать справку",
                                 description="о обучении/в военкомат",
                                 emoji="🆚",
                                 value="https://docs.google.com/forms/d/e/1FAIpQLSdywGJFjEk399XL3SSyaraFL3wfH1A8fTJBhjOmcWSCjBwJgg/viewform"),
            discord.SelectOption(label="Перейти в гугл класс",
                                 description=None,
                                 emoji="🆚",
                                 value="https://classroom.google.com"),
            discord.SelectOption(label="dev2",
                                 description=None,
                                 emoji="🆚",
                                 value="deev")
        ]
    )

    async def newCallback(interaction: discord.Interaction):
        await interaction.response.send_message(select.values)

    select.callback = newCallback
    view = View(select)
    await ctx.respond("Пожалуйста!", view=view)

def setup(bot: discord.Bot):
    bot.add_application_command(learn)