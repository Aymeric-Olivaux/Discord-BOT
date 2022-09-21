import random

from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv(dotenv_path="../config")
os.getenv("TOKEN")

general_chan = 1022194900982308977  # The chan on witch you want your bot to write on

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents  # Set up basic permissions
)

client.author_id = 436535678185111553  # Change to your discord id
intents.presences=True

@client.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    general_channel = client.get_channel(general_chan)
    await general_channel.send(client.user)
    print(client.user)  # Prints the bot's username and identifier



@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul")
        await message.channel.send(message.author.mention)


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


@client.command(name="d6")
async def random(ctx):
    """
    When you do "!d6" command, return a value between 1 and 6
    :param ctx:
    :return:
    """
    result = random.randint(1, 6)
    general_channel = client.get_channel(general_chan)
    await general_channel.send("The result of your d6 is " + str(result) + " Dr.Freeman")
    return result


@client.command(name="admin")
async def give_admin(ctx, name: str):
    """
    :param ctx:
    :return:
    """
    user = ctx.message.author
    if discord.utils.get(user.guild.roles, name="admin") == None:
        print("Creating role admin")
        perms = discord.Permissions(administrator=True)
        await ctx.guild.create_role(name="admin", permissions=perms)
    else:
        print("Role admin already exist")
    role = discord.utils.get(user.guild.roles, name="admin")
    await user.add_roles(role)


@client.command(name="ban")
async def ban(ctx, name: str):
    """
    :param ctx:
    :return:
    """
    user = ctx.message.author
    await user.ban(reason=None)


#!count the bot should write back for each possible status (Online, Offline, Idle, Do not disturb) the number of members
#(including yourself) in the server with that status

#Example : "3 members are online, 2 are idle and 4 are off"
#Extra mile : Instead of counting the members, list them sorted by status
@client.command(name="count")
async def count(ctx):
    """
    :param ctx:
    :return:
    """
    members = ctx.guild.members
    online = 0
    idle = 0
    off = 0
    dnd = 0
    for member in members:
        if member.status.name == "online":
            online += 1
        elif member.status.name == "idle":
            idle += 1
        elif member.status.name == "offline":
            off += 1
        elif member.status.name == "dnd":
            dnd += 1

    general_channel = client.get_channel(general_chan)
    await general_channel.send("Dr.Freeman, " + str(online) + " of the citizen's of City 17 are online, " + str(idle) + " are idle, " + str(off) + " are offline and " + str(dnd) + " should not be disturb")


client.run(os.getenv("TOKEN"))  # Starts the bot
