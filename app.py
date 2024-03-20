import logging
from common import start_logger
from adapters.inbound import run_app_service

start_logger()
logger = logging.getLogger()





def set_up():
    logging.info('START SYSTEM')
    run_app_service()
    logging.info('App service started')



if __name__ == "__main__":
    set_up()
    while True:
        pass