# This is an example Python script for interfacing with the Zabbix api with basic logging included.
# This is useful as a starting point for new scripts.
#
# Nick Miethe 2018

from pyzabbix import ZabbixAPI
from pyzabbix import ZabbixAPIException
import logging

log_file = 'log_name.log'
logger = logging.getLogger('Example Log Title')
logger.setLevel(logging.INFO)
logging_handler = logging.FileHandler(log_file)
logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logging_handler.setFormatter(logger_formatter)
logger.addHandler(logging_handler)

authUser = ''
authPassword = ''
zabbixUrl = ''

def example_main_function():
    function = 'usergroup.get'
    json = {'output':'extend'}
    print (api_request(function, json))

def api_request(function, json):

    # jsonrpc and ID are auto appended by ZabbixAPI
    try:
        zapi = ZabbixAPI(url=zabbixUrl, \
            user=authUser, password=authPassword)
    except ZabbixAPIException:
        logger.warning('URL or Login is incorrect')
        raise

    try:
        response = zapi.do_request(function, json)['result']
        return response
    except ZabbixAPIException:
        logger.error("Trouble executing following function: " + function)
        raise

if __name__ == '__main__':
    example_main_function()
    exit
