def zero(f = None):
    return 0 if not f else f(0)
def one(f = None):
	return 1 if not f else f(1)
def two(f = None):
	return 2 if not f else f(2)
def three(f = None): 
     return 3 if not f else f(3)
def four(f = None):
     return 4 if not f else f(4)
def five(f = None):
     return 5 if not f else f(5)
def six(f = None):
     return 6 if not f else f(6)
def seven(f = None):
     return 7 if not f else f(7)
def eight(f = None):
     return 8 if not f else f(8)
def nine(f = None):
     return 9 if not f else f(9)

def plus(a):
	def p(b):
		return a + b
	return p 

def minus(a):
	def m(b):
		return b - a
	return m

def times(a):
	def t(b):
		return a * b
	return t

def divided_by(a):
	def d(b):
		return b // a
	return d

print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)