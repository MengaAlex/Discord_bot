import discord
from modal.FeedbackForm import FeedbackForm
from database.models import Feedback

feedback = discord.SlashCommandGroup("feedback")

@feedback.command()
async def add(ctx: discord.ApplicationContext):
    """Создать форму"""
    userFeedback = await Feedback.filter(user_id=ctx.user.id).first()
    if not userFeedback:
        await ctx.send_modal(FeedbackForm())
    else:
        await ctx.respond("Вы уже отправляли форму")

    await ctx.send_modal(FeedbackForm())

@feedback.command()
async def close_user_form(ctx: discord.ApplicationContext, user: discord.Member):
    """Закрыть форму"""
    userFeedback = await Feedback.filter(user_id=ctx.user.id).first()

    if not userFeedback:
        await ctx.respond("У пользователя нет активной заявки")
    else:
        await userFeedback.delete()
        await ctx.respond("Форма закрыта")

@feedback.command()
async def check_form_status(ctx: discord.ApplicationContext):
    """Проверка формы"""
    userFeedback= await Feedback.filter(user_id=ctx.user.id).first()

    if userFeedback:
        await ctx.respond("Форма на расмотрении")
    else:
        await ctx.respond("Форма рассмотрена или вы ее еще не отправляли")


def setup(bot: discord.Bot):
    bot.add_application_command(feedback)