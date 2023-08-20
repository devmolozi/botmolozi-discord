import discord
from discord.ext import commands
from keep_alive import keep_alive
import asyncio

import clearchat

cogs = [clearchat]

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(bot)

discord_token = 'MTE0MTQxODM4Mjk5MDc4NjY4MQ.Gu3qPR.xtj-mtWF9wYdhj5Ok3FrlKR4w2DSFZZ1j9Eri4'


# BOT ATIVO

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

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
