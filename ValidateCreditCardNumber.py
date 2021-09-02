# In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.
# Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.

def validate(n):
	digits = [int(i) for i in str(n)]
	digits.reverse()
	digits[1::2] = [ d * 2 if d * 2 < 9 else sum(map(int, str(d * 2))) for d in digits[1::2]]
	return True if sum(digits) % 10 == 0 else False
