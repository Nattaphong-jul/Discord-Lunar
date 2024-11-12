import discord
from discord.ext import commands

# Set up bot prefix and intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure this is enabled for sending and receiving messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command to send a DM to the command author
@bot.command()
async def send_dm(ctx, *, message: str):
    try:
        await ctx.author.send(message)
        await ctx.send("DM sent successfully!")
    except discord.Forbidden:
        await ctx.send("I can't send a DM to this user. They may have DMs disabled.")

# Command to send a DM to a specific user
@bot.command()
async def dm_user(ctx, user: discord.User, *, message: str):
    try:
        await user.send(message)
        await ctx.send(f"DM sent to {user.name}!")
    except discord.Forbidden:
        await ctx.send("I can't send a DM to this user. They may have DMs disabled.")

# Run the bot with your bot token
from Bot_token import Token
bot.run(Token)
