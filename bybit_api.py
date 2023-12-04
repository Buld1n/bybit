import requests
import hashlib
import time


class BybitAPI:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://api.bybit.com"
        self.api_key = api_key
        self.api_secret = api_secret

    def _generate_signature(self, params):
        sorted_params = sorted(params.items())
        encoded_params = "&".join([f"{key}={value}" for key, value in sorted_params])
        full_params = (
            f"{encoded_params}&api_key={self.api_key}&secret_key={self.api_secret}"
        )
        return hashlib.sha256(full_params.encode()).hexdigest()

    def check_active_order(self, token):
        endpoint = "/open-api/order/list"
        params = {"symbol": token, "timestamp": int(time.time() * 1000)}
        signature = self._generate_signature(params)
        response = requests.get(
            f"{self.base_url}{endpoint}", params={**params, "sign": signature}
        )
        return response.json()

    def enter_long_position(self, token):
        endpoint = "/open-api/order/create"
        params = {
            "side": "Buy",
            "symbol": token,
            "order_type": "Market",
            "qty": 1,
            "time_in_force": "GoodTillCancel",
            "timestamp": int(time.time() * 1000),
        }
        signature = self._generate_signature(params)
        response = requests.post(
            f"{self.base_url}{endpoint}", data={**params, "sign": signature}
        )
        return response.json()

    def get_current_price(self, token):
        endpoint = "/v2/public/tickers"
        params = {"symbol": token}
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        data = response.json()
        return data["result"][0]["last_price"]

    def set_limit_order(self, token, price, qty, side="Buy"):
        endpoint = "/open-api/order/create"
        params = {
            "side": side,
            "symbol": token,
            "order_type": "Limit",
            "price": price,
            "qty": qty,
            "time_in_force": "GoodTillCancel",
            "timestamp": int(time.time() * 1000),
        }
        signature = self._generate_signature(params)
        response = requests.post(
            f"{self.base_url}{endpoint}", data={**params, "sign": signature}
        )
        return response.json()

    def set_market_order(self, token, qty, side="Buy"):
        endpoint = "/open-api/order/create"
        params = {
            "side": side,
            "symbol": token,
            "order_type": "Market",
            "qty": qty,
            "time_in_force": "GoodTillCancel",
            "timestamp": int(time.time() * 1000),
        }
        signature = self._generate_signature(params)
        response = requests.post(
            f"{self.base_url}{endpoint}", data={**params, "sign": signature}
        )
        return response.json()

    def move_stop_loss(self, token, stop_price, qty):
        # Предполагаем, что для изменения стоп-лосса нужно создать новый ордер
        endpoint = "/open-api/stop-order/create"
        params = {
            "symbol": token,
            "stop_px": stop_price,  # Цена активации стоп-лосса
            "qty": qty,
            "order_type": "Market",  # В данном случае используем рыночный ордер для стоп-лосса
            "time_in_force": "GoodTillCancel",
            "timestamp": int(time.time() * 1000),
        }
        signature = self._generate_signature(params)
        response = requests.post(
            f"{self.base_url}{endpoint}", data={**params, "sign": signature}
        )
        return response.json()
