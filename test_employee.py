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

if __name__ == "__main__":
    unittest.main()
