import discord
from discord.ext import commands
import requests
import dislash
from dislash import Button, Option, InteractionClient, OptionType

class usercommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inter_client=InteractionClient(self.bot)
    @commands.command(brief="Owner")
    async def customcommandslist(self, ctx):
        a=[]
        cog=self.bot.get_cog("usercommands")
        for i in cog.get_commands():
            a.append(f"`{i.name} | Made by: {i.brief}`\n")
        await ctx.reply("".join(a))    

    @commands.command(brief="Owner")
    async def customcommand(self,ctx):
        await ctx.reply("**__Want a custom command?__*\nJust dm me with this format!\n**name:**\n**description**:\n**type**: <normal/slash/embed>")    

    @dislash.command(brief="pickle#5873", name="syrup", description="Command by pickle#5873", guild_ids=[855956103917338624])
    async def syrup(self,inter):
        embed=discord.Embed(title="Two men kissing").set_image(url="https://cdn.discordapp.com/attachments/912105006692462652/912759335501840414/two-black-men-kissing-meme-by-jridge98-redbubble-49380539.png").set_footer(text="Command by pickle#5873, to get ur own do g?customcommand")
        await inter.reply(embed=embed)
    @commands.command(brief="LIL_DERPYZ#4392")
    async def chungus(self, ctx):
        request = requests.get("https://meme-api.herokuapp.com/gimme/chungus")   
        json = request.json()
        embed=discord.Embed(title=json['title'], url=json['postLink']).set_image(url=json['url']).set_footer(text=f"Custom command by LIL_DERPYZ#4392, do g?customcommand to get your own")
        await ctx.send(embed=embed) 

    @commands.command(brief="Emperor Napoleon#6833")
    async def napoleon(self, ctx):
        request= requests.get("https://cdn.discordapp.com/attachments/909988821943324702/913129285655617556/image0-39.jpg")
        file = open("./assests/membercommands.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/membercommands.png"))     

    @dislash.command(brief="Luingi Reigns Supreme#2401", name="chunknorris", description="Custom command by Luingi Reigns Supreme#2401", guild_ids=[855956103917338624])  
    async def chunknorris(self,inter):
        request = requests.get("https://api.icndb.com/jokes/random")
        json = request.json()
        await inter.reply(json['value']['joke'].replace("&quot;", "\""))  

def setup(bot):
    bot.add_cog(usercommands(bot))           