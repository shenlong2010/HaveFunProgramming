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

def is_admin():
	pass

def has_product():
	pass

def get_product():
	pass

def delete():
	pass

# Never use assertions to do data
def delete_product(prod_id, user):
	if not user.is_admin():
		raise AuthError('Must be admin to delete')
	if not store.has_product(product_id):
		raise ValueError('Unknown product id')
	store.get_product(product_id).delete()


