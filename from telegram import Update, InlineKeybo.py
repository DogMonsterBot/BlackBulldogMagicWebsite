from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    # Create an inline button
    keyboard = [[InlineKeyboardButton("Glass Button", callback_data='button_pressed')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the button
    update.message.reply_text('Hello! Click the button below:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="You clicked the glass button!")

def main() -> None:
    # Add your bot token here
    updater = Updater("7642252782:AAGUVwNlrJIUK1-aoz0Sq3ElACpyTjGzSPE")

    # Get the dispatcher
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
