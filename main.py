from trading_bot import TradingBot


# Список токенов
tokens = ["BTC", "ETH", "XRP"]  # Пример списка токенов


# Создаем и запускаем бота
bot = TradingBot(tokens)
bot.run()
