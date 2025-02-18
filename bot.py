import discord
from discord.ext import commands

TOKEN = ""
GUILD_ID =   # Replace with your server's ID

bot = commands.Bot()

# @bot.slash_command(
#   name="event-submission",
#   description="Type the name of the item drop or objective",
#   kwargs=["asd", "123"],
#   guild_ids=[GUILD_ID]
# )

# async def first_slash(ctx): 
#     await ctx.respond("You executed the slash command!")
    
drops = [
"Justiciar faceguard",
"Justiciar legguards",
"Justiciar chestguard",
"Avernic defender hilt",
"Sanguinesti staff",
"Ghrazi rapier",
"Scythe of vitur (uncharged)",
"Lil'zik",
"Holy ornament kit",
"Sanguine ornament kit",
"Sanguine dust",
"Learner KC",
]

@bot.slash_command(
    name="event-submission", 
    description="Type the name of the item drop or objective",
    guild_ids=[GUILD_ID], )
async def animal_command(
  ctx: discord.ApplicationContext,
  item: discord.Option(str, choices=drops), # type: ignore
  #party_member_1: discord.Option(str)
):
  await ctx.respond(f'You submitted that you got a `{item}`!')
    
bot.run(TOKEN)