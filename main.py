import discord
import token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


symbol = "$"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content[:1] == symbol:
        msg = message.content[1:].split()
        
        if msg[0] == "test":
            print("test")

client.run(token.t)

