import mysql.connector as mysql
import json
from json import JSONDecoder, JSONEncoder, JSONDecodeError
import logging

logger_c = logging.getLogger('schemaOps')
logger_c.setLevel(logging.DEBUG)
log_format = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(log_format)
logger_c.addHandler(consoleHandler)


class config_decoder(object):

    def __init__(self):
        self.props = None

    def load_config(self):
        try:
            with open('../main/config.json', 'r') as params:
                params_ = params.read()
                self.props = json.loads(params_)
        except (JSONDecoder, JSONEncoder, JSONDecodeError) as json_error:
            logging.error('Found error while loading config file.')
        except FileNotFoundError as fnfe:
            logging.error('Config file does not exists.')

    def load_database(self):
        try:
            if self.props is not None:
                return self.props["databases"]
        except JSONDecodeError as json_error:
            logging.error('Found error while json loading.')

    def __str__(self):
        return json.dumps(self.load_database(), indent=3)


if __name__ == '__main__':
    """
    dbOps = config_decoder()
    dbOps.load_config()
    print(dbOps.__str__())
    """
    pass

with open('../main/config.json', 'r') as config_params:
    config_ = config_params.read()
    load_config = json.loads(config_)

database_length = len(load_config["databases"])
database = load_config["databases"]


def load_database(instance):
    for _id in range(0, database_length):
        for _db in database[_id]:
            if database[_id].get(instance):
                print(database[_id].get(instance))


load_database('node_1')
