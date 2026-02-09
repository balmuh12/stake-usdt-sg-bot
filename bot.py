from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Staking Information", callback_data="info")],
        [InlineKeyboardButton("💼 Investment Plans", callback_data="plans")],
        [InlineKeyboardButton("📥 How to Join", callback_data="join")],
        [InlineKeyboardButton("💬 Customer Support", url="https://t.me/ADMIN_USERNAME")],
        [InlineKeyboardButton("👥 Official Group", url="https://t.me/GROUP_USERNAME")]
    ]

    await update.message.reply_text(
        "🤖 Welcome to Stake USDT SG 🇸🇬\n\n"
        "Smart investment with smart strategy\n"
        "Secure • Transparent • Professional\n\n"
        "Please choose a menu below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        text = "📊 Stake USDT SG provides stable and secure USDT staking."
    elif query.data == "plans":
        text = "💼 Investment Plans:\n• Basic\n• Premium\n• VIP"
    elif query.data == "join":
        text = (
            "📥 How to Join:\n"
            "1. Contact Customer Support\n"
            "2. Choose an investment plan\n"
            "3. Transfer USDT\n"
            "4. Account will be created automatically"
        )

    await query.edit_message_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(menu))
app.run_polling()
