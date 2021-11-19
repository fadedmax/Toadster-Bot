import discord
from discord.ext import commands

class dev_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, code:str):
        try:
            result= eval(code)
        except Exception as e:
            await ctx.reply(f"Evaluation complete with return value 400 (error): ```py\n[in]: {code}```\n```diff\n[out]:\n- {e}\n```")
            return
        await ctx.reply(f"Evaluation complete with return value 200 (success): ```py\n[in]: {code}\n[out]: {result}\n```")

def setup(bot):
    bot.add_cog(dev_commands(bot))
