from discord.ext import commands
import discord
from database.models import Students

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.Cog.listener()
    async def on_ready(self):
        print("cogs_info: loaded")


    @discord.slash_command()
    async def info(self, ctx: discord.ApplicationContext):
        """Информация о пользователях"""
        embed = discord.Embed(
        title="INFO",
        description="Навигация по боту",
        color=0x42AAFF
        )
        embed.set_author(name="КИГМ23", url=None, icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
        embed.add_field(name="/admin", value="Перейти в раздел <информация о администрации колледжа>", inline=False)
        embed.add_field(name="/teacher", value="Перейти в раздел<информация о преподавателях>", inline=False)
        embed.add_field(name="/students", value="Перейти в раздел<информация о студентах>", inline=False)
        embed.set_thumbnail(url="https://i.postimg.cc/qvTV9zvM/logo.png")
        
        await ctx.respond("Пожалуйста!", embed=embed)


    @discord.slash_command()
    async def students(self,
                        ctx: discord.ApplicationContext,
                        name: discord.Option(str, choices = ["42ИС",
                                                            "42ГД",
                                                            "41ИС"
                                                            ],
                        description="Выберите группу")):
        """Информация о студентах из группы <name>"""
        if name == "42ИС":
            embed = discord.Embed(
            title="Студент группы 42ИС",
            description="Информация о студентах",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url=None, icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            self.group = await Students.filter(groupp="42ИС").values_list(f"firstname", "lastname", "gender", "email", "dateofbirth")
            for i in range(len(self.group)):
                embed.add_field(name="Студент группы 42ИС", value=self.group[i], inline=False)
            await ctx.respond(embed=embed)
                
        elif name =="42ГД":
            embed = discord.Embed(
            title="Студент группы 42ГД",
            description="Информация о студентах",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url=None, icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            self.group = await Students.filter(groupp="42ГД").values_list(f"firstname", "lastname", "gender", "email", "dateofbirth")
            for i in range(len(self.group)):
                embed.add_field(name="Студент группы 42ГД", value=self.group[i], inline=False)
            await ctx.respond(embed=embed)
        elif name =="41ИС":
            embed = discord.Embed(
            title="Студент группы 41ИС",
            description="Информация о студентах",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url=None, icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            self.group = await Students.filter(groupp="41ИС").values_list(f"firstname", "lastname", "gender", "email", "dateofbirth")
            for i in range(len(self.group)):
                embed.add_field(name="Студент группы 41ИС", value=self.group[i], inline=False)
            await ctx.respond(embed=embed)
        else:
            pass

    @discord.slash_command()
    async def teacher(self,
                        ctx: discord.ApplicationContext,
                        name: discord.Option(str, choices = ["Информационные технологии",
                                                            "Гуманитарные науки",
                                                            "Точные науки"
                                                            ],
                        description="Выберите дисциплину")
                     ):
        """Информация о педагогическом составе с преподаваемой дисциплиной <name>"""
        if name =="Информационные технологии":
            embed = discord.Embed(
            title="Информационные технологии",
            description="Информация о педагогическом составе с учебным направлением Информационные технологии",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/o-nas/pedagogicheskii-sostav#collapse7", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed.add_field(name="Каримов Артем Альбертович", value="karimov@kigm23.ru\n https://kigm.mskobr.ru/teacher-card/karimov_artem_al_bertovich", inline=False)
            embed.add_field(name="Иванов Александр Романович", value="ivanov@kigm23.ru\n https://kigm.mskobr.ru/teacher-card/ivanov_aleksandr_romanovich", inline=False)
            embed.add_field(name="Кравец Галина Сергеевна", value="kravec@kigm23.ru\n https://kigm.mskobr.ru/teacher-card/kravets-galina-sergeevna-1608731495", inline=False)
            embed.add_field(name="Лукьянчиков Максим Александрович", value="lookyanchikov@kigm23.ru\n https://kigm.mskobr.ru/teacher-card/lukyanchikov-maksim-aleksandrovich-1608891304", inline=False)
            embed.add_field(name="Рогожан Вячеслав Георгиевич", value="rogozhan@kigm23.ru\n https://kigm.mskobr.ru/teacher-card/rogojan-vyacheslav-georgievich-1608903359", inline=False)
            embed.add_field(name="Симонов Альберт Николаевич", value="simonov@kigm23.ru\n https://kigm.mskobr.ru/teacher-card/simonov-albert-nikolaevich-1611650336", inline=False)
            embed.set_thumbnail(url="https://i.postimg.cc/qvTV9zvM/logo.png")
            await ctx.respond(embed=embed)
        elif name =="Гуманитарные науки":
            embed = discord.Embed(
            title="Гуманитарные науки",
            description="Информация о педагогическом составе с учебным направлением Гуманитарные науки",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/o-nas/pedagogicheskii-sostav#collapse7", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed.add_field(name="Попович Вадим Олегович", value="popovich@kigm23.ru \n https://kigm.mskobr.ru/teacher-card/popovich_vadim_olegovich", inline=False)
            embed.add_field(name="Пронина Елена Юрьевна", value="pronina@kigm23.ru \n https://kigm.mskobr.ru/teacher-card/pronina-elena-yurevna-1608903024", inline=False)
            embed.set_thumbnail(url="https://i.postimg.cc/qvTV9zvM/logo.png")
            await ctx.respond(embed=embed)
        elif name =="Точные науки":
            embed = discord.Embed(
            title="Точные науки",
            description="Информация о педагогическом составе с учебным направлением Точные науки",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/o-nas/pedagogicheskii-sostav#collapse7", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed.add_field(name="Дерябина Анастасия Васильевна", value="deryabina@kigm23.ru \n https://kigm.mskobr.ru/teacher-card/deryabina_anastasiya_vasil_evna", inline=False)
            embed.set_thumbnail(url="https://i.postimg.cc/qvTV9zvM/logo.png")
            await ctx.respond(embed=embed)
        else:
            pass

    @discord.slash_command()
    async def admin(self,
                    ctx: discord.ApplicationContext,
                    post: discord.Option(str,
                                            choices=["Директор: Бабаков Дмитрий Владимирович",
                                                     "Заместитель директора: Артемова Анастасия Сергеевна",
                                                     "Советник директора: Баранников Роман Андреевич",
                                                     "Начальник службы: Романов Илья Владимирович",
                                                     "Начальник службы: Черняев Роман Анатольевич",
                                                     "Начальник службы: Янович Сергей Александрович",
                                                     "Начальник сектора: Красноруцкая Юлия Геннадиевна",
                                                     "Начальник сектора: Прохорова Анжелика Александровна",
                                                     "Начальник сектора: Сорокина Ирина Алексеевна"
                                                    ],
                                            description="Выберите нужного члена администрации")):
        
        """Информация о администрации колледжа"""

        if post == "Директор: Бабаков Дмитрий Владимирович":
            embed = discord.Embed(
            title="Бабаков Дмитрий Владимирович",
            description="Занимаемая должность: Директор",
            color=0x42AAFF
            )
            embed.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/babakov-dmitriy-vladimirovich", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed.add_field(name="email:", value="babakovdv@kigm23.ru", inline=False)
            embed.add_field(name="Контактный телефон:", value="+7 (499) 169-93-67", inline=False)
            embed.set_thumbnail(url="https://i.postimg.cc/Twfm1RWj/babakov-foto-1665044171.jpg")
            embed.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed)
        elif post =="Заместитель директора: Артемова Анастасия Сергеевна":
            embed2 = discord.Embed(
            title="Артемова Анастасия Сергеевна",
            description="Занимаемая должность: Заместитель директора",
            color=0x42AAFF
            )
            embed2.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/artemova-anastasiya-sergeevna", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed2.add_field(name="email:", value="artemova@kigm23.ru", inline=False)
            embed2.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed2.set_thumbnail(url="https://i.postimg.cc/PqkvVtKG/image.jpg")
            embed2.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed2)
        elif post =="Советник директора: Баранников Роман Андреевич":
            embed3 = discord.Embed(
            title="Баранников Роман Андреевич",
            description="Занимаемая должность: Советник директора по воспитанию и взаимодействию с детскими общественными объединениями",
            color=0x42AAFF
            )
            embed3.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/barannikov-roman-andreevich", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed3.add_field(name="email:", value="barannikov@kigm23.ru", inline=False)
            embed3.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed3.set_thumbnail(url="https://i.postimg.cc/x8qXNqjm/barannikov-1678352317-1710421291.jpg")
            embed3.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed3)        
        elif post =="Начальник службы: Романов Илья Владимирович":
            embed4 = discord.Embed(
            title="Романов Илья Владимирович",
            description="Занимаемая должность: Начальник службы",
            color=0x42AAFF
            )
            embed4.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/romanov-ilya-vladimirovich", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed4.add_field(name="email:", value="romanov@kigm23.ru", inline=False)
            embed4.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed4.set_thumbnail(url="https://kigm.mskobr.ru/teacher-card/romanov-ilya-vladimirovich")
            embed4.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed4)       
        elif post =="Начальник службы: Черняев Роман Анатольевич":
            embed5 = discord.Embed(
            title="Черняев Роман Анатольевич",
            description="Занимаемая должность: Начальник службы",
            color=0x42AAFF
            )
            embed5.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/chernyaev-roman-anatolevich", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed5.add_field(name="email:", value="chernyaev@kigm23.ru", inline=False)
            embed5.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed5.set_thumbnail(url="https://i.postimg.cc/kX02Dn0V/image.jpg")
            embed5.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed5)
        elif post =="Начальник службы: Янович Сергей Александрович":
            embed6 = discord.Embed(
            title="Янович Сергей Александрович",
            description="Занимаемая должность: Начальник службы",
            color=0x42AAFF
            )
            embed6.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/yanovich-sergey-aleksandrovich", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed6.add_field(name="email:", value="yanovich@kigm23.ru", inline=False)
            embed6.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed6.set_thumbnail(url="https://i.postimg.cc/N0zFqBkf/image.jpg")
            embed6.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed6)
        elif post =="Начальник сектора: Красноруцкая Юлия Геннадиевна":
            embed7 = discord.Embed(
            title="Красноруцкая Юлия Геннадиевна",
            description="Занимаемая должность: Начальник сектора",
            color=0x42AAFF
            )
            embed7.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/krasnorutskaya-yuliya-gennadievna-1608731626", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed7.add_field(name="email:", value="krasnorutskaya@kigm23.ru", inline=False)
            embed7.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed7.set_thumbnail(url="https://i.postimg.cc/s2qjHK3M/image.jpg")
            embed7.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed7)
        elif post =="Начальник сектора: Прохорова Анжелика Александровна":
            embed8 = discord.Embed(
            title="Прохорова Анжелика Александровна",
            description="Занимаемая должность: Начальник сектора",
            color=0x42AAFF
            )
            embed8.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/prohorova-anjelika-aleksandrovna-1608903089", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed8.add_field(name="email:", value="prohorova@kigm23.ru", inline=False)
            embed8.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed8.set_thumbnail(url="https://i.postimg.cc/BQ4qzjfB/image.jpg")
            embed8.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed8)
        elif post =="Начальник сектора: Сорокина Ирина Алексеевна":
            embed9 = discord.Embed(
            title="Сорокина Ирина Алексеевна",
            description="Занимаемая должность: Начальник сектора",
            color=0x42AAFF
            )
            embed9.set_author(name="КИГМ23", url="https://kigm.mskobr.ru/teacher-card/sorokina-irina-alekseevna", icon_url="https://i.postimg.cc/qvTV9zvM/logo.png")
            embed9.add_field(name="email:", value="sorokinai@kigm23.ru", inline=False)
            embed9.add_field(name="Контактный телефон:", value="Отсутствует", inline=False)
            embed9.set_thumbnail(url="https://i.postimg.cc/sg0s1KQT/image.jpg")
            embed9.set_footer(text="Нажмите на <КИГМ23> в левом вверхнем углу для подробной информации")
            await ctx.respond(embed=embed9)
        else:
            pass

def setup(bot):
    bot.add_cog(Info(bot))