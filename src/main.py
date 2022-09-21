import random

from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv(dotenv_path="../config")
os.getenv("TOKEN")

general_chan = 1022194900982308977 # The chan on witch you want your bot to write on

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
    general_channel = client.get_channel(general_chan)
    await general_channel.send(ctx.author)
    print(ctx.author)

@client.command(name="d6")
async def name_back(ctx):
    """
    When you do "!6" command, return a value between 1 and 6
    :param ctx:
    :return:
    """
    result = random.randint(1, 6)
    general_channel = client.get_channel(general_chan)
    await general_channel.send("The result of your d6 is " + str(result) + " Dr.Freeman")
    return result

client.run(os.getenv("TOKEN"))  # Starts the bot