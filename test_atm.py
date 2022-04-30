import sqlite3
import unittest
from users import *

util = login_utility()


class LoginTests(unittest.TestCase):

    def testLogInSuccess(self):
        self.assertTrue(login(*util, "Ryan", "ryanpassword"), "login failure")

    def testLogInFailure(self):
        self.assertFalse(login(*util, "Ryan", None), "entered password grants access")


class SignupTests(unittest.TestCase):

    def testSignUpSuccess(self):
        self.assertTrue(signup(*util, "test", "test", "test"), "signup failure")

    def testTakenUsername(self):
        self.assertEqual("exception", signup(*util, "Ryan", "PW", "PW"), "the entered name is not in use")

    def testConfirmFailure(self):
        self.assertFalse(signup(*util, "test2", "test", "bro"))


class DepositTests(unittest.TestCase):

    def testDeposit50(self):
        self.assertEqual(50, deposit(*util, "Ryan", 50), "You did not deposit $50")

    def testResponseType(self):
        self.assertRaises(TypeError, deposit(*util, "Ryan", "ok and?"))


class WithdrawalTests(unittest.TestCase):

    def testWithdraw50(self):
        self.assertEqual(50, withdraw(*util, "Ryan", 50), "You did not withdraw $50")

    def testResponseType(self):
        self.assertRaises(TypeError, withdraw(*util, "Ryan", "str"))


# "username" is a primary key, tests are broken if "test" and "test2" are not removed
def remove_user(con, cur):
    cur.execute("DELETE FROM users WHERE username='test'")
    cur.execute("DELETE FROM users WHERE username='test2'")
    con.commit()


remove_user(*util)


if __name__ == '__main__':
    unittest.main()
