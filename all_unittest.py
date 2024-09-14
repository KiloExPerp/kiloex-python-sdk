import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

from config_kiloex import BNBTEST,OTEST,kiloconfigs
class TestConfig(unittest.TestCase):
    def test_config_len(self):
        self.assertTrue(len(kiloconfigs) > 0)
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

import asset_kiloex
class TestAsset(unittest.TestCase):
    def test_get_asset(self):
        self.assertTrue(asset_kiloex.get_asset(kiloconfigs[BNBTEST], kiloconfigs[OTEST]) >= usdt_kiloex.get_balance(kiloconfigs[BNBTEST]))

import api_kiloex
class TestApi(unittest.TestCase):
    def test_index_symbols(self):
        self.assertTrue(len(api_kiloex.index_symbols(BNBTEST)) >= 0)
    def test_index_symbol(self):
        self.assertEqual(api_kiloex.index_symbol(1, BNBTEST), "ETHUSD")
        self.assertEqual(api_kiloex.index_symbol(222, BNBTEST), None)
    def test_query_fundingList(self):
        self.assertTrue(len(api_kiloex.query_fundingList(BNBTEST)) >= 0)
    def test_query_productList(self):
        self.assertTrue(len(api_kiloex.query_productList(BNBTEST)) >= 0)
    def test_index_prices_current(self):
        self.assertTrue(len(api_kiloex.index_prices_current(BNBTEST)) >= 0)
    def test_index_price(self):
        self.assertTrue(api_kiloex.index_price(1, BNBTEST) > 2000)


if __name__ == '__main__':
    unittest.main()
