import unittest
from source.my_function import check_credit_worthiness

class TestSubBranchCoverage(unittest.TestCase):
    def test_case_1(self):
        """
        Test case 1: Thu nhập -5.00E+06, Lịch sử tín dụng 7 - Đầu vào không hợp lệ
        """
        self.assertEqual(check_credit_worthiness(-5.00e6, 7), "Đầu vào không hợp lệ")

    def test_case_2(self):
        """
        Test case 2: Thu nhập 7.30E+10, Lịch sử tín dụng 10 - Đầu vào không hợp lệ
        """
        self.assertEqual(check_credit_worthiness(7.30e10, 10), "Đầu vào không hợp lệ")

    def test_case_3(self):
        """
        Test case 3: Thu nhập 8.65E+05, Lịch sử tín dụng -6 - Đầu vào không hợp lệ
        """
        self.assertEqual(check_credit_worthiness(8.65e5, -6), "Đầu vào không hợp lệ")

    def test_case_4(self):
        """
        Test case 4: Thu nhập 8.50E+05, Lịch sử tín dụng 23 - Đầu vào không hợp lệ
        """
        self.assertEqual(check_credit_worthiness(8.50e5, 23), "Đầu vào không hợp lệ")

    def test_case_5(self):
        """
        Test case 5: Thu nhập 4.87E+07, Lịch sử tín dụng 5 - Tín dụng thấp
        """
        self.assertEqual(check_credit_worthiness(4.87e7, 5), "Tín dụng thấp")

    def test_case_6(self):
        """
        Test case 6: Thu nhập 6.67E+08, Lịch sử tín dụng 2 - Tín dụng thấp
        """
        self.assertEqual(check_credit_worthiness(6.67e8, 2), "Tín dụng thấp")

    def test_case_7(self):
        """
        Test case 7: Thu nhập 3.20E+09, Lịch sử tín dụng 8 - Tín dụng cao
        """
        self.assertEqual(check_credit_worthiness(3.20e9, 8), "Tín dụng cao")

    def test_case_8(self):
        """
        Test case 8: Thu nhập 5.66E+08, Lịch sử tín dụng 7 - Tín dụng trung bình
        """
        self.assertEqual(check_credit_worthiness(5.66e8, 7), "Tín dụng trung bình")


if __name__ == "__main__":
    unittest.main()