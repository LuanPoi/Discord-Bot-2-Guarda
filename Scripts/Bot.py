import discord
import yaml

_config = yaml.safe_load(open('..\config.yaml', 'r'))

guardaSovietico = discord.Client()

@guardaSovietico.event
async def on_ready():
    print('We have logged in as {0.user}'.format(guardaSovietico))

@guardaSovietico.event
async def on_message(message):
    if message.author == guardaSovietico.user:
        return

    if message.content.startswith('$hw'):
        await message.channel.send('Hello World!')

    if (message.author.id == ((_config['oficialSovietico'])['id'])) & (message.content.endswith("Abram os portões!")):
        await message.channel.send('Ele não trouxe vodka!')

    if message.content.startswith('Eu trouxe vodka'):
        await message.channel.send('Ele trouxe vodka!')

@guardaSovietico.event
async def on_member_join(member):
    canal = guardaSovietico.get_channel((((_config['canais'])['deTexto'])['portoes-de-moscou']))
    await canal.send('"' + member.display_name + '"' + ' à vista!')

guardaSovietico.run(_config['discordBotKey'])
