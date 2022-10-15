import discord
from discord.utils import get

intents = discord.Intents.all()
intents.members = True 
client = discord.Client(intents=intents)

Member_count_channels = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    activity = discord.Game(name="DevBot", type=1)
    
    await client.change_presence(status=discord.Status.online, activity=activity)

    guilds = client.guilds
    for guild in guilds:
        Member = len([m for m in guild.members if not m.bot])
        
        channel = get(guild.channels, name=f"Member: {Member}")
        if not channel:
            Member_count_channels.append(await guild.create_voice_channel(f'Member: {Member}')) 

@client.event
async def on_member_join(member):
    guild = member.guild
    Member = len([m for m in guild.members if not m.bot])
    for channel in Member_count_channels:
        if channel.guild == guild:
            await channel.edit(name=f"Member: {Member}")
@client.event
async def on_member_remove(member):
    guild = member.guild
    Member = len([m for m in guild.members if not m.bot])
    for channel in Member_count_channels:
        if channel.guild == guild:
            await channel.edit(name=f"Member {Member}")











        



client.run("Dein Token")
