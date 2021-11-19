import discord
from discord.ext import commands

class error(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Wrong usage!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Command on cooldown!")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Wrong usage!")
        else:
            raise error
            await ctx.send(f"```diff\n-{error}\n```")


def setup(bot):
    bot.add_cog(error(bot))            
