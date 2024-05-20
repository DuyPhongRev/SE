def check_credit_worthiness(income, history):
    """
    Hàm tính điểm tín dụng khách hàng dựa trên thu nhập và lịch sử tín dụng.

    Args:
        income: Thu nhập cá nhân trong một năm (số nguyên).
        history: Lịch sử tín dụng (số nguyên).

    Returns:
        Chuỗi ký tự thể hiện điểm tín dụng.
    """

    # Kiểm tra tính hợp lệ của đầu vào
#1
    if income < 0 or income > 5e9:
#2
        return "Đầu vào không hợp lệ"
#3
    if history < 0 or history > 10:
#4
        return "Đầu vào không hợp lệ"

    # Xác định điểm tín dụng
#5
    if income <= 100000000 or history < 5: # Lỗi income <= 100000000 dùng dấu < thay <=
#6
        credibility = "Tín dụng thấp"
#7
    elif income >= 1000000000 and history >= 8:
#8
        credibility = "Tín dụng cao"
#9
    else:
#10
        credibility = "Tín dụng trung bình"
#11
    return credibility
