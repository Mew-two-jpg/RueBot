from enum import member

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

welcome_mssg = ["Welcome in buzz", "Type shi", "Them candied bxs"]

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name}, is ready for liftoff!")
@bot.event
async def on_member_join(member):
    await member.send(random.choice(welcome_mssg))

@bot.command()
async def candiedbx(ctx):
    await ctx.send(file = discord.File('candiedbx.jpg'))

@bot.command()
async def skrill(ctx):
    await ctx.send("https://skin.club/en")

@bot.command()
async def skrrt():
    quit()




bot.run(token, log_handler = handler, log_level = logging.DEBUG)