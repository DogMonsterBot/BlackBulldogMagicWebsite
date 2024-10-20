from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler
import asyncio

async def start(update: Update, context: CallbackContext) -> None:
    # ایجاد دکمه شیشه‌ای
    keyboard = [[InlineKeyboardButton("دکمه شیشه‌ای", callback_data='button_pressed')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ارسال پیام با دکمه
    await update.message.reply_text('سلام! روی دکمه زیر کلیک کنید:', reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="شما روی دکمه شیشه‌ای کلیک کردید!")

async def main() -> None:
    # توکن ربات خود را اینجا وارد کنید
    application = ApplicationBuilder().token("7642252782:AAGUVwNlrJIUK1-aoz0Sq3ElACpyTjGzSPE").build()

    # اضافه کردن دستورات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # شروع ربات
    await application.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
