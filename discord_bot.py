import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import time
from Keys import discord_key
from get_requests import get_crypto_data, all_crypto_prices


class CryptoTracker(discord.Client, discord.Embed):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self._dev = "DY"
        self._dev_url = "https://github.com/GoldenTBE"
        self._dev_pfp = "https://avatars.githubusercontent.com/u/54921144?v=4"
        self._footer = 'Version 0.0.2 | Built by Dylan '
        self._crypto_thumbnails = {'BTC':"https://s2.coinmarketcap.com/static/img/coins/200x200/1.png", 
        'ETH': 'https://cdn.thecollegeinvestor.com/wp-content/uploads/2017/06/Ethereum.png',
        'ADA': 'https://www.kaupangkrypto.no/blogg/content/images/2021/03/Cardano--ADA-.png'}
        

    
    async def on_ready(self): #Function tells user if bot is logged in. 
        print(f'Logged in as {self.user}')
    
    
    async def on_message(self, message): #awaiting messages from user
        try:
            if message.content == '!help': #HELP IN FOR USERS
                print(f'Help Command Used by: {message.author}')
                await message.channel.send(embed= self.help_embed())

            elif message.content == '!BTC': #BTC INFO 
                print(f'BTC Info called by: {message.author}')
                await message.channel.send(embed = self.crypto_price('BTC'))
                
            elif message.content == '!ADA': #ADA INFO
                print(f'ADA Info called by: {message.author}')
                await message.channel.send(embed = self.crypto_price('ADA'))

            elif message.content == '!ETH': 
                print(f'ETH Info called by: {message.author}')
                await message.channel.send(embed = self.crypto_price('ETH'))

            elif message.content == '!error':
                print(f'Error Info called by: {message.author}')
                await message.channel.send(embed = self.error_embed()) 

            elif message.content == '!Monitor':
                await message.channel.send(embed = self.error_embed())    
        except:
            await message.channel.send('<@281626075996356610>')
            await message.channel.send(embed = self.error_embed())

    

    def crypto_price(self,currency): 
        returned_data = get_crypto_data(currency)
        embed = discord.Embed(
            title = 'Crypto Tracker',
            description = 'Tracking Crypto with ease.',
            colour = discord.Colour.blue()    
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)
        embed.set_thumbnail(url = self._crypto_thumbnails[currency])

        for key, value in returned_data.items():
            embed.add_field(name = key, value = value, inline = True)
    
    
        print(f'Sent Embed {time.ctime()}')
        return embed




    def help_embed(self): 
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




    def error_embed(self):
        embed = embed = discord.Embed(
            title = 'Crypto Tracker',
            description = 'Error, alerting dev!',
            colour = discord.Colour.red()
        )
        embed.set_author(name = self._dev, url = self._dev_url, icon_url = self._dev_pfp)
        embed.set_footer(text = self._footer)

        return embed


    







if __name__ == "__main__":
    client = CryptoTracker()
    client.run(discord_key) 
