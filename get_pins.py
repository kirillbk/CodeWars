from itertools import product

def get_pins(observed):
	keys = {'0':'08', '1':'124', '2':'1235', '3':'236', '4':'1457', '5':'24568',
	'6':'3569', '7':'478', '8':'57890', '9':'689'}
	return list(''.join(pin) for pin in product(*(keys[d] for d in observed)))

print(get_pins('8'))
print(get_pins('11'))
print(get_pins('59'))


