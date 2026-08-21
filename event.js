const { EmbedBuilder } = require("discord.js");
const { getServerStatus } = require("./minecraft");

async function sendServerStatus(client) {
    const channelId = process.env.MINECRAFT_CHANNEL_ID;

    if (!channelId) {
        console.log("⚠️ MINECRAFT_CHANNEL_ID is missing from .env");
        return;
    }

    const channel = await client.channels.fetch(channelId).catch(() => null);

    if (!channel) {
        console.log("❌ Minecraft Discord channel not found.");
        return;
    }

    const server = await getServerStatus();

    const embed = new EmbedBuilder()
        .setTitle(server.online ? "🟢 Minecraft Server Online" : "🔴 Minecraft Server Offline")
        .setDescription(
            server.online
                ? `The Minecraft server is currently **online**.\n\n👥 Players: **${server.players.online}/${server.players.max}**\n🎮 Version: **${server.version}**`
                : "The Minecraft server is currently **offline**."
        )
        .setTimestamp();

    await channel.send({ embeds: [embed] });
}

module.exports = {
    sendServerStatus
};