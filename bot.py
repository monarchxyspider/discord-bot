import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


class HomeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(
            discord.ui.Button(
                label="Support Server",
                emoji="<:red_shulker:1484155745661620417>",
                style=discord.ButtonStyle.link,
                url="https://discord.gg/54vJcse3"
            )
        )


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! `{round(bot.latency * 1000)}ms`")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Reply only if the bot is mentioned by itself
    if bot.user in message.mentions and message.content.strip() == f"<@{bot.user.id}>":

        embed = discord.Embed(
            title="Hey There!<:sword:1486605962809704520>",
            description="Thanks for mentioning me!\n\nUse **!ping** to test my latency.",
            color=0xE53935
        )

        embed.add_field(
            name="`status` : <:remove:1486921110023831713> Online",
            value="<:remove:1486921110023831713> Online",
            inline=True
        )

        embed.add_field(
            name="🏓 Ping",
            value=f"`{round(bot.latency * 1000)} ms`",
            inline=True
        )

        embed.set_thumbnail(url=bot.user.display_avatar.url)

        await message.reply(embed=embed, view=HomeView())

    await bot.process_commands(message)


bot.run(os.getenv("TOKEN"))