import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

from config_kiloex import BNBTEST,OTEST,kiloconfigs
class TestConfig(unittest.TestCase):
    def test_config_len(self):
        self.assertEqual(len(kiloconfigs), 4)
    def test_config(self):
        config = kiloconfigs[BNBTEST]
        self.assertEqual(config.chain, BNBTEST)
        self.assertEqual(config.chain_id, 97)

import usdt_kiloex
class TestUsdt(unittest.TestCase):
    def test_get_balance(self):
        self.assertTrue(usdt_kiloex.get_balance(kiloconfigs[BNBTEST]) > 0)
    def test_get_available_balance(self):
        self.assertTrue(usdt_kiloex.get_available_balance(kiloconfigs[BNBTEST], kiloconfigs[OTEST]) <= usdt_kiloex.get_balance(kiloconfigs[BNBTEST]))
        self.assertTrue(usdt_kiloex.get_available_balance(kiloconfigs[BNBTEST], kiloconfigs[OTEST]) <= usdt_kiloex.get_balance(kiloconfigs[OTEST]))

import perp_kiloex
class TestPerp(unittest.TestCase):
    def test_get_positions(self):
        ids = [1, 2, 23, 31]
        positions = perp_kiloex.get_positions(kiloconfigs[BNBTEST], ids)
        self.assertTrue(len(positions) >= 0)

import api_kiloex
class TestApi(unittest.TestCase):
    def test_queryKiloCache(self):
        self.assertEqual(api_kiloex.queryKiloCache(BNBTEST).status_code, 200)
        self.assertTrue(len(api_kiloex.queryKiloCache(BNBTEST).text) >= 0)
    def test_queryProducts(self):
        self.assertEqual(api_kiloex.queryProducts(BNBTEST).status_code, 200)
    def test_index_prices(self):
        self.assertEqual(api_kiloex.index_prices(BNBTEST).status_code, 200)
    def test_index_price(self):
        self.assertTrue(api_kiloex.index_price(1, BNBTEST) > 3000)


if __name__ == '__main__':
    unittest.main()
