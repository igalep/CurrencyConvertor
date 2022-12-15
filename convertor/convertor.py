import requests as req
import json
import pprint

class Convertor:
    rates = {}
    def __init__(self, url , api_key):
        self.url = url
        self.api_key = api_key

    def get_list(self):
        ROUTE = '/list'
        headers = {"apikey" : self.api_key}
        response = req.get('http://' + self.url + ROUTE, headers=headers)
        return response.json()




if __name__ == "__main__":
    with open("../config/config.json") as json_config:
        config = json.load(json_config)
        url = config["externalService"]["url"]
        api_key = config["externalService"]["apikey"]

        cc = Convertor(url, api_key)
        data = cc.get_list()

        pprint.pprint(data)