from telethon import events, TelegramClient

async def handle_another_specific_message(event):
    message = event.message
    text = message.text

    if message.from_id and (message.from_id.user_id == message.from_id.user_id == 6205161271) and text == 'منصب؟':
        await message.reply('✔يب منصب')