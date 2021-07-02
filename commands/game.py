import discord, json, random
from discord.ext import commands, tasks
from collections import OrderedDict

class games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= '낚시')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def fishing(self, ctx):
        user_id = ctx.author.id
        with open('user.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        if f'{user_id}' in user_data:
            fish = ['연어', '고등어', '참치', '대구', '흰동가리', '금붕어']
            random_fishing = random.choices(fish, weights=[30, 30, 25, 30, 10, 25])[0]
            embed = discord.Embed(color= 0x00ff9c)
            embed.add_field(name="호우우", value=f'{random_fishing}', inline=True)
            await ctx.channel.send(embed=embed)

            if random_fishing == "연어":
                user_data[f"{user_id}"]["fish"]["salmon"] += 1
            elif random_fishing == "고등어":
                user_data[f"{user_id}"]["fish"]["Mackerel"] += 1
            elif random_fishing == "참치":
                user_data[f"{user_id}"]["fish"]["tuna"] += 1
            elif random_fishing == "대구":
                user_data[f"{user_id}"]["fish"]["cod"] += 1
            elif random_fishing == "희동가리":
                user_data[f"{user_id}"]["fish"]["Clownfish"] += 1
            elif random_fishing == "참치":
                user_data[f"{user_id}"]["fish"]["goldfish"] += 1

            with open('user.json', 'w', encoding='utf-8') as f2:
                json.dump(user_data , f2, indent="\t")

        else:
            embed = discord.Embed(color= 0xec4747)
            embed.add_field(name="이런", value="가입이 안돼있네요 희망봇 가입을 쳐보세요!", inline=True)
            await ctx.channel.send(embed=embed)

    @commands.command(name= '인벤토리')
    async def Inventory(self, ctx):

        user_id = ctx.author.id

        with open('user.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        with open('item\item.json', 'r', encoding='utf-8') as f:
            item_data = json.load(f)

        embed = discord.Embed(color= 0x00ff9c)
        embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="돈:moneybag:", value=f'``{user_data[f"{user_id}"]["money"]}``', inline=True)
        embed.add_field(name="인벤토리:pouch:", value="------------------------", inline=False)

        embed.add_field(name="낚시:fish:", value="------------------------", inline=False)
        embed.add_field(name="연어", value=f'``{user_data[f"{user_id}"]["fish"]["salmon"]}``', inline=True)
        embed.add_field(name="고등어", value=f'``{user_data[f"{user_id}"]["fish"]["Mackerel"]}``', inline=True)
        embed.add_field(name="참치", value=f'``{user_data[f"{user_id}"]["fish"]["tuna"]}``', inline=True)
        embed.add_field(name="대구", value=f'``{user_data[f"{user_id}"]["fish"]["cod"]}``', inline=True)
        embed.add_field(name="희동가리", value=f'``{user_data[f"{user_id}"]["fish"]["Clownfish"]}``', inline=True)
        embed.add_field(name="참치", value=f'``{user_data[f"{user_id}"]["fish"]["goldfish"]}``', inline=True)

        await ctx.channel.send(embed=embed)