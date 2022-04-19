import discord
import asyncio
import random

from discord import message

client = discord.Client()

token = 'OTY1NjgzNjY1NDc4NzYyNTQ3.Yl2w_w.OVBLB1cF3O0B3OvZdgvW66skkUk' #봇 토큰

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('서버 안정화') #봇 서버 안정화 작업하는중 입력
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "서버안정화!": #내가 '서버안정화!'이라고 말하면
        await message.channel.send (f"서버 안정화작업 중") #봇이 '서버 안정화작업 중'라고 대답

client.run(token)