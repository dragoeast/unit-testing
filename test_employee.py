import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee_1 = Employee("Krisztian", "Markella", 60_000)
        self.employee_2 = Employee("Christian", "Markella", 10_000)

    def tearDown(self) -> None:
        pass

    def test_email(self):
        self.assertEqual(self.employee_1.email, "Krisztian.Markella@email.com")
        self.assertEqual(self.employee_2.email, "Christian.Markella@email.com")
        
        self.employee_2.first = "Mark"

        self.assertEqual(self.employee_2.email, "Mark.Markella@email.com")

    def test_fullname(self):
        self.assertEqual(self.employee_1.fullname, "Krisztian Markella")
        self.assertEqual(self.employee_2.fullname, "Christian Markella")
        
        self.employee_2.first = "Mark"

        self.assertEqual(self.employee_2.fullname, "Mark Markella")

    def test_raise(self):
        self.assertEqual(self.employee_1.pay, 60_000)
        self.assertEqual(self.employee_2.pay, 10_000)
        
        self.employee_1.apply_raise()
        self.employee_2.apply_raise()

        self.assertEqual(self.employee_1.pay, 66_000)
        self.assertEqual(self.employee_2.pay, 11_000)

if __name__ == "__main__":
    unittest.main()
