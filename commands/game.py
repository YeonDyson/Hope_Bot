import asyncio  #할일 떡밥, 상점, 던전
import discord, json, random
from discord.ext import commands, tasks
from collections import OrderedDict
from commands import item, game

class games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= '낚시')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fishing(self, ctx):
        user_id = ctx.author.id
        with open('user.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        if f'{user_id}' in user_data:

            for i in range(10):
                if user_data[f'{user_id}']['Inventory'][f'{i}']['id'] == 11:
                    paste_bait_lain = i
                    break
                else:
                    embed = discord.Embed(color= 0xfbb907)
                    embed.set_author(name="희망봇 낚시", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                    embed.add_field(name="저런", value="떡밥이 없내요", inline=True)
                    await ctx.channel.send(embed=embed)
                    return

            fishingg = ['⬜', '⬜', '⬜', '⬜', '⬜', '⬛']
            nemo = '🟦'
            fishingg[random.randrange(0,5)] = nemo
            user_fishing = ['⬜', '⬜', '⬜', '⬜', '⬜', '⬛']

            embed = discord.Embed(color= 0xfbb907)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.add_field(name="낙시중", value=f"{fishingg}", inline=False)
            embed.add_field(name="낙시중", value=f"{user_fishing}", inline=False)
            msg = await ctx.channel.send(embed=embed)

            await msg.add_reaction('🎣')

            for i in range(7):
                def check(reactin, user):
                    return str(reactin) in '🎣' and user == ctx.author and reactin.message.id == msg.id

                try:
                    reactin, _user = await self.bot.wait_for(event='reaction_add', timeout=2.0, check=check)

                except asyncio.TimeoutError:
                    user_fishing = ['⬜', '⬜', '⬜', '⬜', '⬜', '⬛']
                    user_fishing[i] = nemo

                    embed = discord.Embed(color= 0xfbb907)
                    embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.add_field(name="낙시중", value=f"{fishingg}", inline=False)
                    embed.add_field(name="낙시중", value=f"{user_fishing}", inline=False)
                    await msg.edit(embed=embed)

                else:
                    if str(reactin) == '🎣':
                        if fishingg == user_fishing:
                            if user_data[f'{user_id}']['Inventory'][f'{paste_bait_lain}']['id'] == 11:
                                fish = ['salmon', 'Mackerel', 'tuna', 'cod', 'Clownfish', 'goldfish']
                                random_fishing = random.choices(fish, weights=[30, 30, 25, 30, 1, 25])[0]
                    
                                user_data[f"{user_id}"]["fish"][f"{random_fishing}"] += 1

                                with open('user.json', 'w', encoding='utf-8') as f2:
                                    json.dump(user_data , f2, indent="\t")

                                await item.delete_item(paste_bait_lain, 1, ctx)
                                paste_bait = user_data[f'{user_id}']['Inventory'][f'{paste_bait_lain}']['amount'] - 1
                                embed = discord.Embed(color= 0xfbb907)
                                embed.set_author(name="희망봇 낚시", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                                embed.add_field(name="낚시 성공!", value=f'{random_fishing}', inline=True)
                                embed.set_footer(text=f"남은 떡밥 {paste_bait}")
                                await msg.edit(embed=embed) 
                                return
                    else:
                        embed = discord.Embed(color= 0xfbb907)
                        embed.set_author(name="희망봇 낚시", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                        embed.add_field(name="저런", value="물고기가 도망같네요", inline=True)
                        await msg.edit(embed=embed)
                        return    

            embed = discord.Embed(color= 0xfbb907)
            embed.set_author(name="희망봇 낚시", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.add_field(name="저런", value="물고기가 도망같네요", inline=True)
            await msg.edit(embed=embed)

        else:
            embed = discord.Embed(color= 0xec4747)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.add_field(name="이런", value="가입이 안돼있네요 희망봇 가입을 쳐보세요!", inline=True)
            await ctx.channel.send(embed=embed)

    @commands.command(name= '인벤토리')
    async def Inventory(self, ctx):

        with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)
        with open('item\item.json', 'r', encoding='utf-8') as f: item_data = json.load(f)

        user_id = ctx.author.id

        if f'{user_id}' in user_data:   

            user_weapon = user_data[f"{user_id}"]["item"]["weapon"]
            user_armor = user_data[f"{user_id}"]["item"]["armor"]
            user_totem = user_data[f"{user_id}"]["item"]["totem"]
            user_secondary_weapon = user_data[f"{user_id}"]["item"]["secondary_weapon"]
            user_Inventory0 = user_data[f"{user_id}"]["Inventory"]["0"]['id']
            user_Inventory1 = user_data[f"{user_id}"]["Inventory"]["1"]['id']
            user_Inventory2 = user_data[f"{user_id}"]["Inventory"]["2"]['id']
            user_Inventory3 = user_data[f"{user_id}"]["Inventory"]["3"]['id']
            user_Inventory4 = user_data[f"{user_id}"]["Inventory"]["4"]['id']
            user_Inventory5 = user_data[f"{user_id}"]["Inventory"]["5"]['id']
            user_Inventory6 = user_data[f"{user_id}"]["Inventory"]["6"]['id']
            user_Inventory7 = user_data[f"{user_id}"]["Inventory"]["7"]['id']
            user_Inventory8 = user_data[f"{user_id}"]["Inventory"]["8"]['id']
            user_Inventory9 = user_data[f"{user_id}"]["Inventory"]["9"]['id']
            

            embed = discord.Embed(color= 0xfbb907)
            embed.set_author(name="희망봇 인벤토리 1/3", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.set_thumbnail(url=ctx.author.avatar_url)

            embed.add_field(name="레벨", value=f'``{user_data[f"{user_id}"]["levels"]}``', inline=True)
            embed.add_field(name="경험치", value=f'``{user_data[f"{user_id}"]["exp"]}``', inline=True)
            embed.add_field(name="공격력", value=f'``{user_data[f"{user_id}"]["atk"]}``', inline=True)
            embed.add_field(name="방어력", value=f'``{user_data[f"{user_id}"]["def"]}``', inline=True)
            embed.add_field(name="HP", value=f'``{user_data[f"{user_id}"]["hp"]}``', inline=True)

            embed.add_field(name="돈:moneybag:", value=f'``{user_data[f"{user_id}"]["money"]}``', inline=True)

            embed.add_field(name="무기", value=f'``{item_data[f"{user_weapon}"]["name"]}``', inline=True)
            embed.add_field(name="갑옷", value=f'``{item_data[f"{user_armor}"]["name"]}``', inline=True)
            embed.add_field(name="토템", value=f'``{item_data[f"{user_totem}"]["name"]}``', inline=True)
            embed.add_field(name="보조무기", value=f'``{item_data[f"{user_secondary_weapon}"]["name"]}``', inline=True)

            Inventoryembed = discord.Embed(color= 0xfbb907)
            Inventoryembed.set_author(name="희망봇 인벤토리 2/3", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            Inventoryembed.set_thumbnail(url=ctx.author.avatar_url)
            Inventoryembed.add_field(name="인벤토리:pouch:", value="--------------------------------", inline=False)
            Inventoryembed.add_field(name="0", value=f'``{item_data[f"{user_Inventory0}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="1", value=f'``{item_data[f"{user_Inventory1}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="2", value=f'``{item_data[f"{user_Inventory2}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="3", value=f'``{item_data[f"{user_Inventory3}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="4", value=f'``{item_data[f"{user_Inventory4}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="5", value=f'``{item_data[f"{user_Inventory5}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="6", value=f'``{item_data[f"{user_Inventory6}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="7", value=f'``{item_data[f"{user_Inventory7}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="8", value=f'``{item_data[f"{user_Inventory8}"]["name"]}``', inline=True)
            Inventoryembed.add_field(name="9", value=f'``{item_data[f"{user_Inventory9}"]["name"]}``', inline=True)

            fishembed = discord.Embed(color= 0xfbb907)
            fishembed.set_author(name="희망봇 인벤토리 3/3", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            fishembed.set_thumbnail(url=ctx.author.avatar_url)
            fishembed.add_field(name="낚시:fish:", value="--------------------------------", inline=False)
            fishembed.add_field(name="연어", value=f'``{user_data[f"{user_id}"]["fish"]["salmon"]}``', inline=True)
            fishembed.add_field(name="고등어", value=f'``{user_data[f"{user_id}"]["fish"]["Mackerel"]}``', inline=True)
            fishembed.add_field(name="참치", value=f'``{user_data[f"{user_id}"]["fish"]["tuna"]}``', inline=True)
            fishembed.add_field(name="대구", value=f'``{user_data[f"{user_id}"]["fish"]["cod"]}``', inline=True)
            fishembed.add_field(name="희동가리", value=f'``{user_data[f"{user_id}"]["fish"]["Clownfish"]}``', inline=True)
            fishembed.add_field(name="금붕어", value=f'``{user_data[f"{user_id}"]["fish"]["goldfish"]}``', inline=True)

            msg = await ctx.channel.send(embed=embed)

            await msg.add_reaction('◀️')
            await msg.add_reaction('▶️')

            def check(reactin, user):
                return str(reactin) in '◀️', '▶️'  and user == ctx.author and reactin.message.id == msg.id

            page = 0

            while True:

                try:
                    reactin, _user = await self.bot.wait_for(event='reaction_add', timeout=15.0, check=check)

                except asyncio.TimeoutError:
                    break

                else:
                    if str(reactin) == '◀️':
                        if page == 1:
                            page = 3
                        else:
                            page -= 1

                        if page == 1:
                            await msg.edit(embed=embed)
                        elif page == 2:
                            await msg.edit(embed=Inventoryembed)
                        elif page == 3:
                            await msg.edit(embed=fishembed)

                        await msg.remove_reaction('◀️', _user)

                    elif str(reactin) == '▶️':
                        if page == 3:
                            page = 1
                        else:
                            page += 1

                        if page == 1:
                            await msg.edit(embed=embed)
                        elif page == 2:
                            await msg.edit(embed=Inventoryembed)
                        elif page == 3:
                            await msg.edit(embed=fishembed)

                        await msg.remove_reaction('▶️', _user)
                        
        else:
            embed = discord.Embed(color= 0xec4747)
            embed.add_field(name="이런", value="가입이 안돼있네요 희망봇 가입을 쳐보세요!", inline=True)
            await ctx.channel.send(embed=embed)

    @commands.command(name='낚시상점', arg='(판매 또는 구매) (물고기) (물고기수)')
    async def fishing_shop(self, ctx, fish, poor_fish:int):

        with open('user.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        user_id = ctx.author.id

        if f'{user_id}' in user_data:

            if fish == "연어":
                fish = "salmon"
                Sale_Price = 150
            elif fish == "고등어":
                fish = "Mackerel"
                Sale_Price = 100
            elif fish == "참치":
                fish = "tuna"
                Sale_Price = 200
            elif fish == "대구":
                fish = "cod"
                Sale_Price = 100
            elif fish == "희동가리":
                fish = "Clownfish"
                Sale_Price = 100
            elif fish == "금붕어":
                fish = "goldfish"
                Sale_Price = 50
            else:
                embed = discord.Embed(color= 0xec4747)
                embed.set_author(name="희망봇 낚시상점", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                embed.add_field(name="흠", value="그런 물고기는 안사요 NAGA!", inline=True)
                await ctx.channel.send(embed=embed)
                return

            if poor_fish > user_data[f"{user_id}"]["fish"][f"{fish}"]:
                embed = discord.Embed(color= 0xec4747)
                embed.set_author(name="희망봇 낚시상점", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                embed.add_field(name="흠", value="물고기가 그만큼 업잖아요", inline=True)
                await ctx.channel.send(embed=embed)

            elif poor_fish <= 0:
                embed = discord.Embed(color= 0xec4747)
                embed.add_field(name="흠", value="물고기가 없는데요?", inline=True)
                await ctx.channel.send(embed=embed)

            else:
                user_data[f"{user_id}"]["fish"][f"{fish}"] -= poor_fish
                poor_fish *= Sale_Price
                user_data[f"{user_id}"]["money"] += poor_fish
                embed = discord.Embed(color= 0xfbb907)
                embed.add_field(name="굿", value=f'잔액요:`{user_data[f"{user_id}"]["money"]}`', inline=True)
                await ctx.channel.send(embed=embed)

                with open('user.json', 'w', encoding='utf-8') as f2:
                    json.dump(user_data , f2, indent="\t")

        else:
            embed = discord.Embed(color= 0xec4747)
            embed.add_field(name="이런", value="가입이 안돼있네요 희망봇 가입을 쳐보세요!", inline=True)
            await ctx.channel.send(embed=embed)