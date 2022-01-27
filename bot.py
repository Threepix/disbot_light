import discord, random

from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.event
async def on_ready():  
    print('Bot connected successfully!')



@bot.command()
async def randoms(ctx, arg):
    try:
        a = random.randint(0, int(arg))
    except:
        await ctx.send(f'Ошибка')
        return
    await ctx.send(f'Ваше случайное число: {a}')



@bot.command()
async def menu(ctx):
    embed = discord.Embed(color=0xff9900, title='Help menu')
    embed.add_field(name='hello', value='bot say you hi!', inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def repeat(ctx, arg):

bot.run(settings['token'])