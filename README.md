# Nhân đa thức trên trường hữu hạn GF(2^4) và GF(2^8)

* **Họ và tên:** Nguyễn Anh Tú
* **MSSV:** 20233691

## 1. Mô tả đề tài

Cài đặt thuật toán nhân 2 đa thức trên trường hữu hạn $\text{GF}(2^4)$ và $\text{GF}(2^8)$ với các đa thức tối giản tương ứng:

* $\text{GF}(2^4)$: $P(x) = x^4 + x + 1$ (`10011` hoặc `0x13`)
* $\text{GF}(2^8)$: $P(x) = x^8 + x^4 + x^3 + x + 1$ (`100011011` hoặc `0x11b`)

## 2. Cách thức hoạt động

Do hệ số trên $\text{GF}(2)$ chỉ gồm 0 và 1 nên phép cộng/trừ tương đương phép **XOR**.

* **Bước 1 (Nhân):** Duyệt từng bit của đa thức $B$, nếu bit bằng 1 thì dịch trái $A$ tương ứng rồi XOR vào tích.
* **Bước 2 (Chia dư):** Lấy tích thu được XOR với đa thức tối giản $P(x)$ (đã dịch bit cho khớp bậc cao nhất) cho tới khi bậc nhỏ hơn bậc của trường.

## 3. Cấu trúc mã nguồn

* `nhan_da_thuc.py`: Chương trình chính thực hiện các phép toán nhân đa thức, hỗ trợ menu tương tác và hiển thị từng bước rút gọn.
* `test_nhan_da_thuc.py`: Bộ kiểm thử tự động (Unit Test) sử dụng thư viện `unittest` để kiểm chứng tính đúng đắn của thuật toán.

## 4. Hướng dẫn sử dụng

### 4.1 Chạy chương trình chính tương tác

```bash
python3 nhan_da_thuc.py
```

Chương trình cho phép nhập số dưới dạng:
* Nhị phân: ví dụ `1011` hoặc `0b1011`
* Thập phân: ví dụ `11`
* Thập lục phân (Hex): ví dụ `0x57`

### 4.2 Chạy Unit Test kiểm thử

Để chạy toàn bộ các ca kiểm thử với thông tin chi tiết:

```bash
python3 -m unittest test_nhan_da_thuc.py -v
```

hoặc:

```bash
python3 test_nhan_da_thuc.py
```

## 5. Danh mục các ca kiểm thử (Unit Test)

Bộ kiểm chứng gồm 10 bài test độc lập:

1. `test_tim_bac`: Kiểm tra tính bậc của đa thức (xử lý đúng số 0 là bậc -1, các lũy thừa của x).
2. `test_in_dt`: Kiểm tra hiển thị chuỗi đa thức chuẩn $x^n + \dots + 1$.
3. `test_chuyen_doi_so`: Kiểm tra khả năng nhận diện các hệ đếm (nhị phân, thập phân, hex).
4. `test_nhan_co_ban_gf16`: Kiểm tra phép nhân bậc thấp không tràn trên $\text{GF}(2^4)$.
5. `test_nhan_voi_khong`: Kiểm tra tính chất nhân với phần tử 0 ($a \times 0 = 0$).
6. `test_nhan_voi_mot`: Kiểm tra tính chất nhân với phần tử đơn vị 1 ($a \times 1 = a$).
7. `test_nhan_vuot_bac_gf16`: Kiểm tra phép nhân có bậc $\ge 4$ và rút gọn theo $x^4 + x + 1$.
8. `test_gf256_aes_vector`: Kiểm tra với các vector mẫu chuẩn trong tài liệu tiêu chuẩn AES (NIST FIPS 197):
   * $\{57\} \times \{83\} = \{c1\}$
   * $\{57\} \times \{13\} = \{fe\}$
   * $\{02\} \times \{87\} = \{15\}$
   * $\{02\} \times \{57\} = \{ae\}$
   * $\{03\} \times \{57\} = \{f9\}$
   * $\{80\} \times \{02\} = \{1b\}$ (hàm xtime)
9. `test_tinh_chat_giao_hoan`: Kiểm tra tính giao hoán $a \cdot b = b \cdot a$ trên toàn bộ trường.
10. `test_tinh_chat_phan_phoi`: Kiểm tra tính phân phối $a \cdot (b \oplus c) = (a \cdot b) \oplus (a \cdot c)$.
