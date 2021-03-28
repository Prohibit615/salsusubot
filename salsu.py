import discord
import asyncio
import youtube_dl
import datetime
import pytz

client = discord.Client()

token = "ODI0NTgzOTcxNDE2ODM0MDc4.YFxfqg.hD1duYu_EAT_Bv9UoQTZpjL1vmY"


@client.event
async def on_ready():
    print(client.user.name)
    print('SALSU MODE ON')
    game = discord.Game('SALSU')
    await client.change_presence(status=discord.Status.online, activity=game)  # 현활

@client.event
async def on_message(message):
    if message.content.startswith("!살수청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[6:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="SALSU 삭제 완료",
                                  description="채팅 {}개가\nSALSU재단 {}님의 요청으로 SALSU삭제 조치 되었습니다".format(amount,
                                                                                                   message.author),
                                  color=0x000000)
            embed.set_footer(text="MadeBy,PROHIBIT",
                             icon_url="https://media.discordapp.net/attachments/786895608564285470/817046140985933874/SALSU.gif")
            await message.channel.send(embed=embed)
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    if message.content.startswith("!살수공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[6:]
            channel = client.get_channel(823831645949526026)
            embed = discord.Embed(title="**SALSU 공지**",
                                  description="\n―――――――――――――――――――――――――――\n\n{}\n\n―――――――――――――――――――――――――――".format(
                                      notice), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="SALSU : {}".format(message.author),
                             icon_url="https://media.discordapp.net/attachments/786895608564285470/817046140985933874/SALSU.gif")
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/786895608564285470/817046140985933874/SALSU.gif")
            await channel.send("@everyone", embed=embed)
            await message.author.send(
                "**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(
                    channel, message.author, notice))



        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    Warning, age, nick, reason = message.content.split()
    embed = discord.Embed(color=0xff0000, title="SALSU 살생부 등록 안내", timestamp=message.created_at)
    embed.add_field(name="고유번호", value=age, inline=True)
    embed.add_field(name="닉네임", value=nick, inline=True)
    embed.add_field(name="사유", value=reason, inline=False)
    await message.channel.send(embed=embed)  # 살생부등록


client.run(token)