import secondary
import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def save(ctx, tag):
    Rlist = await verify_account(ctx.author, tag)
    value = Rlist[0]
    users = Rlist[1]
    if value == "yes":
        embed = discord.Embed(color=discord.Color.dark_purple())
        embed.set_author(name="Exception In Command")
        embed.add_field(name="Error", value="Account already registered. Type $remove to remove your brawl stars account.")
        await ctx.send(embed=embed)
    if value == "no":
        try:
            player = secondary.get_info(tag)
            rank = secondary.get_rank(player.trophies)
            with open("data.json", "w") as f:
                json.dump(users, f)
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Command Successful")
            embed.add_field(name="Added Account.", value=f"Successfully added account {rank[1]} | {player.name} ")
            await ctx.send(embed=embed)
        except:
            await ctx.send("Not A Valid Account")

async def verify_account(user, tag):
    with open("data.json", "r") as f:
        users = json.load(f)
    if str(user.id) in users:
        value = "yes"
    else:
        users[str(user.id)] = tag
        value = "no"
    return value, users

@bot.command()
async def remove(ctx):
    with open("data.json","r") as f:
        users = json.load(f)
    if str(ctx.author.id) in users:
        profile = secondary.get_info(users[str(ctx.author.id)])
        users.pop(str(ctx.author.id))
        with open("data.json", "w") as f:
            json.dump(users, f)
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name="Command Successful")
        embed.add_field(name="Account Removed.", value=f"Successfully removed account {profile.name}")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=discord.Color.dark_purple())
        embed.set_author(name="Exception In Command")
        embed.add_field(name="Error", value="Account not registered. $save #<tag> to save your brawl stars account.")
        await ctx.send(embed=embed)

@bot.command()
async def profile(ctx):
    with open("data.json","r") as f:
        users = json.load(f)
    if str(ctx.author.id) in users:
        tag = users[str(ctx.author.id)]
        profile_info = secondary.get_info(tag)
        rank = secondary.get_rank(profile_info.trophies)
        imageid = secondary.get_logo(tag)
        if profile_info.is_qualified_from_championship_challenge == True:
            qual = "True"
        else:
            qual = "False"
        try:
            club = profile_info.club.name
        except:
            club = "Not in a club"
        brawlers = profile_info.brawlers
        top_brawler = brawlers[0]
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name=f" ~| Brawl Stars |~")
        embed.set_thumbnail(url=f"https://cdn.brawlstats.com/player-thumbnails/{imageid}.png")
        embed.add_field(name="Username: ", value=f"{rank[1]} | {profile_info.name}")
        embed.add_field(name="Tag:", value=f"{tag}")
        embed.add_field(name="Trophy Road Rank:", value=f"{rank[1]} | {rank[0]}")
        embed.add_field(name="Trophies:", value=f"{profile_info.trophies} <:Trophy:854606907439710218>")
        embed.add_field(name="Highest Trophies: ", value=f"{profile_info.highest_trophies} <:Trophy:854606907439710218>")
        embed.add_field(name="Exp Level: ", value=f"<:Exp:854978177386283028> {profile_info.exp_level}")
        embed.add_field(name="Club: ", value=f"<:Club:855027618448801805> {club}")
        embed.add_field(name="Qualified For Championship Challenge: ", value=f"<:ChampionshipChallenge:855020961401536532> {qual}")
        await ctx.send(embed=embed)
        second = discord.Embed(color=discord.Color.dark_red())
        second.set_author(name='Brawl Matches')
        second.add_field(name='3v3 Victories:', value=f"<:3v3:855020737445625887> {profile_info.x3vs3_victories}")
        second.add_field(name="Team Victories:", value=f"<:3v3:855020737445625887> {profile_info.team_victories}")
        second.add_field(name="Solo Victories:", value=f"<:SoloShowdown:855020872027734016> {profile_info.solo_victories}")
        second.add_field(name="Duo Victories:", value=f"<:DuoShowdown:855020811630018571> {profile_info.duo_victories}")
        second.add_field(name="Best Robo Rumble Time:", value=f"<:Robo_Rumble:855021062302334987> {profile_info.best_robo_rumble_time}")
        second.add_field(name="Best Time As Big Brawler:", value=f"<:Big_Game:855020746894737408> {profile_info.best_time_as_big_brawler}")
        await ctx.send(embed=second)
    else:
        embed = discord.Embed(color=discord.Color.dark_purple())
        embed.set_author(name="Exception In Command")
        embed.add_field(name="Error", value="Account not registered. $save #<tag> to save your brawl stars account.")
        await ctx.send(embed=embed)

bot.run("ODU0MDM0NTk2NTM3NDM0MTcy.YMeDsw.1ITIfnTMwHB-JaoGdEvpsUZYJZ0")