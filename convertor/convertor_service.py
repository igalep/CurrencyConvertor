import json

from flask import Flask as fl
from flask_restful import Api, Resource

from convertor import Convertor

app = fl("CurrencyService")
api = Api(app)


def get_configuration():
    with open("config/config.json") as json_config:
        config = json.load(json_config)
        global url, api_key
        url = config["externalService"]["url"]
        api_key = config["externalService"]["apikey"]


get_configuration()
connection_tuple = (url, api_key)


class CurrencyServiceList(Resource):
    ROUTE = '/list'

    def __init__(self):
        self.cc_list = Convertor(connection_tuple[0], connection_tuple[1], CurrencyServiceList.ROUTE)

    def get(self):
        return self.cc_list.get_list()


class CurrencyServiceLive(Resource):
    ROUTE = '/live'

    def __init__(self):
        self.source = "USD"
        self.currencies = "ILS%2CEUR"
        self.cc_live = Convertor(connection_tuple[0], connection_tuple[1], CurrencyServiceLive.ROUTE)

    def get(self):
        return self.cc_live.get_live(self.source, self.currencies)


api.add_resource(CurrencyServiceList, CurrencyServiceList.ROUTE)
api.add_resource(CurrencyServiceLive, CurrencyServiceLive.ROUTE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)