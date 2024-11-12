import discord
from discord import app_commands
from discord.ext import commands
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import json

# Discord bot setup with Intents and Sync Command Tree for Slash Commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


# Google API scopes
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Helper functions to save and load credentials
def save_credentials(creds):
    with open("token.json", "w") as token_file:
        token_file.write(creds.to_json())

def load_credentials():
    if os.path.exists("token.json"):
        with open("token.json", "r") as token_file:
            creds_info = json.load(token_file)
            return Credentials.from_authorized_user_info(creds_info, SCOPES)
    return None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        # Sync the commands with Discord (in case you add new commands)
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Load credentials at bot startup
bot.creds = load_credentials()

# Step 1: Slash command to start the authorization process
@bot.tree.command(name="authorize", description="Authorize the bot to access your Google Calendar")
async def authorize(interaction: discord.Interaction):
    """Starts the Google OAuth authorization process."""
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
    )
    flow.redirect_uri = "http://localhost:8080"
    
    auth_url, _ = flow.authorization_url(prompt="consent")
    await interaction.response.send_message(f"Please authorize the app by visiting this URL: {auth_url}")
    
    # Save the flow to retrieve it later in the `/auth` command
    bot.flow = flow

# Step 2: Slash command to complete the authorization with code
@bot.tree.command(name="auth", description="Complete authorization with the code")
@app_commands.describe(auth_code="Authorization code obtained from the URL")
async def auth(interaction: discord.Interaction, auth_code: str):
    """Completes authorization with the provided code."""
    flow = bot.flow
    flow.fetch_token(code=auth_code)

    # Save the credentials
    creds = flow.credentials
    bot.creds = creds
    save_credentials(creds)

    await interaction.response.send_message("Authorization successful! You can now use the `/add_event` command.")

# Step 3: Slash command to add an event to Google Calendar
@bot.tree.command(name="add_event", description="Add an event to Google Calendar")
@app_commands.describe(title="Event title", start_time="Start time (ISO format)", end_time="End time (ISO format)")
async def add_event(interaction: discord.Interaction, title: str, start_time: str, end_time: str):
    """Adds an event to the user's Google Calendar."""
    if not bot.creds:
        await interaction.response.send_message("Please authorize the bot using `/authorize` first.")
        return

    # Initialize the Google Calendar API service
    service = build("calendar", "v3", credentials=bot.creds)

    # Define the event
    event = {
        "summary": title,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }

    # Insert the event
    event_result = service.events().insert(calendarId="primary", body=event).execute()
    await interaction.response.send_message(f"Event created: {event_result.get('htmlLink')}")


# Run the bot with your Discord bot token
Token = 'MTI5MzU5MjkxOTM1NzUyMjAzMQ.GE9NAe.FJUVqJu8NM22ofLVAZL0TNHZtiTXpjZ_th2ed4'
bot.run(Token)
