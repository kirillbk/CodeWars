# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.

def solution(n):
	dd = { 1 : 'I', 4: 'IV',  5 : 'V', 9: 'IX',  10 : 'X', 40 : 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}
	digits = list(dd.keys())
	digits.sort(reverse=True)
	res = ''
	for d in digits:
		mod = n // d
		res += ''.join([dd[d] for _ in range(mod)])
		n %= d
	return res

print(solution(1000))
print(solution(123))
print(solution(9))

print(solution(1),'I', "solution(1),'I'")
print(solution(4),'IV', "solution(4),'IV'")
print(solution(6),'VI', "solution(6),'VI'")
print(solution(14),'XIV', "solution(14),'XIV")
print(solution(21),'XXI', "solution(21),'XXI'")
print(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
print(solution(91),'XCI', "solution(91),'XCI'")
print(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
print(solution(1000), 'M', 'solution(1000), M')
print(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
print(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")
