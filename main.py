import discord, os, time, random, math, asyncio
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
from MAL import MyAnimeList
from Trivias import T
from Words import word

client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
client.remove_command('help')

bot_status = cycle(["Owner Coding", "Owner Relearning Python", "Owner Depressed", "Owner Feeling Happy", "Anime with Owner", "Owner Learning Discord.py"])

@tasks.loop(seconds=200)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(bot_status)))


@client.event
async def on_ready():
  print("Bot awake!")
  change_status.start()
#========================COMMAND-CATEGORIES-SCRIPTS===================================#


@client.event
async def on_command_error(ctx, error):
  await ctx.send(
    f"An error occurred: {str(error)} , Please use **-cmds** to check the command list!",
    delete_after=20)


@client.command()
async def cmds(ctx):
  page = discord.Embed(title='Command List',
                       description='Try out these commmands below for fun',
                       colour=discord.Colour.red())
  page.set_thumbnail(
    url=
    'https://cdn.discordapp.com/avatars/1053645706247798794/2c153e5a2dbe1a66adeebde254bbffc2.png?size=1024'
  )
  page.set_footer(
    text="Made By SleepyAsh#6298",
    icon_url=
'https://cdn.discordapp.com/avatars/688590952063041538/c2424dfe6e2aded95825a204389d57e6.png?size=1024'
  )
  page.set_author(
    name='Magician',
    icon_url=
    'https://cdn.discordapp.com/attachments/1053510363938824232/1053931006270386247/HD-wallpaper-hisoka-anime-hunterxhunter.jpg'
  )
  page.add_field(name="Fun", value="`Fun` `shuffle` `slap` `repeat` `trivia` `anime`", inline=False)
  page.add_field(name="Math", value="`Math` `add` `subtract` `divide` `multiply` `square` `expo`", inline=False)
  page.add_field(name="Utility", value="`Utility` `timer`", inline=False)

  await ctx.channel.send(embed=page)


@client.command()
async def Fun(ctx):
  page = discord.Embed(title='Fun Commands',
                       description='Try out these commmands below for fun',
                       colour=discord.Colour.red())
  page.set_thumbnail(
    url=
    'https://cdn.discordapp.com/avatars/688590952063041538/fb619bb74db25b7a7ef4804abe2c4946.png?size=1024'
  )
  page.set_footer(
    text="Made By SleepyAsh#6298",
    icon_url=
'https://cdn.discordapp.com/avatars/688590952063041538/c2424dfe6e2aded95825a204389d57e6.png?size=1024'
  )
  page.set_author(
    name='Magician',
    icon_url=
    'https://cdn.discordapp.com/attachments/1053510363938824232/1053931006270386247/HD-wallpaper-hisoka-anime-hunterxhunter.jpg'
  )
  page.add_field(name="-slap <ping someone>",
                 value="slap 'em cuz they deserve it >:D",
                 inline=False)
  page.add_field(name="-shuffle",
                 value="Gues the word that is shuffled by the magician!",
                 inline=False)
  page.add_field(name="-repeat <msg>",
                 value="The magician will repeat your message",
                 inline=False)
  page.add_field(name="-flip",
                 value="place your bets! the magician will flip the coin",
                 inline=False)
  page.add_field(name="-trivia",
                 value="guess the right answer to the question given!",
                 inline=False)
  page.add_field(name="-anime",
                 value="The magician will recommend you anime series or movies",
                 inline=False)
  await ctx.channel.send(embed=page)


@client.command()
async def Math(ctx):
  page = discord.Embed(
    title='Math Commands',
    description='Try out these commmands below for solving math equations',
    colour=discord.Colour.red())
  page.set_thumbnail(url='https://imgur.com/ObC1UUk.gif')
  page.set_footer(
    text="Made By SleepyAsh#6298",
    icon_url=
'https://cdn.discordapp.com/avatars/688590952063041538/c2424dfe6e2aded95825a204389d57e6.png?size=1024'
  )
  page.set_author(
    name='Magician',
    icon_url=
    'https://cdn.discordapp.com/attachments/1053510363938824232/1053931006270386247/HD-wallpaper-hisoka-anime-hunterxhunter.jpg'
  )
  page.add_field(name="-add <number> <number>",
                 value="the magician will add both numbers",
                 inline=False)
  page.add_field(name="-subtract <number> <number>",
                 value="the magician will subtract both numbers",
                 inline=False)
  page.add_field(name="-divide <number> <number>",
                 value="the magician will divide both numbers",
                 inline=False)
  page.add_field(name="-multiply <number> <number>",
                 value="the magician will multiply both numbers",
                 inline=False)
  page.add_field(name="-square <number>",
                 value="the magician will get the square root of that number",
                 inline=False)
  page.add_field(name="-expo <number> <power>",
                 value="the magician will raise that number entered to the power you entered",
                 inline=False)
  await ctx.channel.send(embed=page)


@client.command()
async def music(ctx):
  page = discord.Embed(
    title='Music Commands',
    description='Try out these commmands below for listening to music(WIP)',
    colour=discord.Colour.red())
  page.set_thumbnail(
    url=
'https://cdn.discordapp.com/avatars/688590952063041538/c2424dfe6e2aded95825a204389d57e6.png?size=1024'
  )
  page.set_footer(
    text="Made By SleepyAsh#6298",
    icon_url=
    'https://cdn.discordapp.com/avatars/1053645706247798794/2c153e5a2dbe1a66adeebde254bbffc2.png?size=1024'
  )
  page.set_author(
    name='Magician',
    icon_url=
    'https://cdn.discordapp.com/attachments/1053510363938824232/1053931006270386247/HD-wallpaper-hisoka-anime-hunterxhunter.jpg'
  )
  page.add_field(name="test", value="test", inline=False)
  page.add_field(name="test", value="test", inline=False)
  page.add_field(name="test", value="test", inline=False)
  await ctx.channel.send(embed=page)


#==================COMMANDS-SCRIPTS-FOR-FUN-CATEGORY==========================#

@client.command()
async def generate(ctx): 
  time.sleep(2)
  await ctx.send(random.randrange(100000, 9999999))
  
@client.command()
async def slap(ctx,
               members: commands.Greedy[discord.Member],
               *,
               reason='no reason'):
  gif = ["https://tenor.com/view/slap-gif-25249881","https://tenor.com/view/slap-cat-gif-20845849","https://tenor.com/view/slap-jjk-nicevagg-anime-gif-22368283","https://tenor.com/view/slap-gif-20126989","https://tenor.com/view/will-smith-gif-25237265","https://tenor.com/view/slap-gif-22830734"]
  slapped = ", ".join(x.name for x in members)
  await ctx.send(f'`{slapped} just got slapped for {reason}`')
  await ctx.send(random.choice(gif))


@client.command()
async def repeat(ctx,* , message):
  await ctx.message.delete()
  await ctx.channel.send(message)


@client.command()
async def trivia(ctx):
    question = random.choice(T)
    question_text = question['question']
    options = question['options']
    answer = question['answer']

    message = f"{question_text}\n\n"
    for i, option in enumerate(options):
        message += f"- {option}\n"
    await ctx.send(message)

    def check_answer(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_answer = await client.wait_for('message', check=check_answer, timeout=15)

        if user_answer.content.lower() == answer.lower():
            await ctx.send("Correct answer!")
        else:
            await ctx.send("Wrong answer! Try again with another Trivia")
    except asyncio.TimeoutError:
        await ctx.send("Time's up! You didn't answer in time.")


@client.command()
async def flip(ctx):
  async with ctx.typing():
    time.sleep(2)
    pick = ["Heads", "Tails"]
    await ctx.send(random.choice(pick))


@client.command()
async def anime(ctx):
  async with ctx.typing():
    time.sleep(1)
  await ctx.send(random.choice(MyAnimeList))
  async with ctx.typing():
    time.sleep(0.5)
  await ctx.send("\nHave you seen this Anime already?")
  def check_answer(m):
        return m.author == ctx.author and m.channel == ctx.channel
  while (True):
    user_answer = await client.wait_for('message', check=check_answer,     timeout=15)

    if user_answer.content.lower() == "yes":
      async with ctx.typing():
        time.sleep(1)
      await ctx.send("How about this one?\n")
      async with ctx.typing():
        time.sleep(0.5)
      await ctx.send(random.choice(MyAnimeList))
      continue
    elif user_answer.content.lower() == "no":
      async with ctx.typing():
        time.sleep(1)
      await ctx.send("Enjoy Watching!")
      break
    else:
      break

@client.command()
async def shuffle(ctx):
    
    picked = (random.choice(word))
    
    shuffled_word = ''.join(random.sample(picked, len(picked)))

    message = await ctx.send(f"Unscramble this word: `{shuffled_word}`")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_input = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await message.edit(content="Time's up! The magic trick failed.")
        return

    if user_input.content.lower() == picked.lower():
        await message.edit(content="Congratulations! You unscrambled the word correctly!")
    else:
        await message.edit(content=f"Oops! That's not the correct unscrambled word. It is {picked}")

@client.command()
async def timer(ctx, duration: int, unit: str = 's'):
    time_units = {
        's': 'seconds',
        'm': 'minutes',
        'h': 'hours'
    }

    if unit not in time_units:
        await ctx.send(f"Invalid time unit. Use `s` for seconds, `m` for minutes, or `h` for hours.")
        return

    time_unit = time_units[unit]
    await ctx.send(f"Timer set for {duration} {time_unit}.")

    if unit == 's':
        await asyncio.sleep(duration)
    elif unit == 'm':
        await asyncio.sleep(duration * 60)
    elif unit == 'h':
        await asyncio.sleep(duration * 3600)

    await ctx.send(f"{ctx.author.mention}, your {duration} {time_unit} timer is up!")



#=================COMMANDS-SCRIPTS-FOR-MATH-CATEGORY==========================#


@client.command()
async def add(ctx, a: int, b: int):
  await ctx.send(a + b)


@client.command()
async def subtract(ctx, a: int, b: int):
  await ctx.send(a - b)


@client.command()
async def divide(ctx, a: int, b: int):
  await ctx.send(a / b)


@client.command()
async def multiply(ctx, a: int, b: int):
  await ctx.send(a * b)

@client.command()
async def square(ctx, number: float):
    result = math.sqrt(number)
    if result.is_integer():
        await ctx.send(f"The square root of {number:.0f} is {int(result)}")
    else:
        await ctx.send(f"The square root of {number} is {result:.2f}")

@client.command()
async def expo(ctx, base: float, exponent: float):
    result = math.pow(base, exponent)
    if result.is_integer():
        await ctx.send(f"{base:.0f} raised to the power of {exponent:.0f} is {int(result)}")
    else:
        await ctx.send(f"{base} raised to the power of {exponent} is {result:.2f}")




#====================COMMANDS-SCRIPTS-FOR-MUSIC-CATEGORY==============================#

#===========ON-MESSAGE-SCRIPT==========#


@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return

  if message.content.startswith("test"):
    await message.channel.send("test complete!")
    
  if message.content.startswith('embed'):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="value", inline=False)
    await message.channel.send(embed=embedVar)
    
  if message.content.startswith("help"):
    await message.channel.send("`Later`")

  if message.content.startswith("ping"):
    await message.channel.send("pong!")

  if client.user.mentioned_in(message):
    await message.channel.send(f"Hello {message.author.mention}! My prefix is || - || don't tell it to anyone :shushing_face:")

keep_alive()
client.run(os.getenv("TOKEN"))
