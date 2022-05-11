import unittest
from pyqt.api.impl.ib_api import IbAPI
import time


class TestIbAPI(unittest.TestCase):

    def setUp(self):
        self.ib_api = IbAPI('127.0.0.1', 7496, 526)
        self.ib_api.start()

    def tearDown(self):
        self.ib_api.stop()

    def testIB(self):
        for _ in range(5):
            data = self.ib_api.get_market_snapshot(['AAPL'])
            print('data=', data)
            time.sleep(1)
