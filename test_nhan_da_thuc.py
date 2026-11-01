import unittest
from nhan_da_thuc import (
    tim_bac,
    in_dt,
    chuyen_doi_so,
    nhan_gf,
    p_gf16,
    p_gf256
)

class TestNhanDaThuc(unittest.TestCase):

    def test_tim_bac(self):
        # kiem tra bac cua da thuc
        self.assertEqual(tim_bac(0), -1)
        self.assertEqual(tim_bac(1), 0)    # 1 la x^0
        self.assertEqual(tim_bac(2), 1)    # 10_2 la x^1
        self.assertEqual(tim_bac(3), 1)    # 11_2 la x^1
        self.assertEqual(tim_bac(4), 2)    # 100_2 la x^2
        self.assertEqual(tim_bac(0b10011), 4) # bac 4 cua GF(2^4)
        self.assertEqual(tim_bac(0b100011011), 8) # bac 8 cua GF(2^8)

    def test_in_dt(self):
        # kiem tra in chuoi da thuc
        self.assertEqual(in_dt(0), "0")
        self.assertEqual(in_dt(1), "1")
        self.assertEqual(in_dt(2), "x")
        self.assertEqual(in_dt(3), "x + 1")
        self.assertEqual(in_dt(5), "x^2 + 1")
        self.assertEqual(in_dt(0b10011), "x^4 + x + 1")

    def test_chuyen_doi_so(self):
        # kiem tra doc input nhieu dinh dang
        self.assertEqual(chuyen_doi_so("1011"), 11)
        self.assertEqual(chuyen_doi_so("0b1011"), 11)
        self.assertEqual(chuyen_doi_so("0x57"), 0x57)
        self.assertEqual(chuyen_doi_so("15"), 15)

    def test_nhan_co_ban_gf16(self):
        # kiem tra phep nhan don gian tren GF(2^4)
        # x * x = x^2 (2 * 2 = 4)
        self.assertEqual(nhan_gf(2, 2, "gf16"), 4)
        # x^2 * x = x^3 (4 * 2 = 8)
        self.assertEqual(nhan_gf(4, 2, "gf16"), 8)

if __name__ == "__main__":
    unittest.main()
