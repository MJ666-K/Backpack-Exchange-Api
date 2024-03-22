from bpx.markets.api import MarketsApi

if __name__ == "__main__":
    markets = MarketsApi()
    markets.get_assets()
