number = 200
turn = 1

while turn <= 5:
    guess = int(input(f"Lượt đoán {turn} - Nhập số của bạn: "))

    if guess < number:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")
    elif guess > number:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")
    else:
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        break

    turn += 1

print("--- TRÒ CHƠI KẾT THÚC ---")
