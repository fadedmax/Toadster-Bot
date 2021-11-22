import discord
from discord.ext import commands
from discord.ext.commands import bot

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"You are missing permissions: {commands.MissingPermissions.missing_perms[0]}")  
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(f"I am missing the permission: {commands.MissingPermissions.missing_perms[0]} to perform that action")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"You are missing a required argument, check our documentation to see the usages! https://github.com/osam7a/Toadster-Bot/wiki")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(f"Invalid arguments! Check our documentation to see the usages! https://github.com/osam7a/Toadster-Bot/wiki")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.reply("That command doesnt even exist!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply("That command is on cooldown!")    
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.reply("That cog is already loaded!")
        elif isinstance(error, commands.ExtensionFailed):
            await ctx.reply(f"Error occured while running this command, exception: ```diff\n-{commands.ExtensionFailed.original}\n```")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Too many arguments! Check out our documentation to see the usages! https://github.com/osam7a/Toadster-Bot/wiki")
        elif isinstance(error, commands.NotOwner):
            await ctx.reply("You are not a developer/owner to do that!")
        elif isinstance(error, commands.MessageNotFound):
            await ctx.reply("Message not found.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("Unknown user! Check if the user is in the guild.")
        elif isinstance(error, commands.UserNotFound):
            await ctx.reply("This user was never in the bot cache!")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.reply("Unkown channel!")
        elif isinstance(error, commands.ChannelNotReadable):
            await ctx.reply("I Do not have permissions to read that channel!")
        elif isinstance(error, commands.BadColourArgument):
            await ctx.reply("Invalid color!")
        elif isinstance(error, discord.Forbidden):
            await ctx.send(f"I do not have permissions to do that.")    
        else:
            await ctx.reply(f"```diff\n-{error}\n```")  


def setup(bot):
    bot.add_cog(ErrorHandler(bot))