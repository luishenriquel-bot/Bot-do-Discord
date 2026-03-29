import asyncio
import os
import discord
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot! Como posso ajudar? {bot.user}!')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command(name="feijão")
async def feijao(ctx):
    await ctx.send("com arroz")

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)


def get_cat_image_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    return data[0]['url']

@bot.command('cat')
async def cat(ctx):
    image_url = get_cat_image_url()
    await ctx.send(image_url)


def get_dog_image_url():
    url = 'https://api.thedogapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    return data[0]['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    import random
    num = random.randint(1, 151)  # primeiros pokémons
    res = requests.get(url + str(num))
    data = res.json()
    
    nome = data['name']
    imagem = data['sprites']['front_default']
    
    return nome, imagem

@bot.command('pokemon')
async def pokemon(ctx):
    nome, imagem = get_pokemon()
    await ctx.send(f'⚡ Pokémon: {nome}')
    await ctx.send(imagem)

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("heh" * count_heh)

@bot.command(name="pão")
async def pao(ctx):
    await ctx.send("com geleia")

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def meme(ctx):
    lista = os.listdir('images')
    img_name = random.choice(lista)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("---------------------")
