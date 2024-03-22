#!/usr/bin/env python

import base64
import time
import datetime
from cryptography.hazmat.primitives.asymmetric import ed25519
from tools.log import getLogger
from configuration_env import get_api_key
from tools.utils import Singleton


@Singleton
class SigningRequests:

    log = getLogger("system-" + datetime.datetime.now().strftime("%Y-%m-%d"))

    def __init__(self, window: int = 5000) -> None:

        self.url = "https://api.backpack.exchange/"
        self.window = window
        self.timestamp = int(time.time() * 1000)
        api_key, api_secret = self._init()
        self.api_key, self.api_secret = api_key, api_secret

    def _init(self):
        KEY, SECRET = get_api_key()
        private_key_bytes = base64.b64decode(SECRET)
        api_secret = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)
        return (KEY, api_secret)

    def get_headers(self, instruction: str = "", parameters: dict = {}):
        if not instruction:
            signing_string = ""
        else:
            signing_string = "instruction=" + instruction
        sorted_params = "&".join(
            f"{key}={value}" for key, value in sorted(parameters.items())
        )
        if sorted_params:
            signing_string += "&" + sorted_params
        signing_string += f"&timestamp={self.timestamp}&window={self.window}"
        signature_bytes = self.api_secret.sign(signing_string.encode())
        encoded_signature = base64.b64encode(signature_bytes).decode()

        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": encoded_signature,
            "X-TIMESTAMP": str(self.timestamp),
            "X-WINDOW": str(self.window),
            "Content-Type": "application/json; charset=utf-8",
        }

        self.log.debug(f"签名认证 {encoded_signature}")
        return headers
