import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


lixo_info = {
    "garrafa pet": "Reciclar\nDica: Pode virar vaso ou porta-lápis!",
    "papel": "Reciclar\nDica: Use como rascunho antes de jogar fora.",
    "vidro": "Reciclar\nDica: Muito cuidado ao descartar!",
    "resto de comida": "🗑️ Orgânico\nDica: Pode virar adubo (compostagem).",
    "lata": "Reciclar\nDica: Alumínio é muito valioso na reciclagem!",
    "celular ou computador": "Reciclar\nDica: Lixos eletrônicos voltam para indúsria.",
    "bateria": "Reciclar\nDica: Lixos eletrônicos voltam para indúsria.",
    "papel": "Reciclar\nDica: Use como rascunho antes de jogar fora.",
    "tecidos": "Reciclar\nDica: Pode ser reutilizado em artesanato.",
    " vidros": "Reciclar\nDica: Muito cuidado ao descartar!Pois pode ser perigoso para quem manuseia u vidro quebrado."
}

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def lixo(ctx, *, item: str):
    item = item.lower()

    if item in lixo_info:
        await ctx.send(f"🔍 Resultado para '{item}':\n{lixo_info[item]}")
    else:
        await ctx.send("❓ Não sei sobre esse item ainda... tente outro!")

# Coloque seu token aqui
bot.run("-------")
