import discord
from discord.ext import commands

# Set up bot with required intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content for reading replies
intents.dm_messages = True  # Enable DM handling (optional, if you want this in DMs too)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message is a reply to another message
    if message.reference and message.reference.message_id:
        try:
            # Fetch the original message that was replied to
            original_message = await message.channel.fetch_message(message.reference.message_id)
            # Display the content of the replied-to message
            await message.channel.send(f"You replied to: {original_message.content}")
        except discord.NotFound:
            await message.channel.send("Couldn't find the original message.")
    
    await bot.process_commands(message)  # Ensures commands are processed

# Run the bot with your bot token
from Example.Bot_token import Token
bot.run(Token)
