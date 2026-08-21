const {
    status,
    queryFull
} = require("minecraft-server-util");

const HOST = process.env.MINECRAFT_SERVER;
const PORT = Number(process.env.MINECRAFT_PORT) || 25565;

async function getServerStatus() {
    try {
        const result = await status(HOST, PORT, {
            timeout: 5000
        });

        return {
            online: true,
            host: HOST,
            port: PORT,
            players: {
                online: result.players.online,
                max: result.players.max
            },
            version: result.version.name,
            motd: result.motd.clean
        };
    } catch (error) {
        return {
            online: false,
            host: HOST,
            port: PORT,
            players: {
                online: 0,
                max: 0
            },
            version: null,
            motd: null
        };
    }
}

module.exports = {
    getServerStatus
};