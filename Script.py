from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import JoinChannelRequest

# Your API ID and hash from my.telegram.org
api_id = '28578880'
api_hash = 'Hash 5f8c87efde57e01d12c0ce98ffdf5928'
bot_token ='6911187935:AAE4g4u0AIELAWQidSiN88J4-3XItyzzX5M'
# Initialize the bot client
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Variables to store channel IDs
source_channel = None
target_channel = None

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("Hello! Use /setsource and /settarget to set the source and target channels.")

@bot.on(events.NewMessage(pattern='/setsource'))
async def set_source(event):
    global source_channel
    source_channel = event.message.message.split(' ')[1]  # Extract the channel ID or username from the command
    await event.reply(f"Source channel set to: {source_channel}")

@bot.on(events.NewMessage(pattern='/settarget'))
async def set_target(event):
    global target_channel
    target_channel = event.message.message.split(' ')[1]  # Extract the channel ID or username from the command
    await event.reply(f"Target channel set to: {target_channel}")

@bot.on(events.NewMessage(chats=lambda e: e.is_channel, incoming=True))
async def clone_message(event):
    global source_channel, target_channel
    if event.chat_id == int(source_channel):  # Ensure that the message is from the source channel
        if target_channel:
            await event.message.forward_to(target_channel)
        else:
            await event.reply("Target channel not set. Please use /settarget to set the target channel.")

print("Bot is running...")
bot.run_until_disconnected()
