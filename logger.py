import logging


def get_logger():
    logger = logging.getLogger('app')
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)

    logger.addHandler(handler)

    return logger


log = get_logger()
