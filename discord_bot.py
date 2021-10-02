import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import time
from Keys import discord_key

class CryptoTracker(discord.Client, discord.Embed):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self._dev = "DY"
        self._dev_url = "https://github.com/GoldenTBE"
        self._dev_pfp = "https://avatars.githubusercontent.com/u/54921144?v=4"
        self._footer = 'Version 0.0.1 | IN works'

    
    async def on_ready(self): #Function tells user if bot is logged in. 
        print(f'Logged in as {self.user}')
    
    
    async def on_message(self, message):
        if message.content == '!help':
            print(f'Help Command Used by: {message.author}')
            await message.channel.send(embed= self.help_embed())

        elif message.content == '!BTC':
            print(f'BTC Info called by: {message.author}')
            await message.channel.send(embed = self.formatting())
            
        elif message.content == '!ADA':
            print(f'ADA Info called by: {message.author}')
            await message.channel.send(embed = self.formatting())

        elif message.content == '!Monitor':
            await message.channel.send()    
    
    def formatting(self,content = None):
        embed = discord.Embed(
            title = 'Crypto Tracker',
            description = 'Tracking Crypto with ease.',
            colour = discord.Colour.blue()    
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.add_field(name = 'Current Price', value= 'Fill', inline= True)
        embed.add_field(name = 'Daily High', value= 'Fill', inline= True)
        embed.add_field(name = 'Market Cap', value= 'Fill', inline= True)
        embed.add_field(name = 'Last 24HR', value= 'Fill', inline= True)
        embed.set_footer(text = self._footer)
        
        print(f'Sent Embed {time.ctime()}')
        return embed

    def help_embed(self): #help embed for users
        embed = discord.Embed(
            title = 'Crypto Tracker',
            description = 'Help Page',
            colour = discord.Colour.orange()
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.add_field(name = 'Bitcoin Info', value= '!BTC', inline= True)
        embed.add_field(name = 'Cardano Info', value= '!ADA', inline= True)
        embed.add_field(name = 'Ethereum Info', value= '!ETH', inline= True)
        embed.add_field(name = 'Monitor Crypto', value= '!Monitor - Will prompt options (Coming Soon)', inline= True)
        embed.set_footer(text = self._footer)
        
        print(f'Sent Embed {time.ctime()}')
        return embed


    

client = CryptoTracker()
client.run(discord_key) 
