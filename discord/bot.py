import discord, os, re
import json
from discord.ext import commands
import random
import asyncio

with open('config.txt') as config:
    lines = config.readlines()
    TOKEN = lines[0]
    #permet de faire en sorte que si quelqu'un a le script il ne possede pas le token de connexion au compte du bot, le token est dans un fichier qui est lu par ligne grace a "readlines"

with open('dico.json') as conf :
    dico = json.load(conf)
    #*(ouvre le dossier dico.json sous variable pour pouvoir l'utiliser dans le script)

with open('questions.json') as gr :
    line = json.load(gr)
    #*

intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='/', intents=intents)
#permet de définir le caractere a mettre devant une commande sur discord

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #affiche dans le termiçnal vs quand le bot est connecté a discord

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    #dit bonjour aux nouveaux membres

@commands.has_permissions(ban_members = True)
@client.event
async def on_message(message):
    member = message.author.mention
    member_=message.author
    await client.process_commands(message)

    if message.author == client.user:
        #empeche le bot de se répondre a lui même
        return
    mot = message.content.lower().split(' ')
    print(mot) #affiche tout ce qui est dit dans le terminal vs
    for i in mot:
        #prends en compte chaque mot du message
        if i in dico.keys():  
            #vérifie si un mot est dans les clés          
            if dico.get(i) == "warn":
                await message.delete()
                await message.channel.send(f"{member}! ce que tu viens de dire est innaproprié, cela merite un warn !")
                role = discord.Object(1108402192861364334)
                await member_.add_roles(role, reason="Derniere chance", atomic=False)
                #permet d'avertir une personne si elle dit un mot non accepté
            if member_.get_role(1108402192861364334):
                await member_.ban(reason=f"{member}ne respecte pas les regles du serveur")
            if dico.get(i) == "ban deff":
                await message.delete()
                await message.channel.send(f"{member}! C'est la fin de ton aventure parmis nous...")
                await member_.ban(reason=f"{member}ne respecte pas les regles du serveur")
                #ban une personne qui aurait dit quelque chose d'interdit
            if dico.get(i) == "mute":
                await message.delete()
                await message.channel.send(f"allez, ta gueule {member}, tu soules tout le monde")
                #empeche l'auteur d'un message chiant de parler pendant un certain temps
            if dico.get(i) == "feur":
                await message.delete()
                await message.channel.send("Attends... Quoi ?! Connard va")
                #commande de modération des messages dirigées par le dossier dico.json

    for i in mot:
        if i=="salut":
        #on respecte les gens
            await message.channel.send(f'Bonjour {member}!')

    for i in mot:
        if i == "bonne nuit":
        #parce que ici on est trop kawaï, donc on dit bonne nuit
            await message.channel.send(f'Bonne nuit mon chaton {member} <3 uwu !') 

    if message.content.lower().startswith('haut haut bas bas gauche droite gauche droite b a start'):
        #anti triche
        await message.reply(f'pas de cheat toleré ici !')

    if message.content.lower().startswith("les nazis c'est pas bien"):
        emoji = '\N{THUMBS UP SIGN}'
        #instancie l'émoji avec lequel le bot va réagir
        await message.add_reaction(emoji)
        #réagis avec l'émoji instancié plus haut 
    
    if message.content.lower().startswith('cours python'):
        #envoie le lien vers le cours zoom
        await message.channel.send("https://us02web.zoom.us/j/81873753575")
    
@client.command(name="ping", description= "Simple commande pour voir si le bot est actif")
async def ping(ctx):
    #commande simple pour savoir si le bot est actif
    await ctx.send("pong")
@client.command(name="snake", description= "commande qui permet d'acceder a un jeu de snake en ligne")
async def snake(ctx):
    #commande simple pour lancer snake sur google
    await ctx.send("https://g.co/kgs/aTjDNp")
@client.command(name="musique", description="commande permettant d'acceder a la meilleur page internet")
async def musique(ctx):
    #commande qui envoie un lien vers une page avec de la bonne musique
    await ctx.send("https://takeb1nzyto.space")
@client.command(name="piece",description= "lance un pile ou face")
async def piece(ctx):
    #commande simple de pile ou face
    piece = random.randint(0,1)
    if piece==0:
        resultat = "pile"
    else:
        resultat = "face"
    await ctx.send(resultat)
@client.command(name="quizz", description="Fonction qui permet de jouer a un jeu de quizz")
async def quizz(ctx):
    await ctx.send("tu auras 15 secondes pour répondre a la question, est-tu prêt ?")
    await asyncio.sleep(1)
    await ctx.send("3...")
    await asyncio.sleep(1)
    await ctx.send("2...")
    await asyncio.sleep(1)
    await ctx.send("1...")
    await asyncio.sleep(1) #decompte pour tenir le joueur pret a donner sa reponse
    question = random.choice(list(line.keys())) #prends une question au hasard dans le dossier questions ouvert sous la forme de la variable line
    #prends une questions au hasard dans le dossier question.json
    await ctx.send(question)
    b=0 #variable instancier pour savoir si le joueur a bien répondu ou pas(b est un terme choisi au hasard par celui qui a codé ce programme)
    def check(msg):
        return msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id
    try:
        msg = await client.wait_for("message", check=check, timeout=15.0)#timeout permet de définir le temps qu'à l'utilisateur pour répondre, ce temps est compté en seconde
        #pour faire en sorte que le bot prenne la reponse même si elle contenu dans une phrase
        msg = msg.content.lower().split(' ')
        for j in msg:
            #pareil que dans la fonction on_message
            if j.lower() in line.get(question):
                await ctx.send("bravo c'est la bonne réponse")
                b+=1 #variable qui affirme au bot que l'utilisateur a bien répondu a la question du quizz
            break
        if b==0:
            #empêche le bot d'envoyer le message d'erreur si l'utilisateur a bien répondu
            await ctx.send("Ah mince, ce n'était pas la bonne réponse")
    except asyncio.TimeoutError :
        #permet de cloturer le quizz si l'utilisateur met trop de temps a repondre
        await ctx.send("tu n'as pas repondu dans les temps le quizz est fini.") 
        #message qui anonc a l'utilisateur qu'il a pris trop de temps pour repondre  

client.run(TOKEN) #le bot se met en marche grace au token cache dans un autre dossier mis sous la forme de la variable token