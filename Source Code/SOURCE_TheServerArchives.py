import discord
import random 
import configparser
import time
import sys
import os

def return_all():
    return discord
    return random
    return configparser
    return time
    return pyautogui

config = configparser.ConfigParser()

print("Please wait while the bot connects to the servers...")

token = "x"

client = discord.Client()
prefix = '$'

@client.event
async def on_ready():
    print('{0.user} is recording in 4k HDR.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel.type) == 'private':
        await message.channel.send("haha imagine trying to clog up the archives with your pointless dms")
        return
    print(message.channel)
    print(message)
    print(message.content)
    config.read("THESERVERARCHIVESconfig.ini")
    counted = int(config.get("BOTconfig", "counted"))
    number = 'message',counted
    content = message, message.content
    config.set("MESSAGES", str(number), str(content))
    counted += 1
    config.set("BOTconfig", "counted", str(counted))
    config.write(open("THESERVERARCHIVESconfig.ini", "w"))

    if message.content.startswith(prefix):
        if 'test' in message.content:
            await message.channel.send("stop")
    else:
        return

client.run(token)
