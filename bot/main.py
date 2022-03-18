import discord
import os
import requests
import json


c = discord.Client()

#quotes command functions
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    return(quote)
def get_author():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    author = json_data[0]['a']
    return(author)


@c.event
async def on_ready():
    print('{0.user} started'
        .format(c))

    await c.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

@c.event
async def on_message(message):
    if message.author == c.user:
        return
    if message.author == discord.user.User.bot:
        return
#ping command
    if message.content.startswith(".ping"):
        embed = discord.Embed(color=0xa29bfe)
        embed.add_field(name="Ping", value=f'{round(c.latency * 1000)} ms', inline=False)
        await message.channel.send(embed=embed)

#quotes
    if message.content.startswith(".quote"):
        quote = get_quote()
        author = get_author()
        embed=discord.Embed(color=0xa29bfe)
        embed.add_field(name=author, value=quote, inline=False)
        await message.channel.send(embed=embed)

#kalle
    if message.content.startswith(".kalle"):
        embed = discord.Embed(color=0xa29bfe)
        embed.set_image(url="https://luqas.me/img/fkalle.png")
        embed.add_field(name="Kalle", value="also ich bin personally intersexuell... but sometime fühl ich mich auch trans... like jede/r/ens/xier sollte das für sich entscheiden. jede/r/ens/xier soll das maken was Xier/DierSieer/Sier/Er/Sie/Es/z/zet/They/The/hen/hens✨AMAZING✨findet!", inline=False)
        await message.channel.send(embed=embed)


c.run(os.getenv('TOKEN'))