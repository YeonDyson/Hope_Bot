import discord
from discord.ext import commands, tasks

class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def 명령어(self, ctx):

        user_id = ctx.author.id
        user_name = ctx.author.name

        embed = discord.Embed(title = "희망봇",color= 0xfbb907)
        embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
        embed.add_field(name="희망위키", value="다양한 정보를 보거나 추가할 수 있아요 \n ``위키만들기``:위키를 새로 만들어요 \n ``페이지추가``:위키에 페이지를 추가해요 \n ``위키삭제``:위키를 삭제해요 \n ``페이지삭제``:페이지를 삭제해요", inline=True)
        embed.add_field(name="게임", value="``가입``:희망봇에 가입을 해요 \n ``탈퇴``:희망봇에 탈퇴를 해요 \n ``낚시``:물고기를 낚아요 \n ``낚시상점``: 낚시와 관련된 아이템을 사거나 팔 수 있서요\n ``인벤토리``: 인벤토리를 봐요", inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url ,text=f"{user_name}의해 실행됨")

        await ctx.channel.send(embed=embed)