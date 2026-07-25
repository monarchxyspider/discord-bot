import os
import discord
from discord.ext import commands
from discord.http import Route

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def send_v2(channel, payload, reply_to=None):
    if reply_to:
        payload["message_reference"] = {
            "message_id": str(reply_to.id),
            "channel_id": str(reply_to.channel.id),
            "fail_if_not_exists": False,
        }
        payload["allowed_mentions"] = {"replied_user": False}
    await bot.http.request(
        Route("POST", "/channels/{channel_id}/messages", channel_id=channel.id),
        json=payload,
    )

def build_info_panel(guild, latency_ms):
    status = "🟢 Operational" if latency_ms < 200 else "🔴 Degraded"
    guild_name = guild.name if guild else "DMs"

    return {
        "flags": 1 << 15,
        "components": [
            {
                "type": 17,
                "accent_color": 0xE53935,
                "components": [
                    {
                        "type": 9,
                        "components": [
                            {"type": 10, "content": "**Hey There! ⚔️**"},
                            {"type": 10, "content": "I'm **Shade Mist** — your all-in-one server companion.\n\u200b"},
                        ]
                    },
                    {"type": 14, "divider": True, "spacing": 1},
                    {
                        "type": 9,
                        "components": [
                            {
                                "type": 10,
                                "content": (
                                    f"**Prefix:** `!`\n"
                                    f"**Help:** `!help`\n"
                                    f"**Commands:** `{len(bot.commands)}` loaded\n"
                                    f"\u200b\n"
                                    f"**Server:** `{guild_name}`\n"
                                    f"**Status:** {status}\n"
                                    f"**Ping:** `{latency_ms}ms`"
                                )
                            }
                        ]
                    },
                ]
            },
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "style": 5,
                        "label": "Support Server",
                        "emoji": {"id": "1484155745661620417", "name": "red_shulker"},
                        "url": "https://discord.gg/54vJcse3"
                    },
                    {
                        "type": 2,
                        "style": 5,
                        "label": "Add Me",
                        "emoji": {"name": "🤖"},
                        "url": "https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=277025770560&scope=bot"
                    }
                ]
            }
        ]
    }


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    payload = {
        "flags": 1 << 15,
        "components": [
            {
                "type": 17,
                "accent_color": 0xE53935,
                "components": [
                    {
                        "type": 9,
                        "components": [
                            {"type": 10, "content": f"🏓 **Pong!**\n`{latency}ms`"}
                        ]
                    }
                ]
            }
        ]
    }
    await send_v2(ctx.channel, payload, reply_to=ctx.message)


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions and message.content.strip() == f"<@{bot.user.id}>":
        payload = build_info_panel(message.guild, round(bot.latency * 1000))
        await send_v2(message.channel, payload, reply_to=message)

    await bot.process_commands(message)


bot.run(os.getenv("TOKEN"))