from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from the .env file
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

# Create bot instance with intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your product monitor bot. 👋")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_BOT_TOKEN environment variable is not set.")
