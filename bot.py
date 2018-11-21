from discord.ext import commands
import discord
import os
import logging

logging.basicConfig(level='INFO')

bot = commands.Bot(command_prefix="?", description="help")
@bot.event
async def on_ready():
  print('Im ready!')
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send('User has been banned.')
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send('User has been kicked.')
   

@bot.command()
async def invite(ctx,):
  await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=512866748165390348&scope=bot&permissions=268575766')

@bot.command()
async def send(ctx, *sendit):
    count = 0
    if not "PRMS" in [x.name for x in ctx.author.roles]:
       await ctx.send('This command is not for you')
       return
    users = [x.id for x in ctx.guild.members]
    for x in users:
        try:
            await bot.get_user(x).send(' '.join(sendit))
        except discord.Forbidden:
            count += 1
    await ctx.send(f'Sent this message for {ctx.guild.members-count} / {ctx.guild.members} users')
@bot.command()
async def gen(ctx):
    guild = ctx.guild
    await guild.create_role(name="PRMS")
    
bot.load_extension('libneko.extras.help')
bot.run(os.environ.get('TOKEN'))
