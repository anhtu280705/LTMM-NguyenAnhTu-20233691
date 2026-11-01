# da thuc toi gian cho GF(2^4) va GF(2^8)
p_gf16 = 0b10011
p_gf256 = 0b100011011

# ham chuyen doi input sang so nguyen
def chuyen_doi_so(chuoi):
    # ho tro nhap he 2 (1011 hoac 0b1011), he 16 (0x57), hoac he 10 (87)
    chuoi = chuoi.strip().lower()
    if not chuoi:
        raise ValueError("Chuoi nhap vao bi rong!")
    if chuoi.startswith("0b"):
        val = int(chuoi, 2)
    elif chuoi.startswith("0x"):
        val = int(chuoi, 16)
    elif all(c in "01" for c in chuoi) and len(chuoi) > 1:
        val = int(chuoi, 2)
    else:
        val = int(chuoi)
    if val < 0:
        raise ValueError("Gia tri phai la so khong am!")
    return val

def tim_bac(so):
    if so == 0:
        return -1
    bac = -1
    while so > 0:
        so = so >> 1
        bac = bac + 1
    return bac

def in_dt(so):
    # in da thuc duoi dang bieu dien toan hoc x^n + ... + 1
    if so is None or so <= 0:
        return "0"
    b = tim_bac(so)
    if b < 0:
        return "0"
    ds = []
    for i in range(b, -1, -1):
        if (so >> i) & 1:
            if i == 0:
                ds.append("1")
            elif i == 1:
                ds.append("x")
            else:
                ds.append("x^" + str(i))
    if not ds:
        return "0"
    return " + ".join(ds)

def nhan_hai_da_thuc(x, y, in_buoc=True):
    kq = 0
    i = 0
    t = y
    if in_buoc:
        print("  --- bat dau nhan ---")
    
    if x == 0 or t == 0:
        return 0
        
    while t > 0:
        if t & 1:
            phan_du = x << i
            if in_buoc:
                print("  bit thu", i, "bang 1, XOR them:", in_dt(phan_du))
            kq = kq ^ phan_du
        t = t >> 1
        i = i + 1
        
    if in_buoc:
        print("  tich chua rut gon la:", in_dt(kq))
    return kq

def chia_va_lay_du(tich, p_toi_gian, in_buoc=True):
    if in_buoc:
        print("  --- rut gon ---")
    bp = tim_bac(p_toi_gian)
    
    if tim_bac(tich) < bp:
        if in_buoc:
            print("  bac nho hon nen thoi khong chia nua")
        return tich
        
    lan = 1
    while tim_bac(tich) >= bp:
        chenh_lech = tim_bac(tich) - bp
        p_dich = p_toi_gian << chenh_lech
        if in_buoc:
            print("  lan", lan, ": XOR voi", in_dt(p_dich))
        tich = tich ^ p_dich
        if in_buoc:
            print("  ket qua sau khi XOR:", in_dt(tich))
        lan = lan + 1
        
    return tich

def nhan_truong(a, b, p, ten="GF", in_buoc=True):
    if in_buoc:
        print("\n==============================")
        print("Dang tinh tren truong:", ten)
        print("A =", in_dt(a))
        print("B =", in_dt(b))
        print("P =", in_dt(p))
    
    tich_chua_rut_gon = nhan_hai_da_thuc(a, b, in_buoc=in_buoc)
    ket_qua_cuoi = chia_va_lay_du(tich_chua_rut_gon, p, in_buoc=in_buoc)
    
    if in_buoc:
        print("------------------------------")
        print("KET QUA CUOI CÙNG:", in_dt(ket_qua_cuoi), "| Dec:", ket_qua_cuoi)
    return ket_qua_cuoi

def nhan_gf(a, b, truong="gf16", in_buoc=False):
    # ham tien ich de goi nhan nhanh tren truong mong muon
    ten = str(truong).lower().strip()
    if ten in ["1", "gf16", "gf(2^4)", "4"]:
        p = p_gf16
        ten_hien_thi = "GF(2^4)"
    elif ten in ["2", "gf256", "gf(2^8)", "8"]:
        p = p_gf256
        ten_hien_thi = "GF(2^8)"
    else:
        raise ValueError("Truong khong hop le, chi chon gf16 hoac gf256")
    return nhan_truong(a, b, p, ten_hien_thi, in_buoc=in_buoc)

def main():
    while True:
        print("\n==============================")
        print("CHUONG TRINH NHAN DA THUC")
        print("1. GF(2^4)")
        print("2. GF(2^8)")
        print("q. Thoat")
        
        lua_chon = input("nhap lua chon (1, 2 hoac q): ").strip().lower()
        if lua_chon == "q":
            print("Tam biet!")
            break
            
        if lua_chon == "1":
            p = p_gf16
            ten_truong = "GF(2^4)"
        elif lua_chon == "2":
            p = p_gf256
            ten_truong = "GF(2^8)"
        else:
            print("Lua chon khong hop le, vui long chon 1 hoac 2!")
            continue
            
        try:
            print("nhap da thuc A (nhi phan, thap phan hoac hex 0x...):")
            s1 = input(" > ").strip()
            a = chuyen_doi_so(s1)
                
            print("nhap da thuc B (nhi phan, thap phan hoac hex 0x...):")
            s2 = input(" > ").strip()
            b = chuyen_doi_so(s2)
            
            nhan_truong(a, b, p, ten_truong, in_buoc=True)
        except Exception as e:
            print("Loi nhap du lieu:", e)

if __name__ == "__main__":
    main()