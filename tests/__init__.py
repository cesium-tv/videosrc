import os
import logging


LOG_LEVEL = os.getenv('LOG_LEVEL', 'ERROR').upper()

LOGGER = logging.getLogger()
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.getLevelName(LOG_LEVEL))


from tests.test_html import *
from tests.test_mrss import *
from tests.test_odysee import *
from tests.test_peertube import *
from tests.test_rumble import *
from tests.test_timcast import *
