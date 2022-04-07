import asyncio
import discord
from colorama import Fore,Style,Back


intents = discord.Intents.default()
intents.members=True
ice=discord.Client(intents=intents)

###########CONFIGS############

TOKEN = "ODg5NTI0OTA1NDU0OTkzNDA4.YUigoA.i3sBh0B7igRY5kgPdLalfKXu7As"
Guild = Your Guild Id
Welcome_Channel = Your Channel Id

@ice.event
async def on_ready():
    await ice.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="ICE Discord Welcomer"))
    print ("OH Hi Im In your Bot Now :)")


@ice.event
async def on_member_join(member):
    guild1 = ice.get_guild(Guild) 
    welcome1_channel = guild1.get_channel(Welcome_Channel)
    created_at = member.created_at.strftime("%b %d, %Y")
    embed1 = discord.Embed(title='ICE WELCOMER', description=f'Hey {member.mention} \n Welcome To {member.guild.name}', color=7419530) 
    embed1.add_field(name='**Joined Discord : **', value=f'``'+created_at+f'``', inline=False)
    embed1.set_image(url=f'{member.avatar_url}')
    embed1.set_footer(text='ICE TOOLS :)')
    await welcome1_channel.send(embed=embed1)

ice.run(TOKEN)