import discord
from discord import app_commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)


MYGUILD = discord.Object(id=984482993336905738)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MYGUILD)
        await self.tree.sync(guild=MYGUILD)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


    
    activity = discord.Game(name="/help", type=1)

    await client.change_presence(status=discord.Status.online, activity=activity)



@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Sagt Hallo"""
    
    
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')



client.run("Dein Token")