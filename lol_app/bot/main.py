import discord
from discord.ext import commands

import lol_app.settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print(bot.user)
    print(bot.user.id)
    print("______________________")


if __name__ == "__main__":
    bot.run(lol_app.settings.DISCORD_TOKEN)
