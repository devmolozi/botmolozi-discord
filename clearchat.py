from discord.ext import commands
import asyncio


class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self,ctx, ammount=10):

        ammount = ammount
        if ammount > 100:
            await ctx.send('Você não pode apagar mais de 100 mensagens')
        else:
            await ctx.channel.purge(limit=ammount+0)
            await ctx.send(f'{ammount} Mensagens apagadas')
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=ammount+0)

def setup(client):
    client.add_cog(ClearCog(client))