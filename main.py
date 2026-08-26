import discord
from discord.ext import commands
import os

# Берем токен из переменных окружения (Render/Replit сам подставит)
TOKEN = os.getenv('TOKEN')

# Настройки бота (нужно для чтения команд)
intents = discord.Intents.default()
intents.message_content = True

# Создаем бота с префиксом "!"
bot = commands.Bot(command_prefix='!', intents=intents)

# Команда проверки
@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} готов!')

# Команда !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет, {ctx.author.mention}!')

# Запуск
bot.run(TOKEN)