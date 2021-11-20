import discord
from discord.ext import commands
import json
import asyncio

unmuted = {}
unbanned = {}

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user:discord.User, reason=None):
        with open("./dicts/warns.json", "r") as f:
            users=json.load(f)
        if reason == None:
            reason="No reason provided"
        if f"{ctx.guild.id}" not in users:
            users[f'{ctx.guild.id}'] = {}

        if f"{user.id}" not in users[f'{ctx.guild.id}']:
            users[f'{ctx.guild.id}'][f'{user.id}'] = {"warns": [{f"{ctx.message.created_at}":f"{reason}"}]}
            await ctx.reply(f"Warned {user.mention} for reason: {reason}, this is their first warning.")
            with open("./dicts/warns.json", "w") as f2:
                json.dump(users, f2)
        else:
            users[f'{ctx.guild.id}'][f'{user.id}']['warns'].append({f"{ctx.message.created_at}":f"{reason}"})
            await ctx.reply(f"Warned {user.mention} for reason: {reason}, this is their {len(users[f'{ctx.guild.id}'][f'{user.id}']['warns'])} warning.")
            with open("./dicts/warns.json", "w") as f2:
                json.dump(users, f2)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warns(self, ctx, user:discord.User):
        with open("./dicts/warns.json", "r") as f:
            users=json.load(f)
        warnList=""
        if f"{user.id}" not in users[f'{ctx.guild.id}'] or len(users[f'{ctx.guild.id}'][f'{user.id}']['warns']) == 0:
            await ctx.reply(f"{user.mention} Was never warned.")
        else:
            for warn in users[f'{ctx.guild.id}'][f'{user.id}']['warns']:
                warnList += f"`{list(warn.keys())[0]} | {list(warn.values())[0]}`\n"
            embed=discord.Embed(title="Warn list for {}".format(user), description=f"History:\n{warnList}")
            await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def removewarn(self, ctx, user:discord.User, limit:int=None):
        with open("./dicts/warns.json", "r") as f:
            users=json.load(f)
        if limit == None:
            users[f'{user.id}']['warns'].clear()
            await ctx.reply(f"Cleared warns of {user.mention}")
            print(f"Cleared {user}'s warns")
            with open("./dicts/warns.json", "w") as f:
                json.dump(users, f)
            return
        for i in range(limit):
            users[f'{ctx.guild.id}'][f'{user.id}']['warns'].remove(users[f'{ctx.guild.id}'][f'{user.id}']['warns'][len(users[f'{ctx.guild.id}'][f'{user.id}']['warns'])-1])
        with open("./dicts/warns.json", "w") as f:
            json.dump(users, f)
        await ctx.reply(f"Removed {limit} warns from {user.mention}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit:int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"{ctx.author.mention} Purged {limit} messages", delete_after=5)
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:discord.User, reason=None):
         if reason == None:
            reason = "No reason provided"
         embed=discord.Embed(title=f"{user} Was kicked!", description=f"{user} Was kicked for: {reason}")
         embed2=discord.Embed(title=f"You have been kicked!", description=f"You were kicked from {ctx.guild.name} for reason: {reason}")
         await user.kick(reason=reason)
         await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user:discord.User, time:int, d:str, *, reason=None):
        if reason == None:
            reason = "No reason provided"
        await user.ban(reason=reason)
        embed=discord.Embed(title=f"{user} Was banned!", description=f"{user} Was banned for {time}{d} for reason: {reason}")
        embed2=discord.Embed(title=f"You have been banned!", descripition=f"You have been banned from {ctx.guild} for {time}{d} for reason: {reason}")
        try:
         await user.send(embed=embed2)
        except:
            await ctx.send("Cant send messages to this user!")
        await ctx.send(embed=embed)
        if d == "s":
            await asyncio.sleep(time)
        elif d == "m":
            await asyncio.sleep(time*60)
        elif d == "h":
            await asyncio.sleep(time*60*60)
        elif d == "d":
            await asyncio.sleep(time*60*60*24)
        await ctx.guild.unban(user)
        embed3=discord.Embed(title="You have been unbanned!!", description=f"You have been unbanned from {ctx.guild}!!")
        try:
         await user.send(embed=embed3)
        except:
         await ctx.send("Cant send messages to that user.")
        await ctx.send(f"{user} Was unbanned.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user:discord.User):
        global unbanned
        await ctx.guild.unban(user)
        await ctx.reply(f"Unbanned {user}")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user:discord.User, time:int, d:str, *, reason=None):
        if reason== None:
            reason = "No reason provided"
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.add_roles(role)
        embed=discord.Embed(title="Muted!", description=f"You have been muted on {ctx.guild.name} for {time}{d} for reason: {reason}")
        embed2=discord.Embed(title="Muted!", description=f"{user} Was muted for {time}{d} for reason: {reason}")
        try:
         await user.send(embed=embed)
        except:
         pass
        await ctx.send(embed=embed2)
        if d == "s":
            await asyncio.sleep(time)
        elif d == "m":
            await asyncio.sleep(time*60)
        elif d == "h":
            await asyncio.sleep(time*60*60)
        elif d == "d":
            await asyncio.sleep(time*60*60*24)
        await user.remove_roles(role)
        embed3=discord.Embed(title="Unmuted!", description=f"You have been unmuted on {ctx.guild}!")
        try:
         await user.send(embed=embed3)
        except:
         pass
        await ctx.send("Unmuted {}".format(user))
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, user:discord.User):
        global unmuted
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(role)
        await ctx.send(f"Unmuted {user}")
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def role(self, ctx, user:discord.User, role:discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            embed=discord.Embed(title=f"Removed role", description=f"Removed role <@&{role.id}> from {user.mention}")
            await ctx.reply(embed=embed)
        else:
            await user.add_roles(role)
            embed=discord.Embed(title=f"Added role", description=f"Added role <@&{role.id}> from {user.mention}")
            await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, channel:discord.TextChannel, amount:int):
        await channel.edit(slowmode_delay=amount)
        if amount != 0:
         await ctx.reply(f"Changed slowdown value for <#{channel.id}> to {amount}")
        else:
            await ctx.reply(f"Disabled slowdown in <#{channel.id}>")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, channel:discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        embed=discord.Embed(title="✅ Channel locked!", color=0x00ff11)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, channel:discord.TextChannel=None):
         role =  ctx.guild.default_role
         channel =  ctx.channel

         if ctx.author.permissions_in(channel).manage_permissions:
          overwrite = channel.overwrites_for(role)
          overwrite.send_messages = True
          await channel.set_permissions(role, overwrite=overwrite)
          embed=discord.Embed(title="✅ Channel unlocked!", color=0x00ff11)
          await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(moderation(bot))
