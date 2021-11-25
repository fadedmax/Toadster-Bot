import discord
from discord.ext import commands
import dislash
from dislash import InteractionClient, Button, Option, OptionType

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inter_client = InteractionClient(self.bot)

    @dislash.slash_command(name="test", description="Test Slash", options=[
        Option("title", "Title of the embed"),
        Option("description", "Description of the embed")
    ], guild_ids=[855956103917338624, 909762686030589972])
    async def test(self, inter, title, description):
        await inter.reply(embed=discord.Embed(title=title, description=description), ephemeral=True)


def setup(bot):
    bot.add_cog(Slash(bot))            