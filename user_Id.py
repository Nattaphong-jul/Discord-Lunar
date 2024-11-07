import discord
from discord.ext import commands

# Set up bot with required intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.dm_messages = True       # Enable DM handling

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message is in a DM channel
    if message.guild is None:
        user_id = message.author.id  # Get the user ID of the message sender
        await message.channel.send(f"Your user ID is: {user_id}")
    else:
        user_id = message.author.id  # Get the user ID of the message sender
        await message.channel.send(f"Your user ID is: {user_id}")
    
    await bot.process_commands(message)  # Ensures commands are still processed

# Run the bot with your bot token
from Bot_token import Token
bot.run(Token)
