import Code
import unittest
class Testcode(unittest.TestCase):
    def test_CorrectUsernameAndCorrectPassword(self):
        self.assertEqual(Code.login('thirawat', '123456'),True)
    def test_CorrectUsernameButIncorrectPassword(self):
        self.assertEqual(Code.login('thirawat', '12356'),False)
    def test_IncorrectUsernameButCorrectPassword(self):
        self.assertEqual(Code.login('thiawat', '123456'),False)
    def test_IncorrectUsernameAndIncorrectPassword(self):
        self.assertEqual(Code.login('thiraat', '12346'),False)
  
if __name__ == '__main__':
    unittest.main()
