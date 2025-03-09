# import discord
# from discord.ext import commands, tasks
# import asyncio
# from datetime import datetime, timedelta

# intents = discord.Intents.default()
# intents.message_content = True  # Enable message content for reading replies
# intents.dm_messages = True  # Enable DM handling (optional, if you want this in DMs too)

# bot = commands.Bot(command_prefix="!", intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user}')

# # Simple command to set a reminder for a specific time (in seconds)
# @bot.command()
# async def remind(ctx, seconds: int, *, reminder_message: str):
#     await ctx.send(f"Reminder set for {seconds} seconds!")
#     await asyncio.sleep(seconds)
#     await ctx.send(f"⏰ Reminder: {reminder_message}")

# # Function to send a daily message at a specific time
# async def daily_message(channel_id, time_of_day):
#     while True:
#         # Calculate the time difference until the specified time of day
#         now = datetime.now()
#         target_time = datetime.combine(now.date(), time_of_day)
#         if now > target_time:
#             target_time += timedelta(days=1)
        
#         await asyncio.sleep((target_time - now).total_seconds())
        
#         # Send message in the specified channel
#         channel = bot.get_channel(channel_id)
#         if channel:
#             await channel.send("Good morning! Here’s your daily update.")  # Customize your message

# @bot.command()
# async def start_daily(ctx):
#     # Start the daily message for a specific channel at 8:00 AM
#     bot.loop.create_task(daily_message(ctx.channel.id, datetime.strptime("14:14", "%H:%M").time()))
#     await ctx.send("Daily messages started at 14:14 AM.")

# # Run the bot with your bot token

# bot.run(Token)
