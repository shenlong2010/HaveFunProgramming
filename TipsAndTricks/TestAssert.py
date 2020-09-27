def apply_discount(product, discount):
	price = int(product['price'] * (1.0 - discount))

	# This statement guarantee discount price 
	# cannot be lower than 0 and
	# cannot be higher than original price
	assert 0 <= price <= product['price']

	return price

shoes = {'name': 'Fancy Shoes',
		 'price': 14900}

print(apply_discount(shoes, 0.25)) # 11175
print(apply_discount(shoes, 2.0))