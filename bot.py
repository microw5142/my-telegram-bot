from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ใส่ Bot Token ที่ได้จาก BotFather
TOKEN = "7973437134:AAETmnbCkm5DUYuHFQOcBWTdlNi6FM3PY08"

# ฟังก์ชันที่ใช้ตอบกลับข้อความ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("สวัสดี! ผมคือบอทของคุณ.")

# สร้าง Application และเพิ่ม Handler
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler('start', start))

# เริ่มการรับข้อมูล
application.run_polling()
