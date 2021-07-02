import asyncio
import discord, json
from discord.ext import commands, tasks
from collections import OrderedDict

class games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    

    @commands.command(name= '가입')
    async def account(self, ctx):
        # user_tag = ctx.author.discriminator
        user_id = ctx.author.id
        user_name = ctx.author.name
        emoji = ['🟩', '🟥']

        with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)

        if f'{user_id}' in user_data:
            embed = discord.Embed(color= 0xec4747)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.add_field(name="오...", value="이미 가입 돼있네요............", inline=True)
            await ctx.channel.send(embed=embed)

        else:
            embed = discord.Embed(color= 0x00ff9c)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.add_field(name="가입입", value="뭐 저장하는건 닉네임과 아이디 밖에없서요 ¯\_(ツ)_/¯", inline=True)
            embed.add_field(name="ㅁㅁㅁ", value="동의 하지 않으면 이용할떄 일부제한이 있을수도있서요", inline=False)
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction('🟩')
            await msg.add_reaction('🟥')

            def check(reactin, user):
                return str(reactin) in emoji and user == ctx.author and reactin.message.id == msg.id
            try:
                reactin, _user = await self.bot.wait_for(event='reaction_add', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                embed = discord.Embed(color= 0x00ff9c)
                embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                embed.add_field(name="어음.........", value="흠ㅁ흐으음", inline=True)
                await msg.edit(embed=embed)
            else:
                if str(reactin) == '🟩':
                    Information = OrderedDict()
                    user_Information = OrderedDict()
                    user_Information["name"] = user_name
                    user_Information["money"] = 100
                    user_Information["levels"] = 1
                    user_Information["exp"] = 0
                    user_Information["power"] = 1
                    user_Information["def"] = 1
                    user_Information["hp"] = 100
                    user_Information["item"] = {'weapon': 3, 'armor': 1, 'totem': 1}
                    user_Information["fish"] = {'salmon': 0, 'Mackerel': 0, 'tuna': 0, 'cod': 0, 'Clownfish': 0, 'goldfish': 0}
                    user_Information["Inventory"] = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
                    Information[user_id] = user_Information
                    user_data.update(Information)

                    with open('user.json', 'w', encoding='utf-8') as outfile: json.dump(user_data , outfile, indent=4)
        
                    embed = discord.Embed(color= 0x00ff9c)
                    embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.add_field(name="우와와아우", value="가입 완료!", inline=True)
                    await msg.edit(embed=embed)    
                elif str(reactin) == '🟥':
                    embed = discord.Embed(color= 0x00ff9c)
                    embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.add_field(name="파이", value="ㅠ", inline=True)
                    await msg.edit(embed=embed)

    @commands.command(name= '탈퇴')
    async def secession(self, ctx):
        user_id = ctx.author.id
        user_name = ctx.author.name
        emoji = ['🟩', '🟥']

        with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)

        if f'{user_id}' in user_data:
            embed = discord.Embed(color= 0x00ff9c)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.add_field(name="ㅓ......", value="진짜로 탈퇴하실건가요", inline=True)
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction('🟩')
            await msg.add_reaction('🟥')

            def check(reactin, user):
                return str(reactin) in emoji and user == ctx.author and reactin.message.id == msg.id

            try:
                reactin, _user = await self.bot.wait_for(event='reaction_add', timeout=15.0, check=check)

            except asyncio.TimeoutError:
                embed = discord.Embed(color= 0x00ff9c)
                embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                embed.add_field(name="어음.........", value="흠ㅁ흐으음", inline=True)
                await msg.edit(embed=embed)

            else:
                if str(reactin) == '🟩':
                    embed = discord.Embed(color= 0x00ff9c)
                    embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                    embed.add_field(name="파이", value="성공적으로 탈퇴했서요 언젠간 다시 와요 ㅠ", inline=True)
                    await msg.edit(embed=embed)

                    del user_data[f"{user_id}"]
                    with open('user.json', 'w', encoding='utf-8') as outfile: json.dump(user_data , outfile, indent=4)
                elif str(reactin) == '🟥':
                    embed = discord.Embed(color= 0x00ff9c)
                    embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                    embed.add_field(name="ㅠ", value=":sob:", inline=True)
                    await msg.edit(embed=embed)

        else:
            embed = discord.Embed(color= 0xec4747)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.add_field(name="?", value="탈퇴할 계정이 없는데요?", inline=True)
            await ctx.channel.send(embed=embed)