import discord
from discord.ui import Modal, InputText
from database.models import Feedback

class FeedbackForm(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, title="Форма обратной связи")
        self.add_item(InputText(label="Как к вам обращаться?",
                                placeholder="Введите ваше имя"))
        self.add_item(InputText(label="Ваша почта", 
                                placeholder="st.*****@kigm23.ru"))
        self.add_item(InputText(label="Введите ваш вопрос", 
                                style=discord.InputTextStyle.multiline
                                )
        )
    
    async def callback(self, interaction: discord.Interaction):
        name, email, qestion = map(lambda x: x.value, self.children)
        print(name, email, qestion)

        await Feedback.create(name=name, 
                              email=email, 
                              qestion=qestion, 
                              user_id = interaction.user.id
        )
        await interaction.respond("Форма зачтена")