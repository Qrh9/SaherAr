from telegram.ext import Updater, CommandHandler
from telethon.sync import TelegramClient
from telethon.sessions import StringSession


# Handler for the /start command
def start(update, context):
    update.message.reply_text("Welcome to the Telethon STRING_SESSION bot!\n\nPlease enter your API ID and API hash in the format: API_ID API_HASH")

# Handler for receiving the API ID and API hash
def receive_api_info(update, context):
    api_info = update.message.text.split()
    if len(api_info) == 2:
        api_id, api_hash = api_info
        client = TelegramClient(StringSession(), api_id, api_hash)
        with client:
            session_string = client.session.save()
        update.message.reply_text(f"Your Telethon STRING_SESSION:\n\n{session_string}")
    else:
        update.message.reply_text("Invalid input. Please enter your API ID and API hash in the correct format: API_ID API_HASH")

def main():
    updater = Updater('your_bot_token', use_context=True)
    dispatcher = updater.dispatcher

    # Register the command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register the message handler
    receive_api_info_handler = MessageHandler(Filters.text, receive_api_info)
    dispatcher.add_handler(receive_api_info_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
