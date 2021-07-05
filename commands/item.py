import discord, json

from discord.ext import commands, tasks

async def save_item(id, ctx):
    user_id = ctx.author.id

    with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)
    with open('item\item.json', 'r', encoding='utf-8') as f: item_data = json.load(f)

    for i in range(9):
        if user_data[f'{user_id}']['Inventory'][f'{i}']['id'] == 0:
            user_data[f'{user_id}']['Inventory'][f'{i}']['id'] = int(id)

            with open('user.json', 'w', encoding='utf-8') as f2:
                json.dump(user_data , f2, indent="\t")
            await ctx.channel.send(f"{i}라인 저장")

            break

def delete_item(id, line, ctx):

    user_id = ctx.author.id

    with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)
    with open('item\item.json', 'r', encoding='utf-8') as f: item_data = json.load(f)