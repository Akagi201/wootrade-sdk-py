from wootrade_sdk.client import Client

API = ""
SECRET = ""
APPLICATION_ID = ""

client = Client(API, SECRET, APPLICATION_ID, testnet=True)
info = client.get_exchange_info(symbol="SPOT_BTC_USDT")
print(info)
