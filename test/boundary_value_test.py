import unittest
from source.my_function import check_credit_worthiness

class TestCreditworthiness(unittest.TestCase):

    def test_case_1(self):
        """
        Test case 1: Thu nhập 2.5 tỷ, Lịch sử tín dụng 0 - Tín dụng thấp
        """
        self.assertEqual(check_credit_worthiness(2.5e9, 0), "Tín dụng thấp")

    def test_case_2(self):
        """
        Test case 2: Thu nhập 2.5 tỷ, Lịch sử tín dụng 5 - Tín dụng trung bình
        """
        self.assertEqual(check_credit_worthiness(2.5e9, 5), "Tín dụng trung bình")

    def test_case_3(self):
        """
        Test case 3: Thu nhập 2.5 tỷ, Lịch sử tín dụng 8 - Tín dụng cao
        """
        self.assertEqual(check_credit_worthiness(2.5e9, 8), "Tín dụng cao")

    def test_case_4(self):
        """
        Test case 4: Thu nhập 2.5 tỷ, Lịch sử tín dụng 10 - Tín dụng cao
        """
        self.assertEqual(check_credit_worthiness(2.5e9, 10), "Tín dụng cao")

    def test_case_5(self):
        """
        Test case 5: Thu nhập 0, Lịch sử tín dụng 5 - Tín dụng thấp
        """
        self.assertEqual(check_credit_worthiness(0, 5), "Tín dụng thấp")

    def test_case_6(self):
        """
        Test case 6: Thu nhập 100 triệu, Lịch sử tín dụng 5 - Tín dụng trung bình
        """
        self.assertEqual(check_credit_worthiness(100e6, 5), "Tín dụng trung bình")

    def test_case_7(self):
        """
        Test case 7: Thu nhập 1 tỷ, Lịch sử tín dụng 5 - Tín dụng trung bình
        """
        self.assertEqual(check_credit_worthiness(1e9, 5), "Tín dụng trung bình")

    def test_case_8(self):
        """
        Test case 8: Thu nhập 5 tỷ, Lịch sử tín dụng 5 - Tín dụng trung bình
        """
        self.assertEqual(check_credit_worthiness(5e9, 5), "Tín dụng trung bình")

    def test_case_9(self):
        """
        Test case 9: Thu nhập cận trung bình, Lịch sử tín dụng trung bình - Tín dụng trung bình
        """
        self.assertEqual(check_credit_worthiness(2.5e9, 5), "Tín dụng trung bình")

if __name__ == "__main__":
    unittest.main()

