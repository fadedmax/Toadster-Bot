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
            if subreddit == "boobs" or subreddit == "ass" or subreddit == "porn" or subreddit == "nsfw" or subreddit == "tits" or subreddit == "daddy":
                return await ctx.reply("NSFW Is not allowed!")
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
        result = json['insult']
        x = result.replace("&quot;", "\"")
        await ctx.send(f"{user.mention} {x}")
    @commands.command()
    async def snipe(self, ctx, limit:int=None):
         if limit != None:
             if limit > 10:
                 return await ctx.reply("Too high limit! Max 10")
         with open("./dicts/deleted_messages.json", "r") as f:
            load= json.load(f)
         result = ''   
         last_msg = load[len(load)-1]
         if limit == None:
             return await ctx.reply(f"{last_msg['message']['author']} Said: {last_msg['message']['content']}")
         else:
             for i in load[len(load)-1-limit:len(load)-1]:
                 result += f"\n{i['message']['author']} Said: {i['message']['content']}"  
             return await ctx.reply(result)      

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
    async def hack(self, ctx, user:discord.User):
        ip = f"192.225.{random.randint(0, 100)}.{random.randint(0, 10)}"
        momname = random.choice(['Carol', 'Jessica', 'Emily', 'UrMomIsHot', 'Amogus', 'bandarita', 'shawerma'])
        sisters=random.randint(0, 20)
        lastdm = random.choice(['hey babe', 'your mom is hot', 'its so big send more', 'help am dying', 'who iz u?', 'never gonna give you up', 'pls work', f'{user} is the best to exist'])
        favoritefood = random.choice(['pizza', 'burger', 'apple', 'fruit', 'cucumber', 'falafel', 'french fries', 'eggplants', 'mac n cheese'])
        crush = random.choice(['Carol', 'Jessica', 'Emily', 'UrMomIsHot', 'Amogus', 'bandarita', 'shawerma'])
        embed1 = discord.Embed(title="Fetching ip...", color=discord.Colour.blue())
        msg = await ctx.reply(embed=embed1)
        await asyncio.sleep(2)
        ipemb=discord.Embed(title=f"ip: {ip}", color=discord.Colour.blue())
        await msg.edit(embed=ipemb)
        await asyncio.sleep(1.5)
        embed2=discord.Embed(title="Looking for mom...", color=discord.Colour.blue())
        await msg.edit(embed=embed2)
        await asyncio.sleep(2)
        momnameemb = discord.Embed(title=f"Mom's name: {momname}", color=discord.Colour.blue())
        await msg.edit(embed=momnameemb)
        await asyncio.sleep(1.5)
        embed3=discord.Embed(title=f"`{user}.fetch_dms()`...", color=discord.Colour.blue())
        await msg.edit(embed=embed3)
        await asyncio.sleep(2)
        lastdmemb = discord.Embed(title=f"Last DM: \"{lastdm}\"", color=discord.Colour.blue())
        await msg.edit(embed=lastdmemb)
        await asyncio.sleep(1.5)
        embed4=discord.Embed(title=f"`{user}.favorite_food`...", color=discord.Colour.blue())
        await msg.edit(embed=embed4)
        await asyncio.sleep(2)
        favfoodemb=discord.Embed(title=f"Favorite food: {favoritefood}", color=discord.Colour.blue())
        await msg.edit(embed=favfoodemb)
        await asyncio.sleep(1.5)
        embed5=discord.Embed(title=f"Getting crush...", color=discord.Colour.blue())
        await msg.edit(embed=embed5)
        await asyncio.sleep(2)
        crushemb=discord.Embed(title=f"Crush: {crush}", color=discord.Colour.blue())
        await msg.edit(embed=crushemb)
        await asyncio.sleep(2)
        embed6=discord.Embed(title="The totally real hack just finished.", color=discord.Colour.blue())
        await msg.edit(embed=embed6)


    @commands.command()
    async def encrypt(self, ctx, shift:int, *, text):
        result = ''
        if shift > 25:
            return await ctx.reply("Shift too long!")
        for a in range(len(text)):
            i = text[a]
            if (i.isupper()):
                result += chr((ord(i) - shift - 65) + 65)
            else:
                result += chr((ord(i) - shift - 97) + 97)    
        await ctx.reply(f"Encrypted your message with shift: {shift}, result: **{result}**") 

    @commands.command()
    async def decrypt(self, ctx, shift, *, text):
        result = ''  
        if shift.isalpha() == False:
            for a in range(len(text)):
                i = text[a]
                if (i.isupper()):
                    result += chr((ord(i) + int(shift) + 65) - 65)
                else:
                    result += chr((ord(i) + int(shift) + 97) - 97)     
            return await ctx.reply(f"Decrypted your message, result: **{result}**") 
        else:
            message = text #encrypted message
            if message.isupper():
                LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            elif message.islower():
                LETTERS = "abcdefghijklmnopqrstuvwxyz"
            else:
                LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"        
            test=[]
            for key in range(len(LETTERS)):
                translated = ''
                result = ''
                for symbol in message:
                    if symbol in LETTERS:
                        num = LETTERS.find(symbol)
                        num = num - key
                        if num < 0:
                            num = num + len(LETTERS)
                            translated = translated + LETTERS[num]
                        else:
                            translated = translated + symbol
                result += "`Key #%s: %s` " % (key, translated)
                test.append(result)
            await ctx.reply(f"Decryption ended with **{len(LETTERS)}** Possiblities:\n{''.join(test)}")   

    @commands.command()
    async def lastEdited(self, ctx, limit:int=None):
        if limit != None:
             if limit > 10:
                 return await ctx.reply("Too high limit! Max 10")
        f=open("./dicts/edited_msgs.json", "r")
        load = json.load(f)
        result = ''
        if limit == None:
            i=load[len(load)-1]
            result += f"Author: {i['author']}, Before: {i['before']}, After: {i['after']}" 
        else:
            for i in load[len(load)-1-limit:len(load)-1]:
                result += f"\n**Author: {i['author']}, Before: {i['before']}, After: {i['after']}**"  
        await ctx.reply(result)                              

def setup(bot):
    bot.add_cog(fun(bot))
