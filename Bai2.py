# Chức năng 1: Sử dụng vòng lặp chạy đúng 7 lần để yêu cầu người dùng nhập vào doanh thu của từng ngày (In rõ thông báo từ "Ngày 1" đến "Ngày 7").
# Chức năng 2: Sử dụng các biến tích lũy để tính toán:
# Tổng doanh thu của cả tuần.
# Doanh thu trung bình mỗi ngày trong tuần.
# Chức năng 3: Đếm xem có bao nhiêu ngày có doanh thu đạt từ 5,000,000 VND trở lên.

total_revenue = 0
number_today = 0
for i in range(1,8):
    revenue = int(input(f"Nhập doanh thu Ngày {i}: "))
    total_revenue += revenue
    if revenue >= 5000000:
        number_today += 1
avg_revenue =  total_revenue/7
print (f"""
-- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---
Tổng doanh thu cả tuần: {total_revenue} VND
Doanh thu trung bình mỗi ngày: {avg_revenue} VND
Số ngày đạt doanh thu mục tiêu (≥ 5,000,000 VND): {number_today} ngày
""")