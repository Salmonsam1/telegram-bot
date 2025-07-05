import asyncio
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes

# Your Telegram Bot Token
TOKEN = "7783212541:AAGbRcTt3aZRBcdxiOWDZTWHULmvQo36Zg8"

# Enable logging
logging.basicConfig(level=logging.INFO)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{user.id} - @{user.username}\n")

    button = InlineKeyboardButton("📲 Sarkari Job Channel Join Karein", url="https://t.me/sarkari_jobs_4")
    keyboard = InlineKeyboardMarkup([[button]])

    await update.message.reply_text(
        f"👋 Hello {user.first_name}!\n✅ Aapka registration ho gaya hai.\n👇 Hamare Sarkari Job Channel se judne ke liye button dabayein:",
        reply_markup=keyboard
    )

# Create and run the bot application without asyncio.run()
def run_bot():
    app: Application = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

# Directly call the run_bot function
if __name__ == "__main__":
    run_bot()
