import discord
from discord.ext import commands
import aioconsole
import js2py
import sys
import os
import io
from aioconsole import aexec

class dev_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def execute(self, ctx, codetype, *, code:str):
        if codetype == "py":
         old_stdout = sys.stdout
         new_stdout = io.StringIO()
         sys.stdout = new_stdout
         local_variable = 2
         codeStr = code.lstrip("```py")
         
         codeRealStr = codeStr.rstrip("```")
         try:
          await aexec(codeRealStr)
         except Exception as e:
          await ctx.send(f"```py\n[in]: {codeRealStr}\n[out]:\n{e}\n ```")
          return
         result = sys.stdout.getvalue().strip()
         sys.stdout = old_stdout
         await ctx.send(f"```py\n[in]: {codeRealStr}\n[out]:\n{str(result)}\n```")
        elif codetype == "js":
         old_stdout = sys.stdout
         new_stdout = io.StringIO()
         sys.stdout = new_stdout
         local_variable = 2
         codeStr = code.lstrip("```js")
         codeRealStr = codeStr.rstrip("```")
         try:
          js2py.eval_js(codeRealStr)
         except Exception as e:
          await ctx.send(f"```js\n[in]: {codeRealStr}\n[out]:\n{e}\n```")
         result = sys.stdout.getvalue().strip()
         sys.stdout = old_stdout
         await ctx.send(f"```js\n[in]: {codeRealStr}\n[out]:\n{result}\n```")

def setup(bot):
    bot.add_cog(dev_commands(bot))
