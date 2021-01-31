from bets import Bookie
import discord
import os
from funcs import *

HELLO = ("!hello")
RUMBLE = ("!rumble")
TOBYCLIP = ("!tobyclip")
RUMBLE_WINNER = ("!win_rumble")
START_BANK = ("!start_bank")
BANK = ("!bank")
MY_FUNDS = ("!my_funds")
GRANT_FUNDS = ("!grant_funds")


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# get authorized channels from env config, for use with specific restricted commands
bot_channels = [int(c) for c in os.getenv('BOT_CHANNELS').split()]
# environment variables
token = os.getenv('TOKEN')
admin = os.getenv('ADMIN')
currency = os.getenv('CURRENCY')

bookie = Bookie()
bookie.initialize()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    

@client.event
async def on_message(message, bookie = bookie, admin = admin, currency = currency):
    if message.author == client.user:
        return

    # process HELLO command
    if message.content.lower().startswith(HELLO):
        await message.channel.send(f"Hello {message.author.name}!")

    # process RUMBLE command
    elif message.content.lower().startswith(RUMBLE):
        if message.channel.id not in bot_channels:
            await message.channel.send("That command can only be used from authorized channels <:cena_blep:695734225885855866>")
            return

        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        if message.author.name != admin:
            await message.channel.send(f'Only {admin} can issue this command.')

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

    # process MY_FUNDS command
    if message.content.lower().startswith(MY_FUNDS.lower()):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        channel = voice.channel
        author_name = message.author.name

        current_funds = bookie.get_member_funds(author_name)

        send_message = f'{author_name}, your current funds are {current_funds} {currency}.'
        await message.channel.send(send_message)

    # process START_BANK command
    if message.content.lower().startswith(START_BANK.lower()):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        if message.author.name != admin:
            await message.channel.send(f'Only {admin} can issue this command.')

        channel = voice.channel
        member_names = list(m.name for m in channel.members)
        # config starting fund
        welcome_fund = 200

        await message.channel.send('---BANK REPORT---')
        for name in member_names:
            bookie.check_member_funds_exist(name, welcome_fund)

        await message.channel.send(f'All new members now have {welcome_fund} {currency}.  (Old members still have what they did before.)')
        await message.channel.send('Use !bank at any time to get the current BANK REPORT or use !my_funds to see what you currently have in the bank.')

    # process BANK command
    if message.content.lower().startswith(BANK.lower()):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        channel = voice.channel
        author_name = message.author.name

        if bookie.bank_dict == {}:
            await message.channel.send('The bank is currently empty.  Use !start_bank to give everyone in the voice channel their starting funds.')
            return
        
        await message.channel.send('---BANK REPORT---')
        for k,v in bookie.bank_dict.items():
            
            send_message = f'{k} has {v} {currency}.'
            await message.channel.send(send_message)
            
    # process GRANT_FUNDS command
    if message.content.lower().startswith(GRANT_FUNDS.lower()):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        if message.author.name != admin:
            await message.channel.send(f'Only {admin} can issue this command.')

        if message.content == GRANT_FUNDS.lower():
            await message.channel.send(f'Please provide a winner, e.g. "{GRANT_FUNDS.lower()} Soniv" (case-sensitive)')
            return
        message_params = message.content.replace(GRANT_FUNDS.lower() + ' ', '')

        if len(message_params.split(' ')) != 2:
            await message.channel.send(f'Please provide 2 parameters - the person getting funds and the amount the receive, e.g. "{GRANT_FUNDS.lower()} Soniv 50" (case-sensitive)')
            return

        target_name = message_params.split(' ')[0]
        try:
            new_funds = int(message_params.split(' ')[1])
        except:
            await message.channel.send('Invalid fund amount, must be a number (positive or negative).')
            new_funds = 0

        bookie.update_member_funds(target_name, new_funds)
        
    # process RUMBLE_WINNER command
    if message.content.lower().startswith(RUMBLE_WINNER.lower()):
        voice = message.author.voice
        if(voice is None):
            await message.channel.send("You must be in a voice channel to use that command <:kurt_thumbs_down:695734225458167900>")
            return

        if message.author.name != admin:
            await message.channel.send(f'Only {admin} can issue this command.')

        channel = voice.channel
        author_name = message.author.name

        if message.content == RUMBLE_WINNER.lower():
            await message.channel.send(f'Please provide a winner, e.g. "{RUMBLE_WINNER.lower()} Soniv" (case-sensitive)')
            return
        winner = message.content.replace(RUMBLE_WINNER.lower() + ' ', '')
        # config rumble winner prize
        reward = 500

        bookie.reward_winners([winner], reward)

        await message.channel.send(f'{winner} is the winner and gets {reward} {currency} for a total of {bookie.bank_dict.get(winner)} {currency}!')

client.run(token)