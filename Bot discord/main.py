import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
from emojies import emoji_len, emojis
import os
import requests
from discord.ext.commands.errors import MissingPermissions

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

img_name = (os.listdir('images'))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        msg = f"Bienvenido {member.mention} a {guild.name}!"
        await guild.system_channel.send(msg)

@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def emoji(ctx):
    x = random.randint(1, emoji_len)
    emoji = emojis.get(x, None)
    if emoji:
        await ctx.send(emoji)
    else:
        await ctx.send(f'Todavia no añado este emoji (Número: {x})')

@bot.command()
async def photo(ctx):
    await ctx.send(ctx.author.avatar.url)

@bot.command()
async def password(ctx, arg=None):
    try:
        length = int(arg) if arg else 10
        await ctx.send(gen_pass(length))
    except ValueError:
        await ctx.send('Please choose a valid number')
    
@bot.command()
async def meme(ctx):
    x = random.randint(1,3)
    if x == 1:
        x = img_name[0]
    elif x == 2:
        x = img_name[1]
    elif x == 3:
        x = img_name[2]
    with open(f'images/{x}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
@commands.has_permissions(manage_messages = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def purge(ctx, arg: int):
    z = await ctx.channel.purge(limit = arg)
    await ctx.send(f'Elimine {len(z)} mensaje(s)')
@purge.error
async def purgeerror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Necesitas permisos para administrar mensajes!')
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
    else:
        raise error
     
@bot.command()
async def inforole(ctx):
    await ctx.send(ctx.author.guild_permissions)


































































































































































token = 'What ya looking for'
