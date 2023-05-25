from os import system
system("pip install discord==1.7.3")
system("pip install discord-py==1.7.3")
import psutil
import time
import discord
import asyncio
import ctypes
from pypresence import Presence
import colorama
from colorama import Fore, init, Style
import platform
client_id = '1111145614424686602'
RPC = Presence(client_id,pipe=0)
RPC.connect()
start_time=time.time()
RPC.update(start=start_time, state=f"Cloning a server!",large_image="worrysmirk", large_text="Lua Cloner",
            small_image="worrythumbsup", small_text="By SakshL and NotTacos",buttons=[{"label": "Join Server", "url": "https://discord.gg/notsaksh"}])
from serverclone import Clone
intents = discord.Intents().all()
bot = discord.Client(intents=intents)
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

                                    ██╗░░░░░██╗░░░██╗░█████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                    ██║░░░░░██║░░░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                    ██║░░░░░██║░░░██║███████║  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
                                    ██║░░░░░██║░░░██║██╔══██║  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
                                    ███████╗╚██████╔╝██║░░██║  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
                                    ╚══════╝░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: SakshL#6969 and NotTacos#0001.{Style.RESET_ALL}
                                                            {Fore.MAGENTA}"Pycord sucks." - NotTacos 2023{Style.RESET_ALL}
        """)
ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Server Cloner - SakshL and NotTacos")
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@bot.event
async def on_ready():
    print(f"Logged In as : {bot.user}")
    print("Cloning Server")
    guild_from = bot.get_guild(int(input_guild_id))
    guild_to = bot.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await bot.close()


bot.run(token, bot=False)
