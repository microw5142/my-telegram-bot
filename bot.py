import os
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# อ่านโทเคนจากไฟล์ .env
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

def main():
    # ตรวจสอบว่าโทเคนถูกตั้งไว้หรือไม่
    if not TELEGRAM_TOKEN:
        print("Error: TELEGRAM_TOKEN not found in environment variables.")
        return

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # เพิ่ม handler สำหรับคำสั่ง /start
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
