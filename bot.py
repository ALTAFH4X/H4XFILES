from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

api_id = 35141764
api_hash = "13ef78302113fe46ba310ff965c0d534"
bot_token = "8985632939:AAEEhuhklALHMIwXaoI3leQF_EHYG9ZFSkYs"

# फाइल की file_id
FILE_ID = "BQACAgUAAxkBAAEVksRqVJkNV1cE2RT2d0RUBLEyD7AC0AIIaKICSFaEtjJxVzXtDdOE"

# यहाँ अपने तीनों चैनल्स के Username या ID डालें
channels = ["-1004347890359", "-1003945512549", "-1003815841522"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def check_subscription(client: Client, user_id: int):
    for channel in channels:
        try:
            member = client.get_chat_member(channel, user_id)
            if member.status not in ["creator", "administrator", "member"]:
                return False
        except Exception as e:
            print(f"Error checking {channel}: {e}")
            return False
    return True

@app.on_message(filters.command("start"))
def start(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel 1", url="https://t.me/+MFkJ8G0FYQNiMGM1")],
        [InlineKeyboardButton("Channel 2", url="https://t.me/+hhJlfs2ljdFhMWFl")],
        [InlineKeyboardButton("Channel 3", url="https://t.me/sanjeevhahah")],
        [InlineKeyboardButton("Verify", callback_data="verify")]
    ])
    message.reply_text("PLZ JOIN THE ALL CHANNEL TO ACCES THE FILES", reply_markup=keyboard)

@app.on_callback_query(filters.regex("verify"))
def verify(client: Client, query: CallbackQuery):
    user_id = query.from_user.id
    if check_subscription(client, user_id):
        query.answer("JOIN SUCCESSFULLY", show_alert=True)
        query.message.edit_text("YOUR WELCOME NOW YOU CAN DOWNLOAD THE FILES")
        
        # फाइल भेजने का कोड
        client.send_document(
            chat_id=query.message.chat.id,
            document=FILE_ID,
            caption="यहाँ आपकी फाइल है!"
        )
    else:
        query.answer("PLEASE JOIN ALL CHANNEL", show_alert=True)

app.run()
