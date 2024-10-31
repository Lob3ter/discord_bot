import discord
from discord.ext import commands
from List import warming
import random
from List import solutions
from List import command_help
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)



@bot.command()
async def help_tybute(ctx):
    await ctx.send(command_help)

@bot.command()
async def global_warming(ctx):
    await ctx.send(random.choice(warming))

@bot.command()
async def solutions_(ctx):
    await ctx.send(random.choice(solutions))




bot.run()
