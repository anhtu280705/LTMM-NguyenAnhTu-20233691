# Nhân đa thức trên trường hữu hạn GF(2^4) và GF(2^8)

* **Họ và tên:** Nguyễn Anh Tú

* **MSSV:** 20233691

## 1. Mô tả đề tài

Cài đặt thuật toán nhân 2 đa thức trên trường hữu hạn $\text{GF}(2^4)$ và $\text{GF}(2^8)$ với các đa thức tối giản tương ứng:

* $\text{GF}(2^4)$: $P(x) = x^4 + x + 1$ (`10011`)

* $\text{GF}(2^8)$: $P(x) = x^8 + x^4 + x^3 + x + 1$ (`100011011`)

## 2. Cách thức hoạt động

Do hệ số trên $\text{GF}(2)$ chỉ gồm 0 và 1 nên phép cộng/trừ tương đương phép **XOR**.

* **Bước 1 (Nhân):** Duyệt từng bit của đa thức $B$, nếu bit bằng 1 thì dịch trái $A$ tương ứng rồi XOR vào tích.

* **Bước 2 (Chia dư):** Lấy tích thu được XOR với đa thức tối giản $P(x)$ (đã dịch bit cho khớp bậc cao nhất) cho tới khi bậc nhỏ hơn bậc của trường.

## 