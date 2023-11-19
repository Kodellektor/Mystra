import discord
from discord.ext import commands
import random
from random import randint, sample
import os
from dotenv import load_dotenv

load_dotenv()
CHANNEL = int(os.getenv('CHANNEL_ID'))

client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('Mystra returns from the beyond!')
    welcome = await client.fetch_channel(CHANNEL)
    await welcome.send('Mystra returns from the beyond!')

@client.command(aliases = ['shutdown', 'kick', 'close', 'quit'])
async def banish(ctx):
    await ctx.send(f'{ctx.author.display_name} has banished Mystra')
    await client.close()

@client.command()
async def roll(ctx, dice: str):
    
    """ Outputs the roll (number of dice | d | dicefaces/dicetype in NdN format)
    As of 07/23/2023 I have yet to handle non standard dice ex: 1d3, modifiers or advantage"""
    
    # Viable examples: 4d6, 2d20, 1d12 
    
    try:
        numdie, dietype = map(int, dice.split('d'))
        
    except Exception: #Being lazy on this until I take time to narrow and figure exact errors
        await ctx.send('Please retry your request in the format NdN!')
        return

    result = ', '.join(str(random.randint(1, dietype)) for n in range(numdie))
    await ctx.send(f'Fate has granted you: {result}')

@client.command()
async def encounter(ctx, partystrength: str, difficulty: str):
    
    """Creates an encounter based on party size and level at the difficulty chosen"""
    pass

@client.command()
async def loot(ctx):
    pass






client.run(os.getenv('DISCORD_TOKEN'))