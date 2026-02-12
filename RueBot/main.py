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
bot = commands.Bot(command_prefix='hey rueben ', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name}, is ready for liftoff!")
@bot.event
async def on_member_join(member):
    await member.send(random.choice(welcome_mssg))

@bot.command()
async def candiedbx(ctx):
    await ctx.send(file = discord.File('ruemages/candiedbx.jpg'))

@bot.command()
async def skrill(ctx):
    await ctx.send("https://skin.club/en")

@bot.command()
async def skrrt(ctx):
    quit()


@bot.event
async def on_message(message):
    import glob

    if message.author == bot.user:
        return

    if 'show me a clip' in message.content.lower():
        videos = glob.glob('ruetoges/*.mp4')
        if videos:
            video_path = random.choice(videos)
            await message.channel.send(file=discord.File(video_path))
        else:
            await message.channel.send("No videos found!")
        return

    # Process other message triggers
    message_lower = message.content.lower()
    word_responses = {
        'candied bxs': ('both', ('got dat for you', 'ruemages/candiedbx.jpg')),
        'wsg': ('text', 'what it do mane'),
        'stuffin her': ('text', 'dats fire :fire:'),
         "see it": ('both',('you see it?', "ruemages/vlone.jpg")),
        "brendan": ('text', 'you mean nigdan?'),
        "big rue": ('text', 'wsg'),
    }

    for word, response_data in word_responses.items():
        if word in message_lower:
            response_type, response_value = response_data

            if response_type == 'both':
                text, image_path = response_value
                await message.channel.send(f"{message.author.mention} {text}", file=discord.File(image_path))
            elif response_type == 'image':
                await message.channel.send(f"{message.author.mention}", file=discord.File(response_value))
            elif response_type == 'text':
                await message.channel.send(f"{message.author.mention} {response_value}")

            break

    # Process commands
    await bot.process_commands(message)

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
        with open("ruemages/image.png", "wb") as f:
            f.write(base64.b64decode(image_base64))

        await ctx.send(file=discord.File("image.png"))

    except Exception as e:
        await ctx.send(f"Something went wrong. {e}")


bot.run(token, log_handler = handler, log_level = logging.DEBUG)
bot.run(token, log_handler = handler, log_level = logging.DEBUG)