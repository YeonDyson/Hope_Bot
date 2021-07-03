import discord, json
from discord.ext import commands, tasks
from collections import OrderedDict

class Wiki(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 희망위키(self, ctx):

        user_id = ctx.author.id
        user_name = ctx.author.name
        embed = discord.Embed(title ="희망위키", description="희망위키에 오신걸 환영해요", color= 0x00ff9c)
        embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
        embed.add_field(name="명령어", value="명령어 목록", inline=True)
        embed.add_field(name="위키 보고싶은위키", value="보고싶은 위키를 볼수 있서요", inline=True)
        embed.add_field(name="위키만들기", value="위키를 새로 만들어요", inline=True)
        embed.add_field(name="페이지추가", value="위키에 페이지를 추가해요", inline=True)
        embed.add_field(name="위키삭제", value="위키를 삭제해요", inline=True)
        embed.add_field(name="페이지삭제", value="페이지를 삭제해요", inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url ,text=f"{user_name}의해 실행됨")

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def 위키만들기(self, ctx, wikiname ,name, Explanation, Youtube, url, Paragraph, Explanation2):
        user_name = ctx.author.name
        with open('wikidata\wiki.json', 'r', encoding='utf-8') as f: wiki_data = json.load(f)

        newwiki = OrderedDict()
        newwiki_data = OrderedDict()
        newwiki_data["name"] = name
        newwiki_data["Explanation"] = Explanation
        newwiki_data["youtube"] = Youtube
        newwiki_data["url"] = url
        newwiki_data["Paragraph"] = Paragraph
        newwiki_data["Explanation2"] = Explanation2
        newwiki[wikiname] = newwiki_data
        wiki_data.update(newwiki)
        with open('wikidata\wiki.json', 'w', encoding='utf-8') as outfile: json.dump(wiki_data, outfile, indent=4)

        embed = discord.Embed(title =wiki_data[wikiname]["name"], description="``"+wiki_data[wikiname]["Explanation"]+"``", color= 0x00ff9c)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
        embed.set_author(name="희망위키", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
        embed.add_field(name="유튜브", value="``"+wiki_data[wikiname]["youtube"]+"``", inline=True)
        embed.add_field(name="추가url", value="``url``", inline=True)
        embed.add_field(name=wiki_data[wikiname]["Paragraph"], value="```"+wiki_data[wikiname]["Explanation2"]+"```", inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url ,text=f"{user_name}의해 실행됨")

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def 페이지추가(self, ctx):
        await ctx.channel.send("만만드는중")

    @commands.command()
    async def 위키삭제(self, ctx):
        await ctx.channel.send("만만드는중")

    @commands.command()
    async def 페이지삭제(self, ctx):
        await ctx.channel.send("만만드는중")