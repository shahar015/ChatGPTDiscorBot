import os
import discord
from discord.ext import commands
import openai
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.dm_messages=True
intents.dm_reactions=True
intents.dm_typing=True
intents.guild_messages=True
intents.guild_typing=True
intents.guild_reactions=True
intents.message_content=True
intents.guilds=True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents, help_command=commands.DefaultHelpCommand())


# Set up OpenAI API key
openai.api_key = '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'

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99')
async def nine_nine(ctx):
    await ctx.send("Hi 909 to you too")

@bot.command(name='chat')
async def generate_text(ctx, *, prompt):
    print("Got The Messege")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    text = response.choices[0].text.strip()
    await ctx.send(text)

@bot.command(name='analyze')
async def analyze_photo(ctx):
    if len(ctx.message.attachments) > 0:
        attachment = ctx.message.attachments[0]
        response = requests.get(attachment.url)
        with open("image.jpg", "wb") as f:
            f.write(response.content)
        question = "What is in this photo?"
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"{question}\nImage:",
            files=[{"file_path": "image.jpg"}],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        text = response.choices[0].text.strip()
        await ctx.send(text)
    else:
        await ctx.send("Please attach a photo to your message.")

bot.run('MTA4NTI5NjI4ODY4NzQ3Njc5OQ.GbrQhB.6sWsD0NoRIgx7w0HHgmLXAjSM5CYxMHWjomRC8')
