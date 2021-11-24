import discord
from discord.ext import commands
import os
from dislash import InteractionClient, Option, OptionType
import json


intents=discord.Intents().all()
client = commands.Bot(command_prefix="g?", case_insensitive=True, help_command=None, intents=intents)
inter_client = InteractionClient(client)

    
@client.event
async def on_ready():
    print("Running...\n[--Available cogs--]\n")
    client.load_extension("Cogs.fun")
    client.load_extension("Cogs.listeners")
    client.load_extension("Cogs.misc")
    client.load_extension("Cogs.moderation")
    client.load_extension("Cogs.help")
    client.load_extension("Cogs.error")
    await client.cogs["Music"].start_nodes()

    for cog in client.cogs:
        print(cog)

@client.command()
@commands.is_owner()
async def webhook(ctx, channel:discord.TextChannel, name):
    webhook = await channel.create_webhook(name=name)
    await ctx.reply("Created webhook at <#%s>, Payload url: %s" % (channel.id, webhook.url))

@client.event
async def on_message(msg):
    if f"<@909763638406025226>" in msg.content:
        await msg.reply("Hello! My prefix is: g?")
    await client.process_commands(msg)    

class colors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

@client.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        client.unload_extension("Cogs.{}".format(cog))
        client.load_extension(f"Cogs.{cog}")
        await ctx.reply(f"Reloaded cog: {cog}")
    except commands.ExtensionNotLoaded:
        client.load_extension(f"Cogs.{cog}")
        await ctx.reply(f"Loaded cog: {cog}")
    except commands.ExtensionNotFound:
        await ctx.reply("No cog with that name!")
    except commands.ExtensionAlreadyLoaded:
        pass

@client.command()
@commands.is_owner()
async def eval(ctx, *, code):
    try:
        output = await eval(code)
        status = 200
    except Exception as e:
        output = e
        status = 400
    await ctx.reply(f'Evaluation exited with return status: {status} ({"failed" if status == 400 else "success"}), ```py\n[in]:\n{code}\n[out]:\n{output}n```')

@client.command()
@commands.is_owner()
async def unload(ctx, cog):
    try:
        client.unload_extension("Cogs.{}".format(cog))
    except commands.ExtensionNotLoaded:
        await ctx.reply("Cog not loaded!")
    except commands.ExtensionNotFound:
        await ctx.reply("No cog with that name.")      

with open("secrets.json", "r") as f:
    a=json.load(f)
    token=a['TOKEN']
client.run(token)
