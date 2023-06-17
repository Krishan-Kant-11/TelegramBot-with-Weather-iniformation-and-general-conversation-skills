# TelegramBot-with-Weather-information-and-General-Conversation-Skills

This is a Telegram bot project named "TelegramBot-with-Weather-information-and-General-Conversation-Skills". The bot is designed to provide weather information and engage in general conversation with users.

## Features

1. **Weather Information**: The bot can provide weather information for a specific city. It uses the OpenWeatherMap API to fetch real-time weather data.

2. **General Conversation**: The bot is capable of engaging in general conversation with users. It can respond to various greetings, inquiries about its identity, and questions about personal information.

3. **Date and Time**: The bot can provide the current date and time. It uses the `datetime` and `pytz` libraries to fetch the date and time information and adjust it to the local timezone.

4. **Social Media Links**: The bot can provide links to popular social media platforms such as YouTube, Instagram, LinkedIn, Facebook, Twitter, WhatsApp, and Gmail.

## Requirements

To run the Telegram bot, you need the following dependencies:

- `os` library
- `telebot` library
- `datetime` library
- `pytz` library
- `requests` library

You can install these dependencies using the following command:
```bash
pip install telebot pytz requests
```


## Getting Started

To use the Telegram bot, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Krishan-Kant-11/TelegramBot-with-Weather-information-and-General-Conversation-Skills.git
```

2. Set up the necessary API keys:

- Obtain a Telegram Bot API key from the [BotFather](https://core.telegram.org/bots#6-botfather).
- Sign up for an account on [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.

3. Replace the placeholders in the code with your API keys:

- Replace `os.environ['key']` with your Telegram Bot API key.
- Replace `os.environ['weatherapi']` with your OpenWeatherMap API key.

4. Run the bot:
```bash
python main.py
```

5. Start a conversation with the bot on Telegram by searching for its name or username.

## Usage

Once the bot is running and you have started a conversation with it on Telegram, you can use the following commands and message formats:

- `/start`: This command initiates the conversation with the bot. It will introduce itself and provide a brief description of its capabilities.

- General Conversation: The bot can respond to various greetings, such as "hello," "hi," "greet," "morning," "afternoon," "evening," "night," "namaste," "namaskara," or "namaskar." It will reply with an appropriate greeting.

- Date and Time: You can ask the bot for the current date and time by including keywords like "time" or "date" in your message. The bot will respond with the current date and time in the local timezone.

- Social Media Links: You can ask the bot for links to popular social media platforms by including keywords like "youtube," "instagram," "linkedin," "facebook," "twitter," "whatsapp," or "gmail" in your message. The bot will reply with the corresponding URL.

- Weather Information: To obtain weather information for a specific city, include the keyword "weather" followed by the city name in your message. The bot will fetch the current temperature and weather description using the OpenWeatherMap API and provide the information in Celsius.

## Limitations

- The bot's weather functionality relies on accurate city names. If an incorrect city name is provided, the bot will not be able to retrieve weather information.

- The bot's conversation skills are limited to pre-defined responses. It may not understand complex or context-specific queries.

- The bot's social media links are provided as general URLs and do not take into account specific user profiles.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.






