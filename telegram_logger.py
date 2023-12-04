import requests


class TelegramLogger:
    def __init__(self):
        self.token = "YOUR_TELEGRAM_BOT_TOKEN"
        self.chat_id = "YOUR_CHAT_ID"
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def log(self, message):
        data = {"chat_id": self.chat_id, "text": message, "parse_mode": "HTML"}
        response = requests.post(self.api_url, data=data)
        return response.json()
