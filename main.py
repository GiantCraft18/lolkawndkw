import lolka as discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Залогинились как {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "!ping":
        await message.channel.send("lolka pong! 🏓")
    if message.content == "!lol":
        await message.channel.send("🤡 Лолка тут!")

client.run("ТВОЙ_ТОКЕН_СЮДА")