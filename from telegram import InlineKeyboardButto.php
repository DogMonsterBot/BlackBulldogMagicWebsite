from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

# Callback function when /start command is triggered
def start(update, context):
    # Create an inline keyboard with a button
    keyboard = [[InlineKeyboardButton("Click Here", callback_data='button_click')]]
    
    # Attach the inline keyboard to a markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the inline keyboard
    update.message.reply_text('Press the button:', reply_markup=reply_markup)

# Function to handle button clicks
def button_click(update, context):
    query = update.callback_query
    query.answer()

    # Redirect user to a hidden link without showing the URL
    query.edit_message_text(text="You've been redirected to the hidden link!")

    # Send the hidden link after clicking the button
    context.bot.send_message(chat_id=query.message.chat_id, text="Here is the hidden link: https://yourhiddenlink.com")

# Main function to start the bot
def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Add command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Add callback query handler for button clicks
    dp.add_handler(CallbackQueryHandler(button_click))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
