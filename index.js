require("dotenv").config();

const {
    Client,
    GatewayIntentBits,
    Partials
} = require("discord.js");

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

client.once("ready", () => {
    console.log(`✅ Logged in as ${client.user.tag}`);
    console.log("🤖 Minecraft Discord Bot is online!");
});

client.on("error", (error) => {
    console.error("❌ Discord Client Error:", error);
});

if (!process.env.DISCORD_TOKEN) {
    console.error("❌ DISCORD_TOKEN is missing from .env");
    process.exit(1);
}

client.login(process.env.DISCORD_TOKEN);