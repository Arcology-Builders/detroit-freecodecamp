import discord
import os
import dotenv
import requests
import json

client = discord.Client()

dotenv.load_dotenv()

GUILD = os.getenv('DISCORD_GUILD')
my_guild = None

response = requests.get('https://api.freecodecamp.org/api/users/get-public-profile?username=paulpham')
profile = json.loads(response.text)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    my_guild = None
    for guild in client.guilds:
        if guild.name == GUILD:
            my_guild = guild
            break

    if my_guild is None:
        exit(f'Our guild {GUILD} was not found.')

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Arcology Builders and the Detroit FreeCodeCamp Meetup'
    )
    await member.dm_channel.send(
        f'You look good in the color {member.color}'
    )

import serial

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('who'):
        await message.channel.send('I am the One.')
    elif message.content.startswith('omnibot'):
        ser = serial.Serial('/dev/ttyACM0')  # open serial port
        print(ser.name)         # check which port was really used
        reply = ""
        try:
            cmd = message.content.split(' ')[1]
            ser.write(bytes(cmd))
            reply = "Sent " + cmd
        except ValueError as e:
            reply = "Error " + str(e) + ". Try 'omnibot <{f,b,l,r,p,q}#>'"

        ser.close()             # close port
        await message.channel.send(reply)
    else:
        await message.channel.send(
            'Why do you want to know: "' + message.content + '" ?'
            )

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(os.getenv('DISCORD_TOKEN'))
