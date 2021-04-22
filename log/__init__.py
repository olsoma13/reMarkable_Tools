import json
import sys
import logging
import os

# load config file
try:
    config = json.load(open('config.json'))
except IOError:
    print('failed to open the file')
    sys.exit()
except TypeError:
    print('failed to parse json')
    sys.exit()


# Setup logging level & location
def setup_logger(name):
    logger = logging.getLogger(name)
    logLevel = config['logging']['level']
    logLocation = config['logging']['location']
    loggingFormat = '%(asctime)s - %(name)s (%(levelname)s) - %(message)s'
    if logLocation == "FILE":
        try:
            logging.basicConfig(
                format=loggingFormat, filename='LoggingOutput/global.log',
                level=logLevel)
        except OSError:
            try:
                os.mkdir("LoggingOutput")
                logger.info("Creating directory `../LoggingOutput` since it doesn't yet exist.")
            except FileExistsError:
                # directory already exists
                logger.warning("Some other OS error occurred. Investigate issue!")
                pass
    elif logLocation == "CONSOLE":
        logging.basicConfig(
            format=loggingFormat, level=logLevel)
    else:
        logging.basicConfig(
            format=loggingFormat, level=logLevel)
        logger.warning('File config.json does not have `location` defined!')
    logger.debug('Pulled logging level of `' +
                 logLevel + '` and a logging location of `' +
                 logLocation + '` from config.json.')
    return logger
