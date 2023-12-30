import epitran
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from tts import get_tts_sound
from pydub import AudioSegment
from pydub.playback import play
from apikeys import *


epi = epitran.Epitran('eng-Latn')

# initialize the discord bot
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("The bot is ready for use!")
    print("_________________________")
    
    
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('wav_files/starter.wav')
        player = voice.play(source)
    else:
        await ctx.send("Sorry dude SrikarBot's glorious voice can only be accessed by those in voice channels")
    
    
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Until next time losers")
    else:
        await ctx.send("I am not in a voice channel dumbdumb")
        

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if client.user.mentioned_in(message):
        await message.channel.send("Currently SrikarBot only functions in voice channels, join one to see what I can do")
    
    audio = get_tts_sound(epi, message.content)
    audio.export(out_f = 'temp_sounds/temp.wav', format='wav')
    
    voice_channel = message.guild.voice_client
    if not voice_channel:
        channel = message.author.voice.channel
        voice = await channel.connect()
    source = FFmpegPCMAudio('temp_sounds/temp.wav')
    player = voice_channel.play(source)
    
        
        
    
    
    
    

client.run(BOTTOKEN)