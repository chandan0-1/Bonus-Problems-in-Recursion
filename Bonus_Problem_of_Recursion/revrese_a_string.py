def reveresed(s):
	if len(s)==0:
		return ""

	small=s[0]
	x=reveresed(s[1:])

	return x+small


# 		OR
def reveresed(s):
	if len(s)<=1:
		return s

	return reveresed(s[1:]) + s[0]


# for testing the test cases
from nose.tools import assert_equal

class Test(object):
	def test(self,sol):
		assert_equal(sol("hello"),"olleh")
		assert_equal(sol("abcde"),"edcba")
		assert_equal(sol("123456789"),"987654321")
		print("All Test Case Passed")
tst=Test()
import time
a=time.time()
tst.test(reveresed)
print(time.time()-a)