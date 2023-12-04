# EXAMPLE of Bybit Trading Bot

## Overview

This project is an example implementation of a trading bot for the Bybit exchange. The bot is designed to automate trading strategies on the Bybit futures market. It includes functionalities such as managing stop-losses and targets dynamically during trades.

## Features

- **Automated Trading**: The bot trades a specified list of tokens on the Bybit futures market.
- **Dynamic Stop-Loss and Target Management**: Adjusts stop-losses and targets based on predefined conditions.
- **Concurrency**: Handles multiple tokens simultaneously using threading.
- **Database Integration**: Uses PostgreSQL for trade history storage.
- **Logging**: All logs are sent to a specified Telegram channel.

## Components

- `main.py`: Entry point for initiating the bot.
- `trading_bot.py`: Core logic for managing trades.
- `bybit_api.py`: Handles interaction with the Bybit API.
- `db_manager.py`: Manages database operations for storing trade data.
- `telegram_logger.py`: Sends log messages to a Telegram channel.