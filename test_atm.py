import sqlite3
import unittest
from users import *

util = login_utility()


class test_case1(unittest.TestCase):

    def testLogInSuccess(self):
        self.assertTrue(login(*util, "Ryan", "ryanpassword"), "login failure")

    def testLogInFailure(self):
        self.assertFalse(login(*util, "Ryan", None), "entered password grants access")


class test_case3(unittest.TestCase):

    def testDeposit50(self):
        self.assertEqual(50, deposit(*util, "Ryan", 50), "You did not deposit $50")

    def testResponseType(self):
        self.assertRaises(TypeError, deposit(*util, "Ryan", "ok and?"))


# "username" is a primary key, tests are broken if "test" and "test2" are not removed
def remove_user(con, cur):
    cur.execute("DELETE FROM users WHERE username='test'")
    cur.execute("DELETE FROM users WHERE username='test2'")
    con.commit()


remove_user(*util)


if __name__ == '__main__':
    unittest.main()
