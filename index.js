require("dotenv").config();

const {
    Client,
    GatewayIntentBits,
    Partials
} = require("discord.js");

const { sendServerStatus } = require("./events");

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ],
    partials: [
        Partials.Channel
    ]
});

client.once("ready", async () => {
    console.log(`✅ Logged in as ${client.user.tag}`);
    console.log("🤖 Minecraft Discord Bot is online!");

    // Check Minecraft server status
    await sendServerStatus(client);

    // Check every 5 minutes
    setInterval(async () => {
        await sendServerStatus(client);
    }, 5 * 60 * 1000);
});

client.on("error", (error) => {
    console.error("❌ Discord Client Error:", error);
});

if (!process.env.DISCORD_TOKEN) {
    console.error("❌ DISCORD_TOKEN is missing from .env");
    process.exit(1);
}

if (!process.env.MINECRAFT_SERVER) {
    console.error("❌ MINECRAFT_SERVER is missing from .env");
    process.exit(1);
}

client.login(process.env.DISCORD_TOKEN);