import logging
import kink

from application.app_facade import AppFacade
from application.bootstrap import bootstrap_di
from common import start_logger
from adapters.inbound import run_app_service
import threading


start_logger()
logger = logging.getLogger()





def set_up():
    logging.info('START SYSTEM')
    run_app_service()
    logging.info('App service started')
    bootstrap_di()



if __name__ == "__main__":
    set_up()
    indoor_thread = threading.Thread(target=kink.di[AppFacade].indoor_main_loop, daemon=False, name="Indoor thred")
    # outdoor_thread = threading.Thread(target=facade.outdoor_main_loop, daemon=False,name="outdoor thred")
    indoor_thread.start()
    # outdoor_thread.start()


    