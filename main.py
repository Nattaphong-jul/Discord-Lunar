from discord.ext import commands
import discord
import random
from discord import channel, voice_client
from discord import FFmpegPCMAudio
import time
from datetime import datetime
import pandas as pd
import csv
import qrcode

Token = 'MTI5MzU5MjkxOTM1NzUyMjAzMQ.GE9NAe.FJUVqJu8NM22ofLVAZL0TNHZtiTXpjZ_th2ed4'
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = commands.Bot(command_prefix= "-", intents=intents)

def write_log(message, sender, server, channel, userID):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")  # Format the date as YYYY-MM-DD
    time = now.strftime("%H:%M:%S")  # Format the time as HH:MM:SS
    
    # Open the CSV file in append mode ('a')
    with open('log.csv', mode='a', newline='', encoding="utf-8") as file: # encoding="utf-8" for Thai language
        writer = csv.writer(file)

        # Write a row with date, time, server ,sender, and message
        writer.writerow([date, time, server, channel, userID, sender, message])

sheet_id = "1kMtrvjDKAevBPcBitv2b8u7m0yxANfuC19XNSp-01Xc"
sheet_name = "Log_Example"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
def language_change(text):
  df = pd.read_csv(url)
  converted = ""
  for i in text:
    try:
        if i in df['Eng'].tolist():
            converted = converted + str(df['Thai'][df['Eng'].tolist().index(i)])
        elif i in df['Shift_Eng'].tolist():
            converted = converted + str(df['Shift_Thai'][df['Shift_Eng'].tolist().index(i)])
        elif i == " ":
            converted = converted + " "
        else:
            converted = converted + i
            
    except:
      continue
  return converted



@client.event
async def on_ready():
    print("Proxima is ready")
    try:
        # Sync the commands with Discord (in case you add new commands)
        
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@client.event
async def on_message(message):
    # Write Log.csv
    message_ = str(message.content)
    author_ = str(message.author)
    userID_ = str(message.author.id)
    if message.guild is None:
        server_ = 'DM'
        channel_ = 'DM'
    else:
        server_ = str(message.guild.name)
        channel_ = str(message.channel.name)
    write_log(message=message_, sender=author_, server=server_, channel=channel_, userID=userID_)

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    await client.process_commands(message)

# Command ---------------------------------------------------------------------------------------------------------

@client.tree.command(name="qr", description="Generate QR-Code from URL")
async def qr(interaction: discord.Interaction, url: str):
    try:
        img = qrcode.make(url)
        img.save('qrcode.png')
        await interaction.response.send_message(file=discord.File('qrcode.png'))
    except:
        await interaction.response.send_message("ทำไม่ได้อ่ะค่ะ ขอโทษด้วยนะคะ:sob:", ephemeral=False)

# import change_language, find_recent_message
# @client.tree.command(name="แปล", description="แก้คำที่ลืมเปลียนภาษา")
# async def แปล(interaction: discord.Interaction):
#         guild_name = interaction.guild.name if interaction.guild else "DM"
#         channel_name = interaction.channel.name if interaction.channel else "DM"
#         await interaction.response.send_message(change_language.language_change(find_recent_message.find_recent(server=guild_name, channel=channel_name)), ephemeral=False)


client.run(Token)