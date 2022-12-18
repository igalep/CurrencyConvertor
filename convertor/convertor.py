import requests as req
import json
import pprint


class Convertor:
    rates = {}

    def __init__(self, url, api_key, route):
        self.url = url
        self.api_key = api_key
        self.route = route

    def get_list(self):
        headers = {"apikey": self.api_key}
        response = req.get('http://' + self.url + self.route, headers=headers)
        return response.json()

    def get_live(self, source, currencies):
        headers = {"apikey": self.api_key}
        params = {"source": source, "currencies": currencies}
        response = req.get('http://' + self.url + self.route, headers=headers, params=params)
        return response.json()


if __name__ == "__main__":
    with open("../config/config.json") as json_config:
        config = json.load(json_config)
        url = config["externalService"]["url"]
        api_key = config["externalService"]["apikey"]

        cc = Convertor(url, api_key)
        data = cc.get_list()

        pprint.pprint(data)