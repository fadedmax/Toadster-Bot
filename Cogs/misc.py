import discord
from discord.ext import commands
import art
import requests

class misc(commands.Cog):
    def __inti__(self, bot):
        self.bot=bot
         
    @commands.command()
    async def image(self, ctx, query):
        request=requests.get(f"https://source.unsplash.com/1600x900/?{query}")
        file=open("./assests/picture.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/picture.png"))

    @commands.command()
    async def jail(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author
        request = requests.get(f"https://some-random-api.ml/canvas/jail?avatar={ctx.author.avatar_url(format='png')}")
        file=open("./assests/jailed.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/jailed.png"))    

    @commands.command()
    async def ascii(self, ctx, *text):
        if len(text) > 4:
            return await ctx.reply("Message too long!") 
        result = ""    
        for i in text:
                result += f"{art.text2art(i)}"

        await ctx.reply(f"```\n{result}\n```")

    @commands.command()
    async def art(self, ctx, query):
        try:
            await ctx.reply(f"```\n{art.art(query)}\n```")  
        except artError:
            await ctx.reply("Invalid art!")       



def setup(bot):
    bot.add_cog(misc(bot))        
       