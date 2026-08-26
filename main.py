import discord
from discord.ext import commands
import random

TOKEN = 'ТВОЙ_ТОКЕН_СЮДА'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ===== БАЗА ШУТОК И ЦИТАТ =====
shutki = [
    "Лол, ты серьёзно? 🤡",
    "Ахахаха, это было смешно... или нет? 😂",
    "Я бы пошутил, но ты не поймёшь 🤓",
    "Ты как всегда в своём репертуаре 😏",
    "Тупой вопрос — тупой ответ 🤪",
    "Дискорд умер, лол кек",
    "Мой создатель — гений (это я про себя)",
    "Ты думал я отвечу? А вот хер там 😎",
    "Я не бот, я твой внутренний голос 🗿"
]

citaty = [
    "Жизнь — как коробка шоколадных конфет, только вместо конфет — проблемы 🍫",
    "Умные мысли приходят, только когда ты в душе 🚿",
    "Я бы пофилосовствовал, но лень 🤷",
    "Это ты мне? Боже, какой позор 😂"
]

otvety = [
    "Да",
    "Нет",
    "Может быть",
    "Спроси позже",
    "Я знаю, но не скажу 🤫",
    "Это слишком сложно для моего маленького мозга 😵"
]

# ===== СОБЫТИЯ =====
@bot.event
async def on_ready():
    print(f'✅ LOLKA-бот {bot.user} готов!')
    await bot.change_presence(activity=discord.Game(name="!lol или !помощь"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Ответ на "привет" или "ку"
    if message.content.lower() in ['привет', 'ку', 'здарова', 'hi', 'hello']:
        await message.reply(f'Лол, здарова {message.author.mention}! 😎')

    # Ответ на "пока"
    elif message.content.lower() in ['пока', 'by', 'bye', 'покеда']:
        await message.reply('Бывай, лох! 👋')

    # Ответ на "ты бот?"
    elif 'бот' in message.content.lower() and '?' in message.content:
        await message.reply('Я не бот, я твой кошмар во плоти 👻')

    # Обязательно обрабатываем команды
    await bot.process_commands(message)

# ===== КОМАНДЫ =====

# Главная команда — лол
@bot.command()
async def lol(ctx):
    """Случайная шутка"""
    await ctx.send(random.choice(shutki))

# Команда с цитатой
@bot.command()
async def цитата(ctx):
    """Мудрость дня"""
    await ctx.send(random.choice(citaty))

# Команда-предсказание
@bot.command()
async def предскажи(ctx):
    """Ответит на твой вопрос (вопрос задавай в той же команде)"""
    await ctx.send(f'🔮 {random.choice(otvety)}')

# Статус бота
@bot.command()
async def статус(ctx):
    """Показывает задержку"""
    await ctx.send(f'⚡ Пинг: {round(bot.latency * 1000)}мс')

# Помощь
@bot.command()
async def помощь(ctx):
    """Список команд"""
    embed = discord.Embed(title="🤡 LOLKA-бот", color=0xff00ff)
    embed.add_field(name="!lol", value="Случайная шутка", inline=False)
    embed.add_field(name="!цитата", value="Мудрость дня", inline=False)
    embed.add_field(name="!предскажи", value="Ответит на твой вопрос", inline=False)
    embed.add_field(name="!статус", value="Пинг бота", inline=False)
    embed.add_field(name="!помощь", value="Покажет это меню", inline=False)
    embed.set_footer(text="Напиши 'привет' и я отвечу!")
    await ctx.send(embed=embed)

# ===== ЗАПУСК =====
bot.run(TOKEN)