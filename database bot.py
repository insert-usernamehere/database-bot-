import discord
from discord.ext import commands
from time import sleep
import os
import datetime
import wget
import threading
from zipfile import ZipFile
from pathlib import Path
import shutil


def closefile():
    sleep(300)
    if os.path.exists(finalfilepath):
        os.remove(finalfilepath)
    else:
        pass

def closefile1():
    sleep(300)
    if os.path.exists(finalfilepath1):
        os.remove(finalfilepath1)
    else:
        pass
    


client = commands.Bot(command_prefix='.')


@client.command() 
async def addcharacter(ctx):
    await ctx.send("adding to database please wait")
    try:
        await ctx.message.attachments[0].save("newcharacter.zip")
                                         
        zf = ZipFile('newcharacter.zip', 'r')
        zf.extractall('public/singlecharacter')
        zf.close()
        if os.path.exists("newcharacter.zip"):
            os.remove("newcharacter.zip")
        else:
            pass
        if os.path.exists("public/characters.zip"):
            os.remove("public/characters.zip")
        else:
            pass
        shutil.make_archive('public/characters', 'zip', 'public/singlecharacter')
        await ctx.send("added to database")
    except Exception:
        await ctx.send("something went wrong! this probably means you didn't attach a file or discord api is broken")

@client.command() 
async def addcourtroom(ctx):
    await ctx.send("adding to database please wait")
    try:
        await ctx.message.attachments[0].save("newcourtroom.zip")
                                         
        zf = ZipFile('newcourtroom.zip', 'r')
        zf.extractall('public/singlecourtroom')
        zf.close()
        if os.path.exists("newcourtroom.zip"):
            os.remove("newcourtroom.zip")
        else:
            pass
        if os.path.exists("public/courtroom.zip"):
            os.remove("public/courtroom.zip")
        else:
            pass
        shutil.make_archive('public/courtrooms', 'zip', 'public/singlecourtroom')
        await ctx.send("added to database")
    except Exception:
        await ctx.send("something went wrong! this probably means you didn't attach a file or discord api is broken")

@client.command()     
async def addsound(ctx):
    await ctx.send("adding to database please wait")
    try:
        await ctx.message.attachments[0].save("newsound.zip")
                                         
        zf = ZipFile('newsound.zip', 'r')
        zf.extractall('public/singlesound')
        zf.close()
        if os.path.exists("newsound.zip"):
            os.remove("newsound.zip")
        else:
            pass
        if os.path.exists("public/sounds.zip"):
            os.remove("public/sounds.zip")
        else:
            pass
        shutil.make_archive('public/sounds', 'zip', 'public/singlesound')
        await ctx.send("added to database")
    except Exception:
        await ctx.send("something went wrong! this probably means you didn't attach a file or discord api is broken")

@client.command()
async def lazyaddsound(ctx):
    soutype = ctx.message.content[14:]
    findsou1 = 'public/singlesound/'+str(soutype)
    if os.path.isdir(findsou1):
        try:
            name = ctx.message.attachments[0].filename
            await ctx.message.attachments[0].save(name)
            shutil.move(f"{name}", f"{findsou1}/{name}")
            if os.path.exists("public/sounds.zip"):
                os.remove("public/sounds.zip")
            else:
                pass
            shutil.make_archive('public/sounds', 'zip', 'public/singlesound')
            await ctx.send("added to database")
        except Exception:
            await ctx.send("something went wrong! this probably means you didn't attach a file or discord api is broken")
    else:
        await ctx.send('thats not a sound option avalible options are "blips", "music", and "general"')

@client.command()     
async def setip(ctx):
    ip = userInput = ctx.message.content[7:]
    with open("public/serverlist.txt", "w+") as hisc:
        hisc.write(str(ip)+":best bois courthouse")
    await ctx.send("changed ip to "+str(ip))

@client.command()     
async def getchrasset(ctx):
    weburl = ctx.message.content[13:]
    filedirweburl = weburl.replace("%20", " ")
    if os.path.isfile('public/singlecharacter/'+str(filedirweburl)):
        betterweburl = weburl.replace(" ", "%20")
        await ctx.send("http://fierce-push.auto.playit.gg:47746/singlecharacter/"+str(betterweburl))
    else:
        await ctx.send("oops! that file does not exist make sure its spelled correctly")

@client.command()     
async def getcortasset(ctx):
    weburl = ctx.message.content[14:]
    filedirweburl = weburl.replace("%20", " ")
    if os.path.isfile('public/singlecharacter/'+str(filedirweburl)):
        betterweburl = weburl.replace(" ", "%20")
        await ctx.send("http://fierce-push.auto.playit.gg:47746/singlecourtroom/"+str(betterweburl))
    else:
        await ctx.send("oops! that file does not exist make sure its spelled correctly")
        
@client.command()     
async def getsound(ctx):
    sound = ctx.message.content[10:]
    sounddirweb = sound.replace("%20", " ")
    if os.path.isfile('public/singlesound/'+str(sounddirweb)):
        bettersound = sound.replace(" ", "%20")
        await ctx.send("http://fierce-push.auto.playit.gg:47746/singlesound/"+str(bettersound))
    else:
        await ctx.send("oops! that file does not exist make sure its spelled correctly")

@client.command()     
async def downloadcharacter(ctx):
    filepath = ctx.message.content[19:]
    if filepath == '':
        filepath = 'something that does not exist'
    else:
        pass
    fullfilepath = 'public/singlecharacter/'+str(filepath)
    if os.path.isdir(fullfilepath):
      await ctx.send("grabbing the character please wait")
      shutil.make_archive(fullfilepath, 'zip', fullfilepath)
      global finalfilepath
      finalfilepath = str(fullfilepath)+'.zip'
      if Path(fullfilepath).stat().st_size > 3850:
          urlpath = finalfilepath.replace(" ", "_")
          os.rename(finalfilepath,urlpath)
          newurlpath = finalfilepath.replace("/public", "")
          await ctx.send("http://fierce-push.auto.playit.gg:47746/"+str(urlpath))
          await ctx.send("note: this link will become invalid in 5 minutes")
          delfile = threading.Thread(target=closefile)
          delfile.start()
      else:
          await ctx.send(file=discord.File(str(finalfilepath)))  
          if os.path.exists(finalfilepath):
             os.remove(finalfilepath)
          else:
            pass
    else:
        await ctx.send("sorry, but thats not a character in my database")

@client.command()     
async def downloadcourtroom(ctx):
    filepath = ctx.message.content[19:]
    fullfilepath = 'public/singlecourtroom/'+str(filepath)
    if os.path.isdir(fullfilepath):
      await ctx.send("grabbing the courtroom please wait")
      shutil.make_archive(fullfilepath, 'zip', fullfilepath)
      global finalfilepath1
      finalfilepath1 = str(fullfilepath)+'.zip'
      if Path(fullfilepath1).stat().st_size > 3850:
          urlpath = finalfilepath1.replace(" ", "_")
          os.rename(finalfilepath1,urlpath)
          newurlpath = finalfilepath1.replace("/public", "")
          await ctx.send("http://fierce-push.auto.playit.gg:47746/"+str(urlpath))
          await ctx.send("note: this link will become invalid in 5 minutes")
          delfile = threading.Thread(target=closefile1)
          delfile.start()
      else:
          await ctx.send(file=discord.File(str(finalfilepath)))  
          if os.path.exists(finalfilepath):
             os.remove(finalfilepath)
          else:
            pass
    else:
        await ctx.send("sorry, but thats not a courtroom in my database")

@client.command()
async def listchr(ctx):
    findchr = os.listdir('public/singlecharacter')
    await ctx.send('```'+str(findchr)+'```')

@client.command()
async def listcourt(ctx):
    findchr = os.listdir('public/singlecourtroom')
    await ctx.send('```'+str(findchr)+'```')

@client.command()
async def listsound(ctx):
    soutype = ctx.message.content[11:]
    findsou1 = 'public/singlesound/'+str(soutype)
    if os.path.isdir(findsou1):
        findsou = os.listdir('public/singlesound/'+str(soutype))
        soulenght = len(str(findsou))
        if soulenght > 1990:
            with open("public/soulist.txt", "w+") as souname:
                souname.write(str(findsou))
            await ctx.send(file=discord.File("public/soulist.txt"))  
            if os.path.exists("public/soulist.txt"):
                os.remove("public/soulist.txt")
            else:
                pass
        else:
            await ctx.send('```'+str(findsou)+'```')
    else:
        await ctx.send('thats not a sound option avalible options are "blps", "music", and "general"')

    
client.run('bottoken')
