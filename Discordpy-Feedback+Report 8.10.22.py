import time
import discord
from asyncio import TimeoutError
from discord.utils import get






intents = discord.Intents.all()
intents.members = True
intents.voice_states = True 
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    activity = discord.Game(name="!help", type=1)

    await client.change_presence(status=discord.Status.online, activity=activity)









                             

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    member = message.author

    if message.content.startswith('hello'):
        await message.channel.send('Hi')


    if message.content.startswith('feedback'):
        await message.channel.send('Deine Rückmeldung:')
        await message.channel.send('Your feedback:')
        UserInput1 = await client.wait_for("message", check = lambda x: x.author == member)
        await message.channel.purge(limit=4)
        await client.get_channel(Deine Channel ID).send (f"Rückmeldung von {message.author} : {UserInput1.content}")

    if message.content.startswith('report'):
        await message.channel.send('Wen willst du melden?:')
        await message.channel.send('Which user do you want to report?:')
        UserInput2= await client.wait_for("message", check = lambda x: x.author == member)
        await message.channel.purge(limit=4)
        await client.get_channel(Deine Channel ID).send (f"Rückmeldung von {message.author} : {UserInput2.content}")


 
    


client.run("Dein Token")