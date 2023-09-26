from woo_sdk.streams import ThreadedWebsocketManager


def on_read(payload):
    print(payload)


API = ""
SECRET = ""
APPLICATION_ID = ""

wsm = ThreadedWebsocketManager(API, SECRET, APPLICATION_ID, testnet=True)
wsm.start()

# Un-auth subscribe
name = "market_connection"
wsm.start_socket(on_read, socket_name=name, auth=False)
wsm.subscribe(name, topic="SPOT_BTC_USDT@kline_1m", id="ClientID", event="subscribe")

# Auth subscribe
name = "private_connection"
wsm.start_socket(on_read, socket_name=name, auth=True)
wsm.authentication(socket_name=name)
wsm.subscribe(
    name,
    topic="executionreport",
    id="ClientID",
    event="subscribe",
)
