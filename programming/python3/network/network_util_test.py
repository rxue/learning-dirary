import unittest
from network_util import *

class TestNetworkUtil(unittest.TestCase):
    def testGetByteInInt(self):
        actualResult = getByteInInt('127.0.0.1',0)
        self.assertEqual(127, actualResult)

    def testGetType_A(self):
        actualResult = getType('1.0.0.1')
        self.assertEqual(NetworkType.A, actualResult)
    def testGetType_LOOPBACK(self):
        actualResult = getType('127.0.0.1')
        self.assertEqual(NetworkType.LOOPBACK, actualResult)
    def testGetType_B(self):
        actualResult = getType('128.0.0.1')
        self.assertEqual(NetworkType.B, actualResult)
    def testGetType_C(self):
        actualResult = getType('192.0.0.1')
        self.assertEqual(NetworkType.C, actualResult)