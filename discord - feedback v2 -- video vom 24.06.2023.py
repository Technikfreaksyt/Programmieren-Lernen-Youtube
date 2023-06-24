import discord
from discord import app_commands
import traceback

from discord.interactions import Interaction





intents = discord.Intents.all()
intents.members = True
intents.voice_states = True 
client = discord.Client(intents=intents)


MY_GUILD = discord.Object(id=984482993336905738)

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


    

intents = discord.Intents.default()
client = MyClient(intents=intents)
    



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


    
    activity = discord.Game(name="/help", type=1)

    await client.change_presence(status=discord.Status.online, activity=activity)




class Report(discord.ui.Modal, title='Report'):

    report = discord.ui.TextInput(
        label='Welchen nutzer willst du melden und warum?',
        style=discord.TextStyle.long,
        placeholder='Bsp: @Devbot#0268, er hat beleidigt, \nAm besten mit Beweis, z.B ein Bild',
        required=True,
    )


    async def on_submit(self, interaction: Interaction):
        await interaction.response.send_message(f'Hey {interaction.user.mention}, danke für deine Meldung!', ephemeral=True)
        channelone = client.get_channel(1014192238894514270)
        message = await channelone.send(f'Meldung von {interaction.user.mention}, Meldung: {self.report.value} ')

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        traceback.print_exception(type(error), error, error.__traceback__)
        




@client.tree.command()
async def report(interaction: discord.Interaction):
    """Melde einen Benutzer"""
    await interaction.response.send_modal(Report())







    




client.run("DEIN_TOKEN")