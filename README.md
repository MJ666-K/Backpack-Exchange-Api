# Backpack Exchange API(1.0)

## ⚡ 简介
# Backpack Exchange
you can clone the repository and install the SDK manually:

```bash
git clone git@github.com:MJ666-K/Backpack-Exchange-Api.git
cd BackpackExchange
pip3 install requirements.text
```

## Usage
### config
```python
[keys]
api_key=YOU-API-KEY
api_secret=YOU-API-SECRET
```
### main.py
```python
from bpx.markets.api import MarketsApi

markets = MarketsApi("SOL_USDC")

# Get all supported assets
assets = markets.get_assets()
print(assets)

# Get ticker
ticker = public_client.get_ticker()
print(ticker)

```

## Documentation
For more detailed information about the API endpoints and their usage, refer to the [Backpack Exchange API documentation](https://docs.backpack.exchange/).

## Support 

If this SDK has been helpful to you 🌟 and you haven't signed up for Backpack Exchange yet, please consider using the following referral link to register: [Register on Backpack Exchange](https://backpack.exchange/refer/solomeowl) 🚀.