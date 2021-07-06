import discord
from discord.ext import commands, tasks
import main
from commands import help, game, account, HopeWiki, item

class Cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'eval')
    async def evaaal(self, ctx, arg):
        if ctx.author.id == 401282433426653186 or 677767957895708672:
            await ctx.channel.send(eval(arg))

    @commands.command(name= '아이템추가')
    async def itemsavecmd(self, ctx, id, amount):
        if ctx.author.id == 401282433426653186:
            await item.save_item(id, amount, ctx)

    @commands.command(name= '아이템삭제')
    async def itemdeletecmd(self, ctx, line, amount):
        if ctx.author.id == 401282433426653186:
            await item.delete_item(line, amount, ctx)
    