import discord
from discord.ext import commands, tasks
import main

class Cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'eval')
    async def evaaal(self, ctx, arg):
        if ctx.author.id == 401282433426653186 or 677767957895708672:
            await ctx.channel.send(eval(arg))