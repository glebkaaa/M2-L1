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


def common_image():
    global common_picture
    image = choice(os.listdir('images/common'))
    with open(f'images/common/{image}', 'rb') as f:
        common_picture = discord.File(f)


def rare_image():
    global rare_picture
    image = choice(os.listdir('images/rare'))
    with open(f'images/rare/{image}', 'rb') as f:
        rare_picture = discord.File(f)


def epic_image():
    global epic_picture
    image = choice(os.listdir('images/epic'))
    with open(f'images/epic/{image}', 'rb') as f:
        epic_picture = discord.File(f)


def legendary_image():
    global legendary_picture
    image = choice(os.listdir('images/legendary'))
    with open(f'images/legendary/{image}', 'rb') as f:
        legendary_picture = discord.File(f)


@bot.command()
async def show(ctx):
    await ctx.send('Бот умеет выдавать ответы по тематикам!' + '\n' + '$mem - случайный мем' + '\n' + '$fox - случайное фото лисы' + '\n' + '$author - авторский мем' + '\n' + '$anime - случайное название аниме')


@bot.command()
async def fox(ctx):
    fox_image = get_img()
    await ctx.send(fox_image)


@bot.command()
async def anime(ctx):
    anime_link = get_anime()
    await ctx.send(anime_link)


@bot.command()
async def author(ctx):
    with open('images/my-meme.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem(ctx):
    rarity = randint(1, 4)
    if rarity == 1:
        common_image()
        await ctx.send(file=common_picture)
        await ctx.send('Обычный мем')
    elif rarity == 2:
        rare_image()
        await ctx.send(file=rare_picture)
        await ctx.send('Редкий мем')
    elif rarity == 3:
        epic_image()
        await ctx.send(file=epic_picture)
        await ctx.send('Эпический мем')
    else:
        legendary_image()
        await ctx.send(file=legendary_picture)
        await ctx.send('Легендарный мем')

bot.run(bot_token)
