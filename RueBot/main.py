from enum import member

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import openai




welcome_mssg = ["Welcome in buzz", "Type shi", "Them candied bxs"]
roles = ["test1", "test2", "test3", "test4", "test5", "test6", "test7"]
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
opai_token = os.getenv("OPENAI_TOKEN")
openai.api_key = opai_token

handler = logging.FileHandler(filename='log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = True
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
async def skrrt(ctx):
    quit()




@bot.command()
async def imagine(ctx, *, prompt):
    await ctx.send("Getting dat for you...")

    try:
        response = openai.images.generate(
            model = "gpt-image-1",
            prompt = prompt,
            size='1024x1024'
        )

        image_base64 = response.data[0].b64_json

        import base64
        with open("image.png", "wb") as f:
            f.write(base64.b64decode(image_base64))

        await ctx.send(file=discord.File("image.png"))

    except Exception as e:
        await ctx.send(f"Something went wrong. {e}")



bot.run(token, log_handler = handler, log_level = logging.DEBUG)