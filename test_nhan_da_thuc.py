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

    def test_nhan_voi_khong(self):
        # kiem tra a * 0 luon bang 0
        for val in [0, 1, 5, 11, 15]:
            self.assertEqual(nhan_gf(val, 0, "gf16"), 0)
            self.assertEqual(nhan_gf(0, val, "gf16"), 0)
        self.assertEqual(nhan_gf(0x57, 0, "gf256"), 0)
        self.assertEqual(nhan_gf(0, 0x83, "gf256"), 0)

    def test_nhan_voi_mot(self):
        # kiem tra phan tu don vi a * 1 == a
        for val in range(16):
            self.assertEqual(nhan_gf(val, 1, "gf16"), val)
            self.assertEqual(nhan_gf(1, val, "gf16"), val)
        self.assertEqual(nhan_gf(0x57, 1, "gf256"), 0x57)
        self.assertEqual(nhan_gf(1, 0xc1, "gf256"), 0xc1)

    def test_nhan_vuot_bac_gf16(self):
        # kiem tra phep nhan can rut gon tren GF(2^4)
        # x^3 * x = x^4 mod (x^4 + x + 1) = x + 1 (8 * 2 = 3)
        self.assertEqual(nhan_gf(8, 2, "gf16"), 3)
        # x^3 * x^3 = x^6 mod P = x^3 + x^2 (8 * 8 = 12)
        self.assertEqual(nhan_gf(8, 8, "gf16"), 12)

    def test_gf256_aes_vector(self):
        # cac vector kiem thu chuan trong tai lieu AES (FIPS 197)
        # 0x57 * 0x83 = 0xc1
        self.assertEqual(nhan_gf(0x57, 0x83, "gf256"), 0xc1)
        # 0x57 * 0x13 = 0xfe
        self.assertEqual(nhan_gf(0x57, 0x13, "gf256"), 0xfe)
        # 0x02 * 0x87 = 0x15
        self.assertEqual(nhan_gf(0x02, 0x87, "gf256"), 0x15)
        # 0x02 * 0x57 = 0xae
        self.assertEqual(nhan_gf(0x02, 0x57, "gf256"), 0xae)
        # 0x03 * 0x57 = 0xf9
        self.assertEqual(nhan_gf(0x03, 0x57, "gf256"), 0xf9)
        # xtime(0x80): 0x80 * 0x02 = 0x1b (da thuc toi gian)
        self.assertEqual(nhan_gf(0x80, 0x02, "gf256"), 0x1b)

    def test_tinh_chat_giao_hoan(self):
        # kiem tra tinh chat giao hoan a * b == b * a tren toan bo GF(2^4)
        for a in range(16):
            for b in range(16):
                self.assertEqual(nhan_gf(a, b, "gf16"), nhan_gf(b, a, "gf16"))

        # kiem tra giao hoan tren mot so phan tu GF(2^8)
        mau = [0x01, 0x02, 0x57, 0x83, 0xae, 0xff]
        for a in mau:
            for b in mau:
                self.assertEqual(nhan_gf(a, b, "gf256"), nhan_gf(b, a, "gf256"))

    def test_tinh_chat_phan_phoi(self):
        # kiem tra tinh chat phan phoi: a * (b ^ c) == (a * b) ^ (a * c)
        a = 0x57
        b = 0x83
        c = 0x13
        ve_trai = nhan_gf(a, b ^ c, "gf256")
        ve_phai = nhan_gf(a, b, "gf256") ^ nhan_gf(a, c, "gf256")
        self.assertEqual(ve_trai, ve_phai)

        # kiem tra phan phoi tren GF(2^4)
        for x in [3, 7, 11]:
            for y in [5, 9, 13]:
                for z in [2, 6, 14]:
                    self.assertEqual(
                        nhan_gf(x, y ^ z, "gf16"),
                        nhan_gf(x, y, "gf16") ^ nhan_gf(x, z, "gf16")
                    )

if __name__ == "__main__":
    unittest.main()
