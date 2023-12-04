from threading import Thread
from bybit_api import BybitAPI
from db_manager import DBManager
from telegram_logger import TelegramLogger


class TradingBot:
    def __init__(self, tokens):
        self.tokens = tokens
        self.api = BybitAPI()
        self.db = DBManager()
        self.logger = TelegramLogger()

    def run(self):
        for token in self.tokens:
            thread = Thread(target=self._run_bot, args=(token,))
            thread.start()

    def _run_bot(self, token):
        try:
            # Проверка наличия активного ордера
            if self.api.check_active_order(token):
                self.logger.log(f"Активный ордер уже существует для {token}")
                return

            # Вход в лонг позицию
            position_id = self.api.enter_long_position(token)

            while True:
                pnl = self.api.get_pnl(position_id)
                current_price = self.api.get_current_price(token)

                # Логика управления ордерами
                if pnl <= -0.05:
                    self.api.set_limit_order(token, current_price)
                elif pnl <= -0.08:
                    self.api.set_market_order(token, current_price)
                elif pnl >= 0.05:
                    self.api.move_stop_loss(token, current_price, 0.01)
                elif pnl >= 0.10:
                    self.api.move_stop_loss(token, current_price, 0.05)

                # Проверка условия выхода
                if pnl <= -0.05:
                    break

                time.sleep(10)  # Пауза перед следующей проверкой

        except Exception as e:
            self.logger.log(f"Ошибка для {token}: {e}")
