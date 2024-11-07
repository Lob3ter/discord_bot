import discord
from discord.ext import commands
from List import warming
import random
from List import solutions
from List import command_help
from List import consequences_random
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

@bot.command()
async def consequences(ctx):
    await ctx.send(random.choice(consequences_random))

@bot.command()
async def statistic(ctx):
    await ctx.send("По оценкам, средняя глобальная температура за последний 10-летний период, с 2014 по 2023 год, будет самой теплой за всю историю наблюдений: примерно на 1,2 °C выше средней температуры 1850–1900 годов (ВМО). Среднее 20-летнее потепление за 2001–2020 годы по сравнению с 1850–1900 годами составляет 0,99 °C (МГЭИК).")

    

         





bot.run("")
