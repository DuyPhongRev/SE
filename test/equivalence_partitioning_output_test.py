import unittest
from source.my_function import check_credit_worthiness

class TestCheckCreditWorthiness(unittest.TestCase):
    def test_case1(self):
        """Test case 1."""
        self.assertEqual(check_credit_worthiness(3.87e9, 17), "Đầu vào không hợp lệ")

    def test_case2(self):
        """Test case 2."""
        self.assertEqual(check_credit_worthiness(7.27e8, 17), "Đầu vào không hợp lệ")

    def test_case3(self):
        """Test case 3."""
        self.assertEqual(check_credit_worthiness(1.27e6, 17), "Đầu vào không hợp lệ")

    def test_case4(self):
        """Test case 4."""
        self.assertEqual(check_credit_worthiness(-6.54e8, 9), "Đầu vào không hợp lệ")

    def test_case5(self):
        """Test case 5."""
        self.assertEqual(check_credit_worthiness(-6.54e8, 7), "Đầu vào không hợp lệ")

    def test_case6(self):
        """Test case 6."""
        self.assertEqual(check_credit_worthiness(-6.54e8, 3), "Đầu vào không hợp lệ")

    def test_case7(self):
        """Test case 7."""
        self.assertEqual(check_credit_worthiness(-6.54e8, 17), "Đầu vào không hợp lệ")

    def test_case8(self):
        """Test case 8."""
        self.assertEqual(check_credit_worthiness(3.87e9, 9), "Tín dụng cao")

    def test_case9(self):
        """Test case 9."""
        self.assertEqual(check_credit_worthiness(3.87e9, 3), "Tín dụng thấp")

    def test_case10(self):
        """Test case 10."""
        self.assertEqual(check_credit_worthiness(7.27e8, 3), "Tín dụng thấp")

    def test_case11(self):
        """Test case 11."""
        self.assertEqual(check_credit_worthiness(1.27e6, 9), "Tín dụng thấp")

    def test_case12(self):
        """Test case 12."""
        self.assertEqual(check_credit_worthiness(1.27e6, 7), "Tín dụng thấp")

    def test_case13(self):
        """Test case 13."""
        self.assertEqual(check_credit_worthiness(1.27e6, 3), "Tín dụng thấp")

    def test_case14(self):
        """Test case 14."""
        self.assertEqual(check_credit_worthiness(7.27e8, 9), "Tín dụng trung bình")

    def test_case15(self):
        """Test case 15."""
        self.assertEqual(check_credit_worthiness(7.27e8, 7), "Tín dụng trung bình")

    def test_case16(self):
        """Test case 16."""
        self.assertEqual(check_credit_worthiness(3.87e9, 7), "Tín dụng trung bình")

if __name__ == "__main__":
    unittest.main()
