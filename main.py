import discord, os
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1160743819726299257))
    print(f"We have logged in as {client.user}")


@tree.command(
    name="hello",
    description="A slash command that says 'Hello!'",
    guild=discord.Object(id=1160743819726299257),
)
async def hello(interaction):
    if str(interaction.user.id) == "329399231229984768":
        await interaction.response.send_message("Fuck you, Ian.")
    else:
        await interaction.response.send_message("Hello, friend.")


client.run(os.getenv("TOKEN"))
