import { Connection, Keypair, Transaction } from "@solana/web3.js";
import { executeTrade } from "./api";

class TradingBot {
    private connection: Connection;
    private wallet: Keypair;

    constructor(connection: Connection, wallet: Keypair) {
        this.connection = connection;
        this.wallet = wallet;
    }

    async start() {
        console.log("SAIT Trading Bot started...");
        // Beispiel: Handel ausführen
        await executeTrade(this.connection, this.wallet, 100, 50);
    }
}

export default TradingBot;
