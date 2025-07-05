from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Replace with your real token
TOKEN = "7783212541:AAGbRcTt3aZRBcdxiOWDZTWHULmvQo36Zg8"

# ✅ Channel username with @
CHANNEL_ID = "@sarkari_jobs_4"

# /start command (for users)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Hello! I'm your Sarkari Job Bot!")

# /post command (sends message to your channel)
async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "📢 New Sarkari Naukri Alert!\n🔗 Join now: https://t.me/sarkari_jobs_4"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message)
    await update.message.reply_text("✅ Message sent to channel!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))

    print("🤖 Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
