import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

# ===== 从 Railway 环境变量读取 =====
TOKEN = os.getenv("BOT_TOKEN")

TARGET_LINK = "https://t.me/HYJT12345"

WELCOME_TEXT = f"""
👋 欢迎加入本群！

📢 官方频道入口：
{TARGET_LINK}

📚 回复“资料”获取免费内容
💰 回复“赚钱”获取项目入口
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👋 欢迎！点击进入频道：\n{TARGET_LINK}")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(WELCOME_TEXT)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "资料" in text:
        await update.message.reply_text(f"📚 免费资料入口：{TARGET_LINK}")

    elif "赚钱" in text:
        await update.message.reply_text(f"💰 项目入口：{TARGET_LINK}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("🤖 引流机器人已启动")
    app.run_polling()

if __name__ == "__main__":
    main()