import requests
import discord
import os
from discord.ext import commands
from deep_translator import GoogleTranslator
from credits import bot_token
from random import choice, randint

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def show(ctx):
    await ctx.send('Бот умеет выдавать ответы по тематикам!' + '\n' + '$mem - случайный мем' + '\n' + '$fox - случайное фото лисы' + '\n' + '$author - авторский мем' + '\n' + '$anime - случайное название аниме')


def get_img():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


def get_anime():
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokio'
    res = requests.get(url)
    data = res.json()
    path = data['data'][randint(0, 5)]['attributes']['titles']['en_jp']
    title_ru = GoogleTranslator(source='auto', target='ru').translate(path)
    return title_ru


@bot.command()
async def fox(ctx):
    fox_image = get_img()
    await ctx.send(fox_image)


@bot.command()
async def anime(ctx):
    anime_link = get_anime()
    await ctx.send(anime_link)
    


@bot.command()
async def mem(ctx):
    image = choice(os.listdir('images'))
    with open(f'images/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def author(ctx):
    with open('images/my-meme.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(bot_token)
