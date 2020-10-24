from telethon.sync import TelegramClient
from telethon.sync import events

bot_name = 'telegram-id-obtainer'
API_ID = 1759413
API_HASH = '609e3756b5a95466c9422ab57eea37bb'
BOT_TOKEN = '1389169665:AAG81cZsPRswI4-hS0z0Yv2l9H3xofl8A24'

bot = TelegramClient(bot_name, API_ID, API_HASH)

bot.start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage)
async def bot_new_message_handler(event):
  userId = event.from_id
  
  await event.respond(f'your id is: {userId}')

bot.run_until_disconnected()