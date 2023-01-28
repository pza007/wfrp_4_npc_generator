import coloredlogs
import logging


logging.basicConfig(filename="log_file.log",
                    format='[%(levelname)s][%(funcName)s, line:%(lineno)s] %(message)s')
                    # filemode='w')

logger = logging.getLogger(__name__)

levelstyles = {'critical': {'bold': True, 'color': 'red'},
               'debug': {'color': 'white'},
               'error': {'color': 'red'},
               'info': {'color': 'magenta'},
               'warning': {'color': 'yellow'}}

coloredlogs.install(level=logging.DEBUG,
                    logger=logger,
                    fmt='%(message)s',
                    datefmt='%H:%M:%S',
                    level_styles=levelstyles)