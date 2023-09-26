import os

from wootrade_sdk.streams import ThreadedWebsocketManager

API = os.getenv("API")
SECRET = os.getenv("SECRET")
APPLICATION_ID = os.getenv("APPLICATION_ID")


def test_create_TWM():
    ThreadedWebsocketManager(API, SECRET, APPLICATION_ID, False)
    ThreadedWebsocketManager(API, SECRET, APPLICATION_ID, False)
