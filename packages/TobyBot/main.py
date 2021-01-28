import discord
import os
from funcs import *

HELLO = ("!hello")
RUMBLE = ("!rumble")

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
    if message.content.lower().startswith(HELLO.lower()):
        await message.channel.send(f"Hello {message.author.name}!")

    # process RUMBLE command
    if message.content.lower().startswith(RUMBLE.lower()):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        channel = voice.channel
        member_names = list(m.name for m in channel.members)
        num_entrants = 30
        
        rumble = assign_rumble(member_names, num_entrants)
        send_message = f"You are in {channel}. Hello {', '.join(member_names)}. \n"
        for r in rumble:
            send_message += f"{r['name']} your numbers are: {', '.join(str(n) for n in r['numbers'])}\n"
        await message.channel.send(send_message)

client.run(os.getenv('TOKEN'))