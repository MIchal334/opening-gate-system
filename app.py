import logging
from application.app_facade import get_facade
from common import start_logger
from adapters.inbound import run_app_service, run_car_handler
import threading

start_logger()
logger = logging.getLogger()





def set_up():
    logging.info('START SYSTEM')
    run_app_service()
    logging.info('App service started')
    run_car_handler()
    logging.info('Run car handler')



if __name__ == "__main__":
    set_up()
    indoor_thread = threading.Thread(target=get_facade().indoor_main_loop, daemon=True)
    outdoor_thread = threading.Thread(target=get_facade().outdoor_main_loop, daemon=False)
    indoor_thread.start()
    outdoor_thread.start()


    