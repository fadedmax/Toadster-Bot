import discord
import requests
import dislash
import json
import asyncio
from dislash import ActionRow, InteractionClient, Button, ButtonStyle
from discord.ext import commands
import random

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inter_client = InteractionClient(bot)

    @commands.command()
    async def meme(self, ctx):
     request = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes")
     json = request.json()
     embed=discord.Embed(title=json['title'], url=json['postLink'])
     embed.set_image(url=json['url'])
     msg = await ctx.reply(embed=embed)


    @commands.command()
    async def reddit(self, ctx, subreddit):
            request = requests.get(f"https://meme-api.herokuapp.com/gimme/{subreddit}")
            json = request.json()
            embed=discord.Embed(title=json['title'], url=json['postLink'])
            embed.set_image(url=json['url'])
            msg = await ctx.reply(embed=embed)



    @commands.command()
    async def mcinfo(self, ctx, minecraftusername):
        request=requests.get(f"https://some-random-api.ml/mc?username={minecraftusername}")
        json = request.json()
        namehistory=""
        for name in json['name_history']:
            if name['changedToAt'] == "Original Name":
                namehistory += f"`Original Name: {name['name']}`\n"
            else:
                namehistory += f"`{name['name']} | {name['changedToAt']}`\n"

        embed=discord.Embed(title=f"Minecraft info about {minecraftusername}", description=f"**Username:** {minecraftusername}\n**UUID:** {json['uuid']}\n**Name History:**\n{namehistory}")
        await ctx.reply(embed=embed)
    @commands.command()
    async def emojiname(self, ctx, *,    name:str):
        nameL = ""
        for i in name.lower():
            if i == " ":
                nameL += "   "
            else:

                nameL += f":regional_indicator_{i.lower()}:"
        await ctx.send(nameL)
    @commands.command()
    async def flipcoin(self, ctx):
        answers=['heads', 'tails']
        await ctx.reply(random.choice(answers))
    @commands.command()
    async def roast(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author
        request = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        json = request.json()
        await ctx.send(f"{user.mention} {json['insult']}")
    @commands.command()
    async def snipe(self, ctx):
         with open("./dicts/deleted_messages.json", "r") as f:
            load= json.load(f)
         last_msg = load[len(load)-1]
         last_msg_str = last_msg['message']['content']
         await ctx.send(f"**{last_msg['message']['author']} Said: {last_msg_str}**")

    @commands.command()
    async def rpc(self, ctx):
        embed=discord.Embed(title="Choose from rock paper scissors.")
        row = ActionRow(Button(style=ButtonStyle.blurple, label="🤜 Rock", custom_id="rock"), Button(style=ButtonStyle.green, label="✂ Scissors", custom_id="scissors"), Button(style=ButtonStyle.red, label="📄 Paper", custom_id="paper"))
        msg = await ctx.send(embed=embed, components=[row])
        inter = await msg.wait_for_button_click()
        result = None
        if inter.clicked_button.label == "🤜 Rock":
            result = "rock"
            await inter.reply("You chose rock", ephemeral=True)
        elif inter.clicked_button.label == "✂ Scissors":
            result = "scissors"
            await inter.reply("You chose scissors", ephemeral=True)
        else:
            result = "paper"
            await inter.reply("You chose paper", ephemeral=True)
        await asyncio.sleep(5)

        choice = random.choice(['rock', 'paper', 'scissors'])
        winner = None
        if result == "rock" and choice == "paper":
            winner = "me"
        elif result == "rock" and choice == "rock":
            winner = "draw"
        elif result == "rock" and choice == "scissors":
            winner = "you"
        elif result == "paper" and choice == "paper":
            winner = "draw"
        elif result == "paper" and choice == "rock":
            winner = "you"
        elif result == "paper" and choice == "scissors":
            winner = "me"
        elif result == "scissors" and choice == "rock":
            winner = "me"
        elif result == "scissors" and choice == "paper":
            winner = "you"
        elif result == "scissors" and choice == "scissors":
            winner = "draw"

        embed2=discord.Embed(title=f"I chose {choice}, and you chose {result}, winner is... **{winner}**")
        await msg.edit(embed=embed2, components=None)

    @commands.command()
    async def ascii(self, ctx, *, text:str):
        if len(text.lower()) > 16:
            await ctx.reply("Message too long!")
            return
        request= requests.get(f"https://artii.herokuapp.com/make?text={text}")
        result = request.text
        await ctx.reply(f"```\n{result}\n```")



def setup(bot):
    bot.add_cog(fun(bot))
