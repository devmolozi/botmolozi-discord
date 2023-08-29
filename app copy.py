import discord
from discord.ext import commands
from keep_alive import keep_alive
import asyncio
import os
import youtube_dl

import clearchat

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_opts = {'options': "-vn"}

cogs = [clearchat]

intents = discord.Intents.all()
client = discord.Client(intents=intents)
intents.message_content = True


bot = commands.Bot(command_prefix='.',  intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(bot)

discord_token = 'MTE0MTQxODM4Mjk5MDc4NjY4MQ.Gu3qPR.xtj-mtWF9wYdhj5Ok3FrlKR4w2DSFZZ1j9Eri4'


# BOT ATIVO

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')



@bot.event
async def on_message(msg):
    if msg.content.startswith("?play"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_opts)

            voice_clients[msg.guild.id].play(player)

        except Exception as err:
            print(err)


    if msg.content.startswith("?pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)

    # This resumes the current song playing if it's been paused
    if msg.content.startswith("?resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)

    # This stops the current playing song
    if msg.content.startswith("?stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)


















@bot.command()
async def clear(ctx, ammount=10):

        ammount = ammount
        if ammount > 100:
            await ctx.send('Você não pode apagar mais de 100 mensagens')
        else:
            await ctx.channel.purge(limit=ammount)
            await ctx.send(f'{ammount} Mensagens apagadas')
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=ammount+0)

# RESPONDER COMANDO============================================================
@bot.command()
async def ola(ctx):
    await ctx.send('Olá seu peba')


@bot.event
async def on_member_join(member):
    canalboasvindass = bot.get_channel(1062907955667796008)
    mesagem = await canalboasvindass.send(f'Seja Bem Vindo(a) {member.mention} !')

@bot.command()
async def link(ctx):
    await ctx.send("""Ajude a divulgar o Servidor pelo link abaixo
                   
https://www.geeksforgeeks.org/reverse-words-given-string-python/""")

# comando==================================================================


@bot.command()
async def inverse(ctx, message):
    await ctx.send(message[::-1])

# 


keep_alive()
bot.run(discord_token)
