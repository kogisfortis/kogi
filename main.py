from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusOnline
import requests
import os
import time

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
target_username = os.getenv('TARGET_USERNAME')
bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

def notify_bot(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': message})

def main():
    client = TelegramClient('monitor_session', api_id, api_hash)
    client.start(phone=phone)
    was_online = False

    with client:
        while True:
            try:
                user = client.get_entity(target_username)
                is_online = isinstance(user.status, UserStatusOnline)
                if is_online and not was_online:
                    notify_bot(f'👤 {target_username} сейчас онлайн!')
                was_online = is_online
            except Exception as e:
                print('Error:', e)
            time.sleep(30)

if __name__ == '__main__':
    main()
