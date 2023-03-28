import discord, webbrowser
from discord.ext import commands


def run(token):
    client = commands.Bot(command_prefix="#", help_command=None, intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f"{client.user.name}({client.user.id}) est lancé.")
        print("--------------------------")
        print(f"{client.user} peut être connecté au serveur")
        webbrowser.open(f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot")

    @client.command(name="private")
    @commands.has_permissions(administrator=True)
    async def private_message(message):
        for member in message.guild.members:
            if member.bot == False:
                print(member)
                await member.send("Enter Your Message\n")

    client.run(token)
