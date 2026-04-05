import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

    def _sign(self, params):
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, **params):
        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        url = BASE_URL + "/fapi/v1/order"

        response = requests.post(url, headers=headers, params=params)

        return response.json()