import discord
from discord.ext import commands
import dc_bot_token
import random

mekanlar = ["sahil","kendi evin","bahçe"]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def helpme(ctx):
    await ctx.send("""
!temizlik
!hangi_yeri_temizlicem
             """)

@bot.command()
async def temizlik(ctx):
   await ctx.send("""
Temizlik çok önemli!
Çevreyi temiz tutmaya özen göster eğer nereyi temizleyiceğini bilmiyorsan
!hangi_yeri_temizlicem komudunu kullan.
             """)
@bot.command()
async def hangi_yeri_temizlicem(ctx):
    await ctx.send(random.choice(mekanlar))

bot.run(dc_bot_token.bot_token)