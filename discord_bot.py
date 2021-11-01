from dotenv import load_dotenv
import os
import discord
from discord import client
from discord.ext import tasks, commands
import time
from get_requests import get_crypto_data, all_crypto_prices
from string_helper import *

class MyClient(discord.Client, discord.Embed, commands.Cog):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self._dev = "DY"
        self._description = "Tracking Crypto with ease"
        self._dev_url = "https://github.com/GoldenTBE"
        self._dev_pfp = "https://avatars.githubusercontent.com/u/54921144?v=4"
        self._footer = 'Version 2.3.1 | Fast and Efficient'
        self._crypto_thumbnails = cc_thumbnails
    
    async def on_ready(self): #Function tells user if bot is logged in. 
        print(f'Logged in as {self.user}')
        await client.change_presence(activity= discord.Game(name=self._footer))
    
    async def on_message(self, message): #awaiting messages from user
        if message.content.startswith('!'):
            try:
                command = message.content.lower()[1:]
                if command in commands_dict:
                    if commands_dict[command] == 'help':
                        await message.channel.send(embed = self.help_embed())
                    elif commands_dict[command] == 'monitor':
                        await message.channel.send(embed = self.alerts('Started Monitor!', 'All Prices will be sent every 30 minutes, "!stop" to end monitor'))
                        self.start_monitor(message.channel)
                    elif commands_dict[command] == 'stop':
                        self.stop_monitor()
                    else:
                        await message.channel.send(embed = self.crypto_price(command,commands_dict[command]))
                else:
                    await message.channel.send(embed = self.alerts(f'Invalid Command','"!help" for commands'))
            except Exception as e:
                print(e)
                await message.channel.send('<@281626075996356610>')
                await message.channel.send(embed = self.alerts('Error :warning:',e))

    def start_monitor(self,channel):
        self.monitor.start(channel)

    def stop_monitor(self):
        self.monitor.cancel()
    
    @tasks.loop(minutes=30)
    async def monitor(self,channel):
        await channel.send(embed = self.crypto_price('all','All CryptoCurrencies'))


    def crypto_price(self,currency,name): 
        if currency == 'all': #calls all_prices, this returns all coins in string_helper
            returned_data = all_crypto_prices()
        else:
            returned_data = get_crypto_data(currency.upper()) #need to .upper() due to logic in prev function
        embed = discord.Embed(
            title = name,
            description = self._description,
            colour = discord.Colour.blue()    
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)
        embed.set_thumbnail(url = self._crypto_thumbnails[currency])
        embed.add_field(name = "__Currency__", value = ':flag_us:',inline= False)

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        embed.add_field(name = "__Time__", value = "`" + current_time + "`",inline=False)

        for key, value in returned_data.items():
            if key == "All Time High":
                embed.add_field(name = "__" + key + "__", value = "`$"+ value + "`", inline = False)
            else:
                embed.add_field(name = "__" + key + "__", value = "`$"+ value[:7]+"`", inline = False)
    
        print(f'Sent Embed {time.ctime()}')
        return embed

    def help_embed(self): #Help 
        embed = discord.Embed(
            title = 'Help Page',
            description = self._description,
            colour = discord.Colour.orange()
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)
        
        for key, value in help_info.items():
            embed.add_field(name= "__" + key + "__", value = "`" + value +"`", inline = False)

        print(f'Sent Embed {time.ctime()}')
        return embed

    def alerts(self,title,desc):
        embed = discord.Embed(
            title = title,
            description = desc,
            colour = discord.Colour.orange()
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)
        return embed

while True:
    load_dotenv()
    discord_key = os.getenv("DISCORD_TOKEN")
    client = MyClient()
    client.run(discord_key) 
