from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv(dotenv_path="../config")
os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

client.author_id = 436535678185111553  # Change to your discord id

@client.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(client.user)  # Prints the bot's username and identifier

@client.command(name="name")
async def name_back(ctx):
    """
    When you do "!name" command, return the name of whom write the command
    :param ctx:
    :return:
    """
    general_channel = client.get_channel(1022194900982308977)
    await general_channel.send(ctx.author)
    print(ctx.author)


client.run(os.getenv("TOKEN"))  # Starts the bot