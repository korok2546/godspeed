import discord
import random
import os
import json
from datetime import datetime,timedelta
import asyncio
from discord.ext import commands
from discord.utils import get
client = discord.Client()
command="?"
@client.event
async def on_ready():
    print("구인봇 준비")
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    else:
        if message.content.startswith(command):
            I=str(message.author.id)
            nick=str(message.author.display_name)
            name=str(message.author.name)
            tag=str(message.author)
            s=message.content
            data=s[1:].split()
            if data[0]=="사용법" or data[0]=="명령어" or data[0]=="help":
                embed2=discord.Embed(title="help", description="역할을 멘션해서 사용합니다\n?setup\n?게임이름 입장\n?게임이름 퇴장\n?추가 게임이름\n\n현재 게임 목록:\n롤\n그타\n레식\n어몽어스\n마크\n피파\n메이플\n음악", color=0xff56)
                await message.channel.send(embed=embed2)
            elif data[0]=="추가":
                guild=message.guild
                await guild.create_role(name=data[1])
                embed2=discord.Embed(title="입장", description="%s가 역할에 추가되었습니다."%(data[1]), color=0xff56)
                await message.channel.send(embed=embed2)

            elif data[0]=="setup":
                guild=message.guild
                await guild.create_role(name="롤")
                await guild.create_role(name="그타")
                await guild.create_role(name="레식")
                await guild.create_role(name="어몽어스")
                await guild.create_role(name="마크")
                await guild.create_role(name="피파")
                await guild.create_role(name="메이플")
                await guild.create_role(name="음악")
                embed2=discord.Embed(title="입장", description="셋업이 완료되었습니다.", color=0xff56)
                await message.channel.send(embed=embed2)
                
            elif data[1]=="입장":
                role = discord.utils.get(message.guild.roles, name=data[0])
                await message.author.add_roles(role)
                embed2=discord.Embed(title="입장", description="<@%s>님 ,%s에 입장하셨습니다."%(I,data[0]), color=0xff56)
                await message.channel.send(embed=embed2)

            elif data[1]=="퇴장":
                role = discord.utils.get(message.guild.roles, name=data[0])
                await message.author.remove_roles(role)
                embed2=discord.Embed(title="퇴장", description="<@%s>님 ,%s에서 퇴장하셨습니다."%(I,data[0]), color=0xff0000)
                await message.channel.send(embed=embed2)
            else :
                embed2=discord.Embed(title="경고", description="올바르지 않은 명령어입니다.\n\n?게임이름 입장, ?게임이름 퇴장", color=0xE09500)
                await message.channel.send(embed=embed2)
client.run("")
