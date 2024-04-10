import logging
from application.app_facade import get_facade
from common import start_logger
from adapters.inbound import run_app_service
import threading
import time

start_logger()
logger = logging.getLogger()





def set_up():
    logging.info('START SYSTEM')
    run_app_service()
    logging.info('App service started')



if __name__ == "__main__":
    set_up()
    facade = get_facade()
    indoor_thread = threading.Thread(target=facade.indoor_main_loop, daemon=False, name="Indoor thred")
    # outdoor_thread = threading.Thread(target=facade.outdoor_main_loop, daemon=False,name="outdoor thred")
    indoor_thread.start()
    # outdoor_thread.start()


    