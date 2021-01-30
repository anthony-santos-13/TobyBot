import discord
import os
from funcs import *

HELLO = ("!hello")
RUMBLE = ("!rumble")
TOBYCLIP = ("!tobyclip")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # process HELLO command
    if message.content.lower().startswith(HELLO):
        await message.channel.send(f"Hello {message.author.name}!")

    # process RUMBLE command
    elif message.content.lower().startswith(RUMBLE):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        channel = voice.channel
        await message.channel.send(f"Hello {channel}, it's time for a ROYAL RUMBLE match!")

        members = channel.members
        num_entrants = 30
        
        messages = assign_rumble(members, num_entrants)
        [await message.channel.send(m) for m in messages]
        
    # process TOBYCLIP command
    elif message.content.lower().startswith(TOBYCLIP):
        clip = get_toby_clip()

        await message.channel.send(f"Here's a cool TobyStamkos clip: {clip}")

client.run(os.getenv('TOKEN'))