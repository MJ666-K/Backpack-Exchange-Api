# Backpack Exchange API(1.0.0)

## ⚡ 简介
# Backpack Exchange
You can clone the repository and use it directly:

```bash
git clone git@github.com:MJ666-K/Backpack-Exchange-Api.git
cd Backpack-Exchange-Api
pip3 install requirements.txt
```

## Usage
### config.ini
```python
[keys]
api_key=YOUR-API-KEY
api_secret=YOUR-SECRET
```
### main.py
```python
from bpx.markets.api import MarketsApi

markets = MarketsApi("SOL_USDC")

# Get all supported assets
assets = markets.get_assets()
print(assets)

# Get ticker
ticker = markets.get_ticker()
print(ticker)

```

## Documentation
For more detailed information about the API endpoints and their usage, refer to the [Backpack Exchange API documentation](https://docs.backpack.exchange/).

## Support 

If this interface has been helpful to you 🌟 and you haven't signed up for Backpack Exchange yet, please consider using the following referral link to register: [Register on Backpack Exchange](https://backpack.exchange/refer/solomeowl) 🚀.
