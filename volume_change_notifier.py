import telebot
from binance.client import Client
from datetime import datetime
import time
import json


# Load configuration from file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

API_KEY = config['BINANCE_API_KEY']
API_SECRET = config['BINANCE_API_SECRET']
TELEGRAM_TOKEN = config['TELEGRAM_TOKEN']
CHAT_ID = config['CHAT_ID']
SYMBOLS = config['SYMBOLS']
INTERVAL = config['INTERVAL']


# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Function to get historical data and calculate volume change


def get_volume_change(symbol, interval):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=2)
    if len(klines) == 2:
        prev_volume = float(klines[0][5])
        curr_volume = float(klines[1][5])
        volume_change = ((curr_volume - prev_volume) / prev_volume) * 100

        prev_timestamp = datetime.fromtimestamp(klines[0][0] / 1000)
        curr_timestamp = datetime.fromtimestamp(klines[1][0] / 1000)

        return {
            'previous_volume': prev_volume,
            'previous_timestamp': prev_timestamp,
            'current_volume': curr_volume,
            'current_timestamp': curr_timestamp,
            'volume_change': volume_change
        }
    else:
        return None

# Function to send Telegram message


def send_telegram_message(message):
    bot.send_message(CHAT_ID, message)



# Continuously check for volume changes every 10 seconds
while True:
    for symbol in SYMBOLS:
        volume_data = get_volume_change(symbol, INTERVAL)
        if volume_data:
            prev_volume = volume_data['previous_volume']
            curr_volume = volume_data['current_volume']
            volume_change = volume_data['volume_change']

            print(f"Symbol: {symbol}")
            print(f"Interval: {INTERVAL}")
            print(
                f"Previous Volume: {prev_volume:.2f} at {volume_data['previous_timestamp']}")
            print(
                f"Current Volume: {curr_volume:.2f} at {volume_data['current_timestamp']}")
            print(f"Volume change: {volume_change:.2f}%\n")

            if volume_change > 5:
                message = (f"Volume change alert for {symbol}!\n"
                           f"Interval: {INTERVAL}\n"
                           f"Previous Volume: {prev_volume:.2f} at {volume_data['previous_timestamp']}\n"
                           f"Current Volume: {curr_volume:.2f} at {volume_data['current_timestamp']}\n"
                           f"Volume change: {volume_change:.2f}%")
                send_telegram_message(message)
        else:
            print(
                f"Not enough data to calculate volume change for {symbol} at {INTERVAL}\n")

    time.sleep(10)
