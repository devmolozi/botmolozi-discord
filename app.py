import discord
from discord.ext import commands
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

discord_token = 'MTE0MTQxODM4Mjk5MDc4NjY4MQ.GzHDCp.DfclVJ7hhx6cyhG3ffSPzO0WHbNaQ89L6mP9cQ'



@bot.command()
async def inverse(ctx, message):
    await ctx.send(message[::-1]) 


keep_alive()
bot.run(discord_token)