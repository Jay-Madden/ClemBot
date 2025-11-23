import logging
import os

import seqlog
from seqlog import ConsoleStructuredLogHandler, StructuredLogger, StructuredRootLogger

logging.setLoggerClass(StructuredLogger)

logging.root = StructuredRootLogger(logging.WARNING)
logging.Logger.root = logging.root
logging.Logger.manager = logging.Manager(logging.Logger.root)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(module)s %(message)s",
    handlers=[ConsoleStructuredLogHandler()],
    level=logging.INFO,
)
