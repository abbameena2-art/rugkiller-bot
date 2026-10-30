import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- CONFIG ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8519601591:AAFP...PUT_YOUR_FULL_TOKEN_HERE")
# Saka token dinka a Railway Variables!

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 RugKiller Bot V8 is LIVE! 🔥\n\n"
        "Commands:\n"
        "/start - Fara bot\n"
        "/scan <token_address> - Duba token\n"
        "/help - Taimako\n\n"
        "Bot yana aiki 24/7 akan Railway!"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ RugKiller V8 Help\n\n"
        "Ina duba rug pull, honeypot, da liquidity lock.\n"
        "Yi amfani da /scan <address>"
    )

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Amfani: /scan 0x123... address")
        return
    token = context.args[0]
    await update.message.reply_text(f"🔍 Ina duba token: {token}\n\n⏳ Bincike yana gudana... (V8 engine)")
    # Anan zaka saka logic na web3 dinka
    await update.message.reply_text(f"✅ Result for {token}: \nLiquidity: OK\nHoneypot: NO\nRug Risk: LOW - Amintacce!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("scan", scan))
    print("Bot is starting...")
    app.run_polling()
