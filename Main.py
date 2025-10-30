import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 **Welcome to @Botlyx Demo!**\n\n"
        "💎 **@Botlyx** is live on Fragment Auction:\n"
        "💰 **Current Price: 1500 TON**\n"
        "🔗 **Bid Now:** fragment.com/username/Botlyx\n\n"
        "🎮 **Bot Features:**\n"
        "• Automated TON Trading\n"
        "• NFT Gaming Integration\n"
        "• Smart Telegram Automation\n\n"
        "**Bid and own @Botlyx!** 👑\n\n"
        "/price - Check current bid\n"
        "/demo - Simulate TON trade"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 **@Botlyx Current Price: 1500 TON (~$3210)**\n"
        "🔥 **Live Auction:** fragment.com/username/Botlyx\n"
        "**First bid wins!**"
    )

async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 **TON Trade Demo:**\n"
        "You traded 100 TON → +15% profit! 📈\n"
        "**Build real bots with @Botlyx!**\n"
        "fragment.com/username/Botlyx"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("demo", demo))
    app.run_polling()

if __name__ == '__main__':
    main()
