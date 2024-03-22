from bpx.api.api import Api
import datetime
from tools.log import getLogger

log = getLogger("system-" + datetime.datetime.now().strftime("%Y-%m-%d"))


class MarketsApi:
    def __init__(self, symbol: str = None) -> None:
        self.bp = Api()
        self.symbol = symbol

    def get_assets(self):
        url = f"{self.bp.url}api/v1/assets"
        response = self.bp.get(url)
        if response:
            msg, code = response
            log.info(f"GetAssets: {code} {msg}")
            return msg
        else:
            log.info(f"GetAssets Error...")

    def get_markets(self):
        # https://api.backpack.exchange/api/v1/markets
        pass
