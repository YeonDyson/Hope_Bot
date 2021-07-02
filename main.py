import json
import discord
from discord.ext import commands, tasks
from commands import help, game, account, HopeWiki, cmd
bot = commands.Bot(command_prefix='희망봇 ')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("희망봇 명령어"))
    print("로딩ㄷㄷ돠ㅣㅅ")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        seconds = round(error.retry_after)
        await ctx.channel.send(f"``{seconds}``초 후 가능해요 아무튼")
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        embed = discord.Embed(color=0xec4747)
        embed.add_field(name="핑! 퐁", value=error, inline=True)
        embed.set_footer(text="이이건 샌즈네요")
        await ctx.channel.send(embed=embed)
        
if __name__ == "__main__":
    bot.add_cog(help.Core(bot))
    bot.add_cog(cmd.Cmd(bot))
    bot.add_cog(game.games(bot))
    bot.add_cog(account.games(bot))
    bot.add_cog(HopeWiki.Wiki(bot))
    bot.run("ODU3MDY4MDY2OTc0NTk3MTQx.YNKM1g.3VeW3ZgxEfbqzuFSGUJFH8KqpT8")