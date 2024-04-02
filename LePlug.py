import discord
import os

discord_bot_token = os.environ.get('DISCORD_BOT_TOKEN')


# Définir les intentions de votre bot
intents = discord.Intents.default()
intents.messages = True  # Activer l'intention des messages
Role_citoyen = 1208836973071048814

destination_channel_id = 1221259458907344896

# Définir les ID des canaux à surveiller
channels_to_watch_fr = [
    (1208807100063420426, 1221933383211552818),   # New wave
    (1208775212829642792, 1221933669292183682),   # HyperPop
    (1208779707491815445, 1221933721335234672),    # NewJazz
    (1220846176576868413, 1221933795070972085),  # Brazilian funk
    (1208806735570010113, 1221933877384450048),       # #DVM
    (1208785226340245585, 1221933961262006272),      # PLUGG
    (1208783226622050335, 1221934147921121384),    # Jersey
    (1208810096864403466, 1221934293811593376),      # Drill
    (1208807707562217542, 1221934365068755025),        # trap
    (1208807762763587584, 1221934401353678899),        # R&B
    (1209533765034967041, 1221952805758308494),       # Afro
    (1208807432394903633, 1221934731235688458),      # Autre
    (1208813731690061864, 1221934471826116719)   # Mainsteam
]

channels_to_watch_us_uk = [
    (1208812759836262450, 1221933383211552818),   # New wave
    (1208812585366069281, 1221933669292183682),   # HyperPop
    (1208812672443744266, 1221933721335234672),    # NewJazz
    (1220845116638367804, 1221933795070972085),  # Brazilian funk
    (1208812795077075024, 1221933877384450048),       # #DVM
    (1208812728580448346, 1221933961262006272),      # PLUGG
    (1208812711794970654, 1221934147921121384),    # Jeresey
    (1208812869164994640, 1221934293811593376),      # Drill
    (1208812844813123605, 1221934365068755025),        # Rap
    (1209534111799320578, 1221934401353678899),       # Afro
    (1208812895706681364, 1221934731235688458),      # Autre
    (1208813801634271272, 1221934471826116719)   # Mainsteam
]

channel_dj = [
    (1208847528775131146, 1221939115390537819),       # Mix
]

channel_sorties = [
    (1208845427961503806, 1208836973071048814),      # Event
    (1208845124864442440, 1208836973071048814)      # Pop-Up
]

channel_da_image = [
    (1208828230111596685, 1221934902724005939),       # Clip
    (1208827934035419156, 1221934902724005939)  # Real Photographe
]

channel_beatmaker = [
    (1208815833854386277, 1221934808922456155),       # pepite fr
    (1208817784889544704, 1221934808922456155)  # pepite internationale
]

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Connecté en tant que {0.user}'.format(client))

@client.event
async def on_message(message):
    # Vérifiez si le message est dans l'un des canaux à surveiller
    for channel_id, role in channels_to_watch_fr:
        if message.channel.id == channel_id:
            message_to_send = f"<@&{role}> Viens voir ! Un nouveau son a été partagé dans le canal (FR) <#{channel_id}>"
            break
    else:
        for channel_id, role in channels_to_watch_us_uk:
            if message.channel.id == channel_id:
                message_to_send = f"<@&{role}> Viens voir ! Un nouveau son a été partagé dans le canal (US/UK) <#{channel_id}>"
                break
        else:
            for channel_id, role in channel_sorties:
                if message.channel.id == channel_id:
                    message_to_send = f"<@&{role}> Viens voir ! Un nouvel event viens de pop :boom: ! <#{channel_id}>"
                    break
            else:
                for channel_id, role in channel_da_image:
                    if message.channel.id == channel_id:
                        message_to_send = f"<@&{role}> Il y a du nouveau à la DA :video_camera: Venez voir ! <#{channel_id}>"
                        break
                else:
                    for channel_id, role in channel_beatmaker:
                        if message.channel.id == channel_id:
                            message_to_send = f"<@&{role}> Yo Pi'erre! you wanna come out here :musical_keyboard:  <#{channel_id}>"
                            break
                    else:
                        for channel_id, role in channel_dj:
                            if message.channel.id == channel_id:
                                message_to_send = f"<@&{role}> Mieux que ton mix aleatoire Spotify ! :musical_keyboard:  <#{channel_id}>"
                                break
                            else:
                                return 
    
    if destination_channel_id:
        destination_channel = client.get_channel(destination_channel_id)
        print(f"Sending message to {message_to_send}")
    if destination_channel:
        
        await destination_channel.send(message_to_send)

client.run(discord_bot_token)
