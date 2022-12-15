from flask import Flask as fl
from flask_restful import Api , Resource
import json
from convertor import Convertor


app = fl("CurrencyService")
api = Api(app)


class CurrencyService(Resource):
    url = ''
    api_key = ''

    def __get_configuration(self):
        with open("../config/config.json") as json_config:
            config = json.load(json_config)
            self.url = config["externalService"]["url"]
            self.api_key = config["externalService"]["apikey"]

    def get(self):
        self.__get_configuration()
        cc = Convertor(self.url, self.api_key)
        return cc.get_list()


api.add_resource(CurrencyService, '/list')

if __name__ == "__main__":
    app.run()
