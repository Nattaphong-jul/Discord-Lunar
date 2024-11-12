import discord
from discord.ext import commands
from PIL import Image
import requests
from io import BytesIO

# Set up bot with required intents
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True  # Enable DM handling

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message has attachments
    if message.attachments:
        for attachment in message.attachments:
            # Check if the attachment is an image
            if attachment.content_type and "image" in attachment.content_type:
                await message.channel.send("Image received! Analyzing...")

                # Download the image for further processing
                image_bytes = await attachment.read()
                
                # Process the image (e.g., with PIL)
                try:
                    image = Image.open(BytesIO(image_bytes))
                    # Example processing: get image size
                    width, height = image.size
                    await message.channel.send(f"Image size: {width}x{height}")
                except Exception as e:
                    await message.channel.send("Couldn't process the image.")
                    print(e)
    
    await bot.process_commands(message)  # Ensures commands are processed

# Run the bot with your bot token
from Example.Bot_token import Token
bot.run(Token)
