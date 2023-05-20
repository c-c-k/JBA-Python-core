from logging import getLogger, DEBUG
from logging.handlers import RotatingFileHandler

from mem_tool import main

logger = getLogger()
logger.setLevel(DEBUG)
frh = RotatingFileHandler('debug.log')
frh.setLevel(DEBUG)
logger.addHandler(frh)

if __name__ == "__main__":
    main()
