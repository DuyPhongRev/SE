import unittest
from source.my_function import check_credit_worthiness

class EPInputTest(unittest.TestCase):
    def test_invalid_income(self):
        """Kiểm tra trường hợp đầu vào thu nhập không hợp lệ."""
        self.assertEqual(check_credit_worthiness(-4.52e7, 5), "Đầu vào không hợp lệ")

    def test_invalid_history(self):
        """Kiểm tra trường hợp đầu vào lịch sử tín dụng không hợp lệ."""
        self.assertEqual(check_credit_worthiness(5.44e7, -12), "Đầu vào không hợp lệ")

    def test_both_inputs_invalid(self):
        """Kiểm tra trường hợp cả hai đầu vào đều không hợp lệ."""
        self.assertEqual(check_credit_worthiness(-2132342, -4), "Đầu vào không hợp lệ")

    def test_low_credit(self):
        """Kiểm tra trường hợp tín dụng thấp."""
        self.assertEqual(check_credit_worthiness(1.24e6, 0), "Tín dụng thấp")


# Chạy test
if __name__ == "__main__":
    unittest.main()
