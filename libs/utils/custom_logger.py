import logging

class CustomLogger:

    @staticmethod
    def printStep(msg):
        logging.info('{0}'.format(msg))


    @staticmethod
    def printDebug(msg):
            logging.debug('{0}'.format(msg))

    @staticmethod
    def printError(msg):
        logging.error('{0}'.format(msg))

