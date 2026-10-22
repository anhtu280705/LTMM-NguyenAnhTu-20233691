p_gf16 = 0b10011
p_gf256 = 0b100011011

def tim_bac(so):
    if so == 0:
        return -1
    bac = -1
    while so > 0:
        so = so >> 1
        bac = bac + 1
    return bac

def in_dt(so):
    if so == 0:
        return "0"
  b = tim_bac(so)
    ds = []
    i = b
    while i >= 0:
        if (so >> i) & 1:
            if i == 0:
                ds.append("1")
            elif i == 1:
                ds.append("x")
            else:
                ds.append("x^" + str(i));
        
        i = i - 1
    kq_chuoi = " + ".join(ds)
    return kq_chuoi

def nhan_hai_da_thuc(x, y):
    kq = 0
    i = 0
    t = y
    print("  --- bat dau nhan ---")
    
    if x == 0 or t == 0:
        return 0
        
    while t > 0:
        if t & 1:
            phan_du = x << i
            print("  bit thu", i, "bang 1, XOR them:", in_dt(phan_du))
            kq = kq ^ phan_du
        t = t >> 1
        i = i + 1
        
    print("  tich chua rut gon la:", in_dt(kq))
    return kq

def chia_va_lay_du(tich, p_toi_gian):
    print("  --- rut gon ---")
    bp = tim_bac(p_toi_gian)
    
    if tim_bac(tich) < bp:
        print("  bac nho hon nen thoi khong chia nua")
        return tich
        
    lan = 1
    while tim_bac(tich) >= bp:
        chenh_lech = tim_bac(tich) - bp
        p_dich = p_toi_gian << chenh_lech
        print("  lan", lan, ": XOR voi", in_dt(p_dich))
        tich = tich ^ p_dich
        print("  ket qua sau khi XOR:", in_dt(tich))
        lan = lan + 1
        
    return tich

def nhan_truong(a, b, p, ten):
    print("\n==============================")
    print("Dang tinh tren truong:", ten)
    print("A =", in_dt(a))
    print("B =", in_dt(b))
    print("P =", in_dt(p))
    
    tich_chua_rut_gon = nhan_hai_da_thuc(a, b)
    ket_qua_cuoi = chia_va_lay_du(tich_chua_rut_gon, p)
    
    print("------------------------------")
    print("KET QUA CUOI CÙNG:", in_dt(ket_qua_cuoi), "| Dec:", ket_qua_cuoi)
    return ket_qua_cuoi

def main():
    print("CHUONG TRINH NHAN DA THUC")
    print("1. GF(2^4)")
    print("2. GF(2^8)")
    
    lua_chon = input("nhap lua chon (1 hoac 2): ").strip()
    
    if lua_chon == "1":
        p = p_gf16
        ten_truong = "GF(2^4)"
    elif lua_chon == "2":
        p = p_gf256
        ten_truong = "GF(2^8)"
    else:
        print("nhap sai roi")
        return
        
    print("nhap da thuc A:")
    s1 = input(" > ").strip()
    if all(c in "01" for c in s1):
        a = int(s1, 2)
    else:
        a = int(s1)
        
    print("nhap da thuc B:")
    s2 = input(" > ").strip()
    if all(c in "01" for c in s2):
        b = int(s2, 2)
    else:
        b = int(s2)
        
    nhan_truong(a, b, p, ten_truong)

if __name__ == "__main__":
    main()