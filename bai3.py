bill = int(input("Nhập số lượng hóa đơn trong ca: "))
for i in range(bill):
    value_bill = int(input(f"Nhập giá trị hóa đơn thứ {i + 1}: "))
    if i == 0:
        max_bill = value_bill
        min_bill = value_bill
    else:
        if value_bill > max_bill:
            max_bill = value_bill

        if value_bill < min_bill:
            min_bill = value_bill
print(f"""
--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---
Hóa đơn có giá trị cao nhất: {max_bill} VND
Hóa đơn có giá trị thấp nhất: {min_bill} VND
""")