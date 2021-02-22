import discord
import os
from funcs import *

HELLO = ("!hello")
RUMBLE = ("!rumble")
TOBYCLIP = ("!tobyclip")
POLL = ("!poll")
WHAT = ("!what")
HELP = ("!help")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# get authorized channels from env config, for use with specific restricted commands
bot_channels = [int(c) for c in os.getenv('BOT_CHANNELS').split()]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # process HELP command
    if message.content.lower().startswith(HELP):
        help_text = get_help_text()
        await message.channel.send(help_text)

    # process HELLO command
    elif message.content.lower().startswith(HELLO):
        await message.channel.send(f"Hello {message.author.name}!")

    # process RUMBLE command
    elif message.content.lower().startswith(RUMBLE):
        await message.channel.send("Today is not the day to rumble! <:sting_unimpressed:696005929241542687>")
        return

        if message.channel.id not in bot_channels:
            await message.channel.send("That command can only be used from authorized channels <:cena_blep:695734225885855866>")
            return

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

    # process POLL command
    elif message.content.lower().startswith(POLL):
        if message.channel.id not in bot_channels:
            await message.channel.send("That command can only be used from authorized channels <:cena_blep:695734225885855866>")
            return

        message_content = message.clean_content

        poll_message,  poll_labels = create_poll(message_content)
        
        sent_message = await message.channel.send(poll_message)

        for p in poll_labels:
            await sent_message.add_reaction(p)
        
    # process TOBYCLIP command
    elif message.content.lower().startswith(TOBYCLIP):
        clip = get_toby_clip()

        await message.channel.send(f"Here's a cool TobyStamkos clip: {clip}")

    # process WHAT command
    elif message.content.lower().startswith(WHAT):
        what = get_what()
        await message.channel.send(f"{what} WHAT?")

    # display error if ! is used and not recognized
    elif message.content.lower().startswith("!"):
        await message.channel.send(f"Command not recognized, type !help for a list of supported commands.")

client.run(os.getenv('TOKEN'))