# Crypto Volume Monitor

Ever feel like you're missing out on those big crypto moves because you're too busy actually living your life? 🌍🏃‍♂️ Fear not! This project monitors the volume changes of your favorite cryptocurrencies on the Binance exchange and alerts you via Telegram. 🚀📲 It's like having a financial watchdog that doesn't need walking or feeding—just a steady diet of API keys. 🐕💻



## Setup

### Prerequisites

- Python 3.6 or later
- pip (Python package installer)
- python-binance
- pyTelegramBotAPI

To install the required dependencies, run:

```
pip install python-binance pyTelegramBotAPI
```

### Configuration

1. Create a new file named `config.json` in the project root directory.
2. Open the `config.json` file and add the following content:

```json
{
  "BINANCE_API_KEY": "your_binance_api_key",
  "BINANCE_API_SECRET": "your_binance_api_secret",
  "TELEGRAM_TOKEN": "your_telegram_bot_token",
  "CHAT_ID": "your_telegram_chat_id",
  "SYMBOLS": ["BTCUSDT", "ETHUSDT", "XRPUSDT"],
  "INTERVAL": "1d"
}
```

3. Replace the placeholders with your actual values:
   - `BINANCE_API_KEY` and `BINANCE_API_SECRET`: Obtain these from your Binance account by creating a new API key.
   - `TELEGRAM_TOKEN`: Create a new Telegram bot by talking to the BotFather and obtain the bot token.
   - `CHAT_ID`: Send a message to your bot in Telegram and use the `@get_id_bot` to obtain your chat ID.
   - `SYMBOLS`: List the cryptocurrency symbols you want to monitor (e.g., `BTCUSDT`, `ETHUSDT`, `XRPUSDT`).
   - `INTERVAL`: Specify the time interval for monitoring volume changes (e.g., `1d` for daily).

### Running the Application

To run the application, execute the following command:

```
python main.py
```

The application will start monitoring the specified cryptocurrencies and send alerts to the configured Telegram bot when there are significant volume changes.

## Contributing

Contributions are welcome! Please follow the contributing guidelines and submit a pull request.

## Testing

To test the `get_volume_change` function, run the following test:

```python
def test_get_volume_change(symbol, interval, expected_output):
    actual_output = get_volume_change(symbol, interval)
    assert actual_output == expected_output
```

This test function takes three arguments:

- `symbol`: The cryptocurrency symbol (e.g., `BTCUSDT`).
- `interval`: The time interval for monitoring (e.g., `1d`).
- `expected_output`: The expected volume change percentage.

You can add multiple test cases by calling `test_get_volume_change` with different inputs and expected outputs.

## Deployment

To create a standalone executable for the application, you can use PyInstaller:

```
pyinstaller --onefile main.py
```

This will create a single executable file `main` (or `main.exe` on Windows) in the `dist` directory.

## Troubleshooting

- **Missing or invalid `config.json` file**: Ensure that the `config.json` file exists in the project root directory and contains valid values for the required keys.
- **Binance API errors**: Check your Binance API key and secret, and make sure you have enabled the required permissions for your API key.
- **Telegram bot errors**: Verify your Telegram bot token and chat ID are correct.

## License

This project is licensed under the [MIT License](LICENSE).
