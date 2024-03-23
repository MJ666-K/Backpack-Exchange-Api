from bpx.api.api import Api
import datetime
from tools.log import getLogger

log = getLogger("system-" + datetime.datetime.now().strftime("%Y-%m-%d"))


class MarketsApi:
    def __init__(self, symbol: str = None) -> None:
        self.bp = Api()
        self.symbol = symbol
        self.url = f"{self.bp.url}api/v1/"

    def get_assets(self):
        """
        Retrieves all the assets that are supported by the exchange.
        """
        response = self.bp.get(self.url + "assets")
        if response:
            msg, code = response
            log.info(f"GetAssets: {code} {msg}")
            return msg
        else:
            log.info(f"GetAssets Error...")

    def get_markets(self):
        """
        Retrieves all the markets that are supported by the exchange.
        """
        response = self.bp.get(self.url + "markets")
        if response:
            msg, code = response
            log.info(f"GetMarkets: {code} {msg}")
            return msg
        else:
            log.info(f"GetMarkets Error...")

    def get_ticker(self):
        """
        Retrieves summarised statistics for the last 24 hours for the given market symbol.
        """
        response = self.bp.get(self.url + "ticker", parameters={"symbol": self.symbol})
        if response:
            msg, code = response
            log.info(f"GetTicker: {code} {msg}")
            return msg
        else:
            log.info(f"GetTicker Error...")

    def get_tickers(self):
        """
        Retrieves summarised statistics for the last 24 hours for all market symbols.
        """
        response = self.bp.get(self.url + "tickers")
        if response:
            msg, code = response
            log.info(f"GetTickers: {code} {msg}")
            return msg
        else:
            log.info(f"GetTickers Error...")

    def get_depth(self):
        """
        Retrieves the order book depth for a given market symbol.
        """
        response = self.bp.get(self.url + "depth", parameters={"symbol": self.symbol})
        if response:
            msg, code = response
            log.info(f"GetDepth: {code} {msg}")
            return msg
        else:
            log.info(f"GetDepth Error...")

    def get_klines(self, interval: str, startTime: int = None, endTime: int = None):
        """
        Get K-Lines for the given market symbol, optionally providing a startTime and endTime.
        If no startTime is provided, the interval duration will be used.
        If no endTime is provided, the current time will be used.
        """
        parameters = {"symbol": self.symbol, "interval": interval}
        if not startTime:
            parameters["startTime"] = startTime
        if not endTime:
            parameters["endTime"] = startTime
        response = self.bp.get(self.url + "klines", parameters=parameters)
        if response:
            msg, code = response
            log.info(f"GetKlines: {code} {msg}")
            return msg
        else:
            log.info(f"GetKlines Error...")
