import discord
from discord import app_commands
from discord.ext import commands

Token = 'MTI5MzU5MjkxOTM1NzUyMjAzMQ.GE9NAe.FJUVqJu8NM22ofLVAZL0TNHZtiTXpjZ_th2ed4'

# Define the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# This is called when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        # Sync the commands with Discord (in case you add new commands)
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Slash command example
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! 👋")

# Another slash command with an option
@bot.tree.command(name="addes", description="Add two numbers.")
@app_commands.describe(num1="The first number", num2="The second number")
async def addy(interaction: discord.Interaction, num1: int, num2: int):
    result = num1 + num2
    await interaction.response.send_message(f"The result is: {result}")

# Run the bot with your token
bot.run(Token)
