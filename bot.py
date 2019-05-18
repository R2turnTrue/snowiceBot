import discord
import asyncio
import os

#VDV
#DSFFD

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("설빙아 도와줘 ㄱㄱ")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("설빙아 안녕"):
        await message.channel.send("안녕하신가! 나는 설빙이다!")
    if message.content.startswith("설빙아 뭐해"):
        await message.channel.send("PvP 연습해")
    if message.content.startswith("설빙아 놀자"):
        await message.channel.send("./p join bidulgi_gamer 를 입력해라!")
    if message.content.startswith("설빙아 도와줘"):
        embed = discord.Embed(title="설빙아 안녕", description="안녕 이라 하기!")

        await message.channel.send("```설빙봇 도움말\n설빙아 뭐해: 뭐하냐고 물어볼 수 있어요.\n설빙아 놀자: 설빙이랑 놀고 싶다면? 이 명령어로!\n설빙아 안녕!: 안녕! 설빙!\n설빙봇 by redwikitv#0345 ```")

        ### embed.set_author(name="도움말",, icon_url = "http://redwikitv.github.io/photo.png") ###
        #embed = discord.Embed(title="설빙봇 도움말", description="설빙봇의 도움말입니다!")
        #embed.set_thumbnail(url="http://redwikitv.github.io/photo.png")
        #embed.add_field(name="설빙아 뭐해", value = "뭐하냐고 물어볼 수 있어요.", inline = True)
        #embed.add_field(name="설빙아 놀자", value = "설빙이랑 놀고 싶다면? 이 명령어로!", inline = True)
        #embed.add_field(name="설빙아 안녕!", value = "안녕! 설빙!", inline = True)
        #embed.set_footer(text="설빙봇 by redwikitv#0345 문의 및 제안은 여기로!")
        #await client.send_message(message.channel, embed=embed)
        await client.say(embed=embed)
    if message.content.startswith("md 테스트"):
        await message.channel.send("```s hello \nwtf ```")

access_token = os.environ[ACCESS_TOKEN]
        
client.run("NTc5MDk2ODM5MDU2NTIzMjc1.XN9ngQ.2ZcMUcZbHrNYZgPmjFizMVjvx44")

#@client.event
#async def on_ready():
#    game = discord.Game("설빙아 도와줘 ㄱㄱ")
#    await client.change_presence(status=discord.Status.online, activity=game)
#    client.change_presence()
#    print (client.user)
#    print ("bot is ready")

#@client.event
#async def on_message(message):
#    if message.content.startswith("설빙아 안녕"):
#        await message.channel.send("안녕하신가! 나는 설빙이다!")
#    if message.content.startswith("설빙아 뭐해"):
#        await message.channel.send("뭐하긴 pvp하는데")
#    if message.content.startswith("설빙아 놀자"):
#        await message.channel.send("./p join bidulgi_gamer 를 쳐라!")

#client.run('NTc5MDk2ODM5MDU2NTIzMjc1.XN9R8w.HEI71JaEzdp0dazt6Mfkc9SlQVo')
