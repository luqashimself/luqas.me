import discord 
import os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} started'
    .format(client))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="god"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.test'):
        await message.channel.send('test')

@client.event
async def on_message(message):

  if message.author == client.user: 
      return
    
  if message.content.startswith('.ping'):
    await message.channel.send(f'Pong! {round (client.latency * 1000)} ms')
    

client.run(os.getenv('TOKEN'))