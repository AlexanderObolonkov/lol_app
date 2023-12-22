import logging

import discord
from discord.ext import commands

from lol_app import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
logger = logging.getLogger("bot")


@bot.event
async def on_ready() -> None:
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")


@bot.command()
async def ping(ctx: commands.Context) -> None:
    await ctx.send("Pong!")


if __name__ == "__main__":
    bot.run(settings.DISCORD_TOKEN, root_logger=True)
