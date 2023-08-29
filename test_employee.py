import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        employee_1 = Employee("Krisztian", "Markella", 60_000)
        employee_2 = Employee("Christian", "Markella", 10_000)

        self.assertEqual(employee_1.email, "Krisztian.Markella@email.com")
        self.assertEqual(employee_2.email, "Christian.Markella@email.com")
        
        employee_2.first = "Mark"

        self.assertEqual(employee_2.email, "Mark.Markella@email.com")

    def test_fullname(self):
        employee_1 = Employee("Krisztian", "Markella", 60_000)
        employee_2 = Employee("Christian", "Markella", 10_000)

        self.assertEqual(employee_1.fullname, "Krisztian Markella")
        self.assertEqual(employee_2.fullname, "Christian Markella")
        
        employee_2.first = "Mark"

        self.assertEqual(employee_2.fullname, "Mark Markella")

    def test_raise(self):
        employee_1 = Employee("Krisztian", "Markella", 60_000)
        employee_2 = Employee("Christian", "Markella", 10_000)

        self.assertEqual(employee_1.pay, 60_000)
        self.assertEqual(employee_2.pay, 10_000)
        
        employee_1.apply_raise()
        employee_2.apply_raise()

        self.assertEqual(employee_1.pay, 66_000)
        self.assertEqual(employee_2.pay, 11_000)

if __name__ == "__main__":
    unittest.main()
