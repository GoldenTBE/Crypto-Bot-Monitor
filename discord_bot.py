import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import time
from Keys import discord_key
from get_requests import get_crypto_data, all_crypto_prices
from string_helper import *

class CryptoTracker(discord.Client, discord.Embed):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self._dev = "DY"
        self._description = "Tracking Crypto with ease"
        self._dev_url = "https://github.com/GoldenTBE"
        self._dev_pfp = "https://avatars.githubusercontent.com/u/54921144?v=4"
        self._footer = 'Tracking made easy | Version 0.0.2 | Made with Love '
        self._crypto_thumbnails = cc_thumbnails
        

    
    async def on_ready(self): #Function tells user if bot is logged in. 
        print(f'Logged in as {self.user}')
    
    
    async def on_message(self, message): #awaiting messages from user
        try:
            if message.content == '!help': #HELP IN FOR USERS
                print(f'Help Command Used by: {message.author}')
                await message.channel.send(embed= self.help_embed())

            elif message.content == '!BTC': #BTC INFO 
                print(f'BTC Info called by: {message.author}')
                await message.channel.send(embed = self.crypto_price('BTC','Bitcoin'))
                
            elif message.content == '!ADA': #ADA INFO
                print(f'ADA Info called by: {message.author}')
                await message.channel.send(embed = self.crypto_price('ADA','Cardano'))

            elif message.content == '!ETH': 
                print(f'ETH Info called by: {message.author}')
                await message.channel.send(embed = self.crypto_price('ETH','Ethereum'))

            elif message.content == '!error':
                print(f'Error Info called by: {message.author}')
                await message.channel.send(embed = self.error_embed()) 

            elif message.content == '!Monitor':
                await message.channel.send(embed = self.error_embed())    
        except Exception as e:
            print(e)
            await message.channel.send('<@281626075996356610>')
            await message.channel.send(embed = self.error_embed())

    

    def crypto_price(self,currency,name): 
        returned_data = get_crypto_data(currency)
        embed = discord.Embed(
            title = name,
            description = self._description,
            colour = discord.Colour.blue()    
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)
        embed.set_thumbnail(url = self._crypto_thumbnails[currency])

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
            embed.add_field(name = "__" + key + "__", value = "`" + value +"`", inline = False)

        print(f'Sent Embed {time.ctime()}')
        return embed

    def error_embed(self): #Sent when Error Ocuurs
        embed = embed = discord.Embed(
            title = 'Error!',
            description = 'Alerting Dev! :hot_face:',
            colour = discord.Colour.red()
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)

        return embed


if __name__ == "__main__":
    client = CryptoTracker()
    client.run(discord_key) 
