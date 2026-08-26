import discord
from discord.ext import commands

# СЮДА ВСТАВЛЯЕШЬ СВОЙ ТОКЕН
TOKEN = 'ВАШ_ТОКЕН_БОТА'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} готов!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет, {ctx.author.mention}!')

bot.run(TOKEN)