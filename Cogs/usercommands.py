import discord
from discord.ext import commands
import requests

class usercommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief="Owner")
    async def customcommandslist(self, ctx):
        a=[]
        cog=self.bot.get_cog("usercommands")
        for i in cog.get_commands():
            a.append(f"`{i.name} | Made by: {i.brief}`\n")
        await ctx.reply("".join(a))    

    @commands.command(brief="pickle#5873")
    async def syrup(self,ctx):
        request=requests.get("https://cdn.discordapp.com/attachments/912105006692462652/912759335501840414/two-black-men-kissing-meme-by-jridge98-redbubble-49380539.png")
        file=open("./assests/membercommands.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply("Custom Command By pickle#5873, to get yours, do g?customcommand", file=discord.File("./assests/membercommands.png"))

    @commands.command(brief="LIL_DERPYZ#4392")
    async def chungus(self, ctx):
        request = requests.get("https://meme-api.herokuapp.com/gimme/chungus")   
        json = request.json()
        embed=discord.Embed(title=json['title'], url=json['postLink']).set_image(url=json['url']).set_footer(text=f"Custom command by LIL_DERPYZ#4392, do g?customcommand to get your own")
        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(usercommands(bot))           