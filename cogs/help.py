import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):

        embed = discord.Embed(
            title="❤️ ShadeMist Help",
            description="Welcome to **ShadeMist**!\nChoose a category below.",
            color=0xE53935
        )

        embed.add_field(
            name="🛡 Moderation",
            value="`ban`\n`kick`\n`timeout`\n`clear`\n`warn`",
            inline=True
        )

        embed.add_field(
            name="🎫 Tickets",
            value="`ticket`\n`close`\n`claim`",
            inline=True
        )

        embed.add_field(
            name="⚙ Utility",
            value="`ping`\n`userinfo`\n`serverinfo`",
            inline=True
        )

        embed.set_footer(text="ShadeMist • Version 2.0")

        view = discord.ui.View()

        view.add_item(
            discord.ui.Button(
                label="Support Server",
                emoji="❤️",
                url="https://discord.gg/54vJcse3"
            )
        )

        await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Help(bot))