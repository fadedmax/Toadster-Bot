import discord
from discord.ext import commands
from dislash import SelectMenu, InteractionClient, Button, ActionRow, SelectOption

class help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        InteractionClient(self.bot)
    @commands.command()
    async def help(self, ctx, category=None):
        if category == None:
            global helpmsg
            embed=discord.Embed(title=f"Hey {ctx.author}!", description="Please select a category")
            options = []
            for i in self.bot.cogs:
                if i == "listeners" or i == "dev_commands" or i == "error":
                 if ctx.author.id == 761159873194491915:
                  options.append(SelectOption(i, i))
                elif i == "moderation":
                    role = discord.utils.get(ctx.guild.roles, name="Staff")
                    if role in ctx.author.roles or ctx.author.id == 761159873194491915:
                        options.append(SelectOption(i, i))
                else:
                    options.append(SelectOption(i, i))
            helpmsg = await ctx.send(embed=embed, components=[SelectMenu(custom_id="helpmenu", max_values=1, placeholder="Select a category...", options=options)])
    @commands.Cog.listener()
    async def on_dropdown(self, inter):
        commands = ""
        a = inter.select_menu.selected_options[0].label
        a= self.bot.get_cog(a)
        a = a.get_commands()
        for i in a:
            if len(a) == 3 or len(a) or len(a) == 6 or len(a) == 9 or len(a) == 12:
                commands += f"`{i.name}`\n"
            else:
                commands += f"`{i.name}` "
        embed=discord.Embed(title=f"{inter.select_menu.selected_options[0].label} Commands", description=f"{commands}")
        await helpmsg.edit(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))
